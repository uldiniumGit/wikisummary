import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.db.repository import ArticleRepository


class WikiParserService:
    def __init__(self, repo: ArticleRepository):
        self.repo = repo

    async def parse_article(self, url: str, parent_id=None, depth=0, max_depth=5):
        if depth > max_depth:
            return

        exists = await self.repo.get_by_url(url)
        if exists:
            return

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                html = await resp.text()

        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else url
        text = soup.get_text()

        article = await self.repo.create_article(url, title, text, parent_id)

        links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("/wiki/")]
        for href in set(links)[:10]:
            full_url = urljoin("https://en.wikipedia.org", href)
            await self.parse_article(full_url, parent_id=article.id, depth=depth + 1)

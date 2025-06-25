from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Article, Summary


class ArticleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_url(self, url: str):
        result = await self.session.execute(select(Article).where(Article.url == url))
        return result.scalars().first()

    async def create_article(self, url, title, content, parent_id=None):
        article = Article(url=url, title=title, content=content, parent_id=parent_id)
        self.session.add(article)
        await self.session.commit()
        return article


class SummaryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_article(self, article_id: int):
        return await self.session.get(Article, article_id)

    async def create_summary(self, article_id: int, content: str):
        summary = Summary(article_id=article_id, content=content)
        self.session.add(summary)
        await self.session.commit()
        return summary

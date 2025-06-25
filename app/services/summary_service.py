import openai
from app.db.repository import SummaryRepository
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY


class SummaryService:
    def __init__(self, repo: SummaryRepository):
        self.repo = repo

    async def generate_summary(self, article_id: int, content: str):
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize this Wikipedia article."},
                {"role": "user", "content": content[:4000]}
            ]
        )
        summary = response.choices[0].message.content
        return await self.repo.create_summary(article_id, summary)

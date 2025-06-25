from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import get_parser_service, get_summary_service
from app.services.parser_service import WikiParserService
from app.services.summary_service import SummaryService

router = APIRouter()


@router.post("/parse/")
async def parse_article(url: str, parser: WikiParserService = Depends(get_parser_service)):
    await parser.parse_article(url)
    return {"status": f"Parsing started for {url}"}


@router.post("/summary/")
async def get_summary(url: str,
                      parser: WikiParserService = Depends(get_parser_service),
                      summary_service: SummaryService = Depends(get_summary_service)):
    article = await parser.repo.get_by_url(url)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found. Please parse it first.")
    summary = await summary_service.generate_summary(article.id, article.content)
    return {"summary": summary.content}

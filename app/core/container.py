from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.repository import ArticleRepository, SummaryRepository
from app.services.parser_service import WikiParserService
from app.services.summary_service import SummaryService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.api.endpoints"])

    engine = providers.Singleton(create_async_engine, settings.DATABASE_URL, echo=True)
    session_factory = providers.Singleton(sessionmaker, bind=engine, class_=AsyncSession, expire_on_commit=False)

    article_repo = providers.Factory(ArticleRepository, session=session_factory)
    summary_repo = providers.Factory(SummaryRepository, session=session_factory)

    parser_service = providers.Factory(WikiParserService, repo=article_repo)
    summary_service = providers.Factory(SummaryService, repo=summary_repo)

from dependency_injector.wiring import Provide, inject
from app.core.container import Container
from app.services.parser_service import WikiParserService
from app.services.summary_service import SummaryService


@inject
def get_parser_service(parser: WikiParserService = Provide[Container.parser_service]):
    return parser


@inject
def get_summary_service(summary: SummaryService = Provide[Container.summary_service]):
    return summary

from fastapi.routing import APIRouter

from stats_collector.web.api import docs, monitoring, stats

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(stats.router, prefix="/stats", tags=["stats"])

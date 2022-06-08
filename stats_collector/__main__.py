import uvicorn

from stats_collector.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "stats_collector.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        factory=True,
    )


if __name__ == "__main__":
    main()

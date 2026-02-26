from fastapi import FastAPI
from app.api.routes import health,root
from config.settings import settings
from utils.logger import setup_logging

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title = settings.APP_NAME,
        version= settings.APP_VERSION,
        debug= settings.DEBUG
    )

    app.include_router(root.routor)
    app.include_router(health.routor)

    return app
app = create_app()

from fastapi import FastAPI
from api.routers import urls
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(urls.router, prefix="/api/v1/urls")

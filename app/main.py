from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from api.routers import urls
from core.config import settings
from db.session import async_sessionmaker, engine
from db.models import Base

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(urls.router, prefix="/api/v1/urls")

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await run_in_threadpool(create_tables)

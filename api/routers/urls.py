from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, HTTPException
from ..schemas import Url
from db.models import UrlModel
from db.session import get_db
from services.url_service import shorten_url, retrieve_url
from core.config import settings
import logging

router = APIRouter()

@router.post("/shorten/")
async def create_url(url: Url, db: AsyncSession = Depends(get_db)):
    logging.info(f"Creating shortened URL for {url.url}")
    alias = await shorten_url(str(url.url), db)
    return {"url": f"{settings.BASE_URL}/{alias}"}

@router.get("/{alias}")
async def get_url(alias: str, db: AsyncSession = Depends(get_db)):
    logging.info(f"Retrieving URL for alias {alias}")
    url = await retrieve_url(alias, db)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": url}

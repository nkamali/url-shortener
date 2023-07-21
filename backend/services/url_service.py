from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from db.models import UrlModel
from db.session import engine
from string import ascii_letters, digits
from random import choice


def generate_alias():
    return ''.join(choice(ascii_letters + digits) for _ in range(5))


async def shorten_url(url: str, db: AsyncSession) -> str:
    while True:
        alias = generate_alias()
        if not isinstance(url, str):
            url = url.url
        url_model = UrlModel(alias=alias, url=url)
        db.add(url_model)
        try:
            await db.commit()
            return alias
        except IntegrityError:
            await db.rollback()


async def retrieve_url(alias: str, db: AsyncSession) -> str:
    stmt = select(UrlModel.url).where(UrlModel.alias == alias)

    async with AsyncSession(engine) as session:
        result = await session.execute(stmt)
        url = result.scalars().first()

    return url if url else None

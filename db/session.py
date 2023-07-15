from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings

# asynchronous SQLAlchemy engine
engine = create_async_engine(settings.DATABASE_URL, future=True)

async_sessionmaker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Function to get a database session
async def get_db() -> AsyncSession:
    async with async_sessionmaker() as session:
        yield session

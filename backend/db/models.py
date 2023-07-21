import asyncio
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from db.session import get_db

Base = declarative_base()


class UrlModel(Base):
    __tablename__ = "urls"

    alias = Column(String(5), primary_key=True, index=True)
    url = Column(String(256), nullable=False)

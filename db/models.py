from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from db.session import engine
from db.types import PydanticUrl

Base = declarative_base()


class UrlModel(Base):
    __tablename__ = "urls"

    alias = Column(String(5), primary_key=True, index=True)
    url = Column(PydanticUrl, nullable=False)

Base.metadata.create_all(bind=engine)
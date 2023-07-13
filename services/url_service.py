from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from db.models import UrlModel
from string import ascii_letters, digits
from random import choice


def shorten_url(url: str, db: Session) -> str:
    # generate a random 5 character string as the alias
    alias = ''.join(choice(ascii_letters + digits) for _ in range(5))
    print("ALIAS", alias, type(alias))
    print("URL", url, type(url))
    url_model = UrlModel(alias=alias, url=url)
    db.add(url_model)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Alias already exists.")
    return alias


def retrieve_url(alias: str, db: Session) -> str:
    result = db.query(UrlModel.url).filter(UrlModel.alias == alias).first()
    return result[0] if result else None


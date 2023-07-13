from sqlalchemy import TypeDecorator, String
from pydantic import AnyUrl

class PydanticUrl(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is not None:
            return str(value)

    def process_result_value(self, value, dialect):
        if value is not None:
            return AnyUrl(value)

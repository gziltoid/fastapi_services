from pydantic import BaseModel


class Phone(BaseModel):
    number: str

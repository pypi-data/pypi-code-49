from pydantic import HttpUrl, Field
from pydantic.main import BaseModel


class BaseItemSchema(BaseModel):
    url: HttpUrl = Field(..., example="https://www.youtube.com/watch?v=bpA6fAz_r04")


class ItemSchemaIn(BaseItemSchema):
    pass


class ItemSchemaOut(BaseItemSchema):
    class Config:
        orm_mode = True
        extra = "ignore"

    artist: str = Field(..., example="Vic Dibitetto")
    duration: int = Field(..., example=94)
    id: int
    played: bool
    title: str = Field(..., example="Anybody want cawfee?!")

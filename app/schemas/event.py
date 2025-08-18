from pydantic import BaseModel
from datetime import date

class EventCreate(BaseModel):

    ruler_id: int
    title: str
    date: str
    description: str

class EventRead(BaseModel):
    id: int
    ruler_id: int
    title: str
    date: str
    description: str

    class Config:
        from_attributes = True
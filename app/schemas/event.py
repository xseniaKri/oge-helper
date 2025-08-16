from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    ruler_id: int
    date: date
    description: str
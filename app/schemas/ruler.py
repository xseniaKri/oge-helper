from pydantic import BaseModel

class RulerCreate(BaseModel):

    name: str
    years_of_reign: str

class RulerRead(BaseModel):
    id: int
    name: str
    years_of_reign: str | None

    class Config:
        from_attributes = True
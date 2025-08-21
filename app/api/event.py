from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.event import EventCreate, EventRead
from app import crud

router = APIRouter()

@router.post("/events", response_model=EventRead)
async def create_event(data: EventCreate, session: AsyncSession = Depends(get_db)):
    return await crud.event.create(session, data)

@router.get("/events/{ruler_id}", response_model=List[EventRead])
async def read_events(ruler_id: int, session: AsyncSession = Depends(get_db)):
    return await crud.event.read(session, ruler_id)


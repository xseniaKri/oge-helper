from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Sequence

from app.models.models import Event
from app.schemas.event import EventCreate

async def create(session: AsyncSession, data: EventCreate):
    event = Event(**data.model_dump())
    session.add(event)
    await session.commit()
    await session.refresh(event)
    return event

async def read(session: AsyncSession, ruler_id: int) -> Sequence[Event]:

    process = select(Event).where(Event.ruler_id == ruler_id)
    result = await session.execute(process)
    return result.scalars().all()
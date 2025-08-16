from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Sequence

from app.models.models import Ruler
from app.schemas.ruler import RulerCreate

async def create(session: AsyncSession, data: RulerCreate) -> int:
    ruler = Ruler(**data.model_dump())
    session.add(ruler)
    await session.commit()
    await session.refresh(ruler)
    return ruler

async def read(session: AsyncSession) -> Sequence[Ruler]:

    result = await session.execute(select(Ruler))
    return result.scalars().all()

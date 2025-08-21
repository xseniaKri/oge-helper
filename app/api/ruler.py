from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.ruler import RulerCreate, RulerRead
from app import crud

router = APIRouter()

@router.post("/rulers", response_model=RulerRead)
async def create_ruler(data: RulerCreate, session: AsyncSession = Depends(get_db)):
    return await crud.ruler.create(session, data)

@router.get("/rulers_see", response_model=List[RulerRead])
async def see_rulers(session: AsyncSession = Depends(get_db)):
    return await crud.ruler.read(session)

@router.get("/rulers/{ruler_id}", response_model=RulerRead)
async def see_ruler(ruler_id: int, session: AsyncSession = Depends(get_db)):
    return await crud.ruler.read_one(session, ruler_id)
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.ruler import RulerCreate, RulerRead
from app import crud

router = APIRouter()

@router.post("/rulers", response_model=RulerRead)
async def create_ruler(data: RulerCreate, session: AsyncSession = Depends(get_db)):
    return await crud.ruler.create(session, data)

from fastapi import APIRouter, Depends
from src.task_manager_api.schemas.user import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession

from src.task_manager_api.database import get_session
from src.task_manager_api.services.user import register_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=UserRead, status_code=201)
async def register(data: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await register_user(db, data.email, data.password)
    return user

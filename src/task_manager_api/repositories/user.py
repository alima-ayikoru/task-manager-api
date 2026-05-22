from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.task_manager_api.models import User


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalars_one_or_none()

    return user


async def create_user(session: AsyncSession, email: str, password_hash: str) -> User:
    user = User(email=email, password_hash=password_hash)
    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user

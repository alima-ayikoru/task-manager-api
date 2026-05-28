from src.task_manager_api.repositories.user import (
    get_user_by_email, 
    create_user,
)
from sqlalchemy.ext.asyncio import AsyncSession
from src.task_manager_api.utils import hash_password
from src.task_manager_api.exceptions.exceptions import (
    UserAlreadyExistsError,
    WeakPasswordError,
)


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        return False
    return True


async def register_user(session: AsyncSession, email: str, password: str):
    existing_user = await get_user_by_email(session, email)
    if existing_user:
        raise UserAlreadyExistsError(email)

    if not is_strong_password(password):
        raise WeakPasswordError()

    hashed_password = hash_password(password)
    user = await create_user(session, email, hashed_password)

    return user

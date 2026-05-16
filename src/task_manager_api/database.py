from sqlalchemy.orm import DeclarativeBase
from fastapi import Request


class Base(DeclarativeBase):
    pass


async def get_session(request: Request):
    async with request.app.state.session_factory() as session:
        yield session

import pytest
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from src.task_manager_api.database import Base, get_session
from src.task_manager_api.settings import settings
from src.task_manager_api.main import app
from httpx import ASGITransport, AsyncClient

engine = create_async_engine(settings.test_database_url, echo=True)
test_session_factory = async_sessionmaker(engine, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session():
    async with test_session_factory() as session:
        yield session
        await session.rollback()


@pytest.fixture
async def client(db_session: AsyncSession):
    async def override_get_session():
        yield db_session

    app.dependency_override[get_session] = override_get_session

    async with AsyncClient(
        # ASGITransport bypasses the network( uvicorn and port)
        # and directly calls the app, which is faster for testing
        transport=ASGITransport(app=app),
        # use a dummy base URL since ASGITransport
        # doesn't make real HTTP requests
        base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_override.clear()

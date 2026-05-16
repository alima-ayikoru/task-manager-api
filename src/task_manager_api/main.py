from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select, text
from src.task_manager_api.settings import settings
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Stating up the application...")
    engine = create_async_engine(settings.database_url, echo=True)

    try:
        async with engine.connect() as conn:
            # await conn.execute(select(1))
            await conn.execute(text("SELECT 1"))
            print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise ConnectionError("Failed to connect to the database") from e

    app.state.session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

    yield

    print("Shutting down the application...")
    await engine.dispose()

# Create the FastAPI application with the defined lifespan
app = FastAPI(lifespan=lifespan)

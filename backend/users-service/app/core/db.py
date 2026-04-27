from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings
from core.base import Base

DATABASE_URL = str(settings.db_url)

engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


async def create_table():
    async with engine.begin() as coon:
        await coon.run_sync(Base.metadata.create_all)

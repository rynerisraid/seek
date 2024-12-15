from app.settings.config import settings
from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.user import *

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
async_engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True, future = True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
# 获取异步会话
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
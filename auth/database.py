from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import JSON, TIMESTAMP, Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from models.user import role
from sqlalchemy.dialects.postgresql import ARRAY

from config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    bio = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    client = Column(Boolean, default=False)
    role_id = Column(ForeignKey(role.c.id))
    date = Column(String, default=None)
    descr = Column(String, nullable=True)
    listOfOrders = Column(ARRAY(Integer), nullable=True)
    rate = Column(Float, default=0.0)
    comments = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    activeBalance = Column(Float, default=0)
    frozenBalance = Column(Float, default=0)
    transactions = Column(String, nullable=True)
    userStatus = Column(String, nullable=True, default="Offline")
    activeTasks = Column(ARRAY(Integer), nullable=True)
    implementer = Column(Boolean, default=False)
    pendingTasks = Column(ARRAY(Integer), nullable=True)

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
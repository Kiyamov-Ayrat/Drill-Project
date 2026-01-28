from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends
from core.config import DATABASE_URL
from sqlalchemy.ext.asyncio import (create_async_engine,
                                    async_sessionmaker)


engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSession = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

# def create_db_and_tables():
#     Data.metadata.create_all(bind=engine)


async def get_async_session():
    async with AsyncSession() as session:
        yield session

# def get_session():
#     session = Session()
#     try:
#         yield session
#     finally:
#         session.close()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]
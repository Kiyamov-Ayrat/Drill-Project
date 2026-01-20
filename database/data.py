from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends
from core.config import DATABASE_URL
# from models.data import Data

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def create_db_and_tables():
#     Data.metadata.create_all(bind=engine)


def get_session():
    with Session() as session:
        yield session

# def get_session():
#     session = Session()
#     try:
#         yield session
#     finally:
#         session.close()

SessionDep = Annotated[Session, Depends(get_session)]
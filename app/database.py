from sqlalchemy import create_engine
import time
from sqlalchemy.ext.declarative import declarative_base
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import session, sessionmaker
import psycopg2
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#instead of using sqlalchemy we can use this
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connectiong to database failed")
#         print("Error: ", error)
#         time.sleep(2)
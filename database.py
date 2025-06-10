'''
Author: ChiaEnKang
Date: 2025-06-11 02:27:27
LastEditors: ChiaEnKang
LastEditTime: 2025-06-11 02:40:48
'''
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_db_url(
    db_user: str = "postgres",
    db_password: str = "postgres",
    db_host: str = "localhost",
    db_port: str = "5432",
    db_name: str = "fastapi_db",
    use_sqlite: bool = False
) -> URL:
    if use_sqlite:
        return URL.create("sqlite", database=f"{db_name}.db")
    return URL.create(
        "postgresql+pg8000",
        username=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )

# For testing with SQLite
SQLALCHEMY_DATABASE_URL = create_db_url(use_sqlite=True)
# For production with PostgreSQL
# SQLALCHEMY_DATABASE_URL = create_db_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

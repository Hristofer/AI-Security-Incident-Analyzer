from sqlalchemy.orm import Session

from app.database.database import SessionLocal


def get_database() -> Session:
    database = SessionLocal()

    try:
        return database
    finally:
        database.close()

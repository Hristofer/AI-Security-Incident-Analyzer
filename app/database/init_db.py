from app.database.database import Base
from app.database.database import engine

from app.database import models


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)

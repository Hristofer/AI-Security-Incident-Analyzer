from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    severity = Column(String(30), nullable=False)

    source = Column(String(100), nullable=False)

    ip_address = Column(String(50))

    mitre_technique = Column(String(50))

    description = Column(Text)

    ai_summary = Column(Text)

    resolved = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

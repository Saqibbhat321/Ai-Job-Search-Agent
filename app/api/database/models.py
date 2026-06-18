from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from app.database.db import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    company = Column(
        String(255),
        nullable=False
    )

    location = Column(
        String(255),
        nullable=True
    )

    skills = Column(
        Text,
        nullable=True
    )

    description = Column(
        Text,
        nullable=False
    )

    source = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
)
from datetime import datetime

from ...database import Base


class CompanyOUSModel(Base):
    __tablename__ = 'companies_ous'

    id = Column(Integer, primary_key=True)
    name = Column(String(190), unique=True, nullable=False)
    ticker = Column(String(20), nullable=True)
    exchange = Column(String(100), nullable=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

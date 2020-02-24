from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
    ForeignKey,
)
from datetime import datetime

from ...database import Base


class SubsidiaryAACTTrialMappingModel(Base):
    __tablename__ = 'subsidiary_aact_trial_mappings'

    id = Column(Integer, primary_key=True)
    nct_id = Column(String(128), nullable=False)
    subsidiary_id = Column(
        Integer,
        ForeignKey('subsidiaries.id'),
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    __table_args__ = (UniqueConstraint('nct_id', 'subsidiary_id'),)

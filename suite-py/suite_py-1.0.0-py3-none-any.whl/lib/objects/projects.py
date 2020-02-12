from __future__ import print_function, unicode_literals
from sqlalchemy import Column, Boolean, DateTime, String, BigInteger, func
from sqlalchemy.dialects.mysql import ENUM
from ..base import Base


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    status = Column(ENUM('unlocked', 'locked'), default='unlocked')
    updated_at = Column(DateTime, default=func.now())
    qa = Column(Boolean, default=False)

    def __repr__(self):
        return "{}".format(self.name)

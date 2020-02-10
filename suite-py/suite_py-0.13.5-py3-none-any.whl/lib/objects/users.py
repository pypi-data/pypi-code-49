from __future__ import print_function, unicode_literals
from sqlalchemy import Column, String, BigInteger
from ..base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    github_login = Column(String(32))
    name = Column(String(32))
    surname = Column(String(32))
    review_label = Column(String(64))

    def __repr__(self):
        return "{} - {} {}".format(self.github_login, self.name, self.surname, self.review_label)

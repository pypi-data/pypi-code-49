from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declared_attr


class FiorygiTransaction:
    __tablename__ = "fiorygitransactions"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)

    @declared_attr
    def change(self):
        return Column(Integer, nullable=False)

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("fiorygi.user_id"), nullable=False)

    @declared_attr
    def user(self):
        return relationship("Fiorygi", backref=backref("transactions"))

    @declared_attr
    def reason(self):
        return Column(String, nullable=False, default="")

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.change:+} to {self.user.username} for {self.reason}>"

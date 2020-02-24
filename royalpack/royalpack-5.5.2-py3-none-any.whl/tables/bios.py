from sqlalchemy import Column, \
                       Integer, \
                       Text, \
                       ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr


class Bio:
    __tablename__ = "bios"

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("users.uid"), primary_key=True)

    @declared_attr
    def user(self):
        return relationship("User", backref=backref("bio", uselist=False))

    @declared_attr
    def contents(self):
        return Column(Text, nullable=False, default="")

    def json(self) -> dict:
        return {
            "contents": self.contents
        }

    def __repr__(self):
        return f"<Bio of {self.user}>"

    def __str__(self):
        return self.contents

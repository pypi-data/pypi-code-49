from sqlalchemy import Column, \
                       Integer, \
                       ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr


class TriviaScore:
    __tablename__ = "triviascores"

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("users.uid"), primary_key=True)

    @declared_attr
    def user(self):
        return relationship("User", backref=backref("trivia_score", uselist=False))

    @declared_attr
    def correct_answers(self):
        return Column(Integer, nullable=False, default=0)

    @declared_attr
    def wrong_answers(self):
        return Column(Integer, nullable=False, default=0)

    @property
    def total_answers(self):
        return self.correct_answers + self.wrong_answers

    @property
    def offset(self):
        return self.correct_answers - self.wrong_answers

    @property
    def correct_rate(self):
        if self.total_answers == 0:
            return 0.0
        return self.correct_answers / self.total_answers

    @property
    def score(self) -> float:
        return (self.correct_answers + self.correct_answers * self.correct_rate) * 10

    def __repr__(self):
        return f"<TriviaScore of {self.user}: ({self.correct_answers}|{self.wrong_answers})>"

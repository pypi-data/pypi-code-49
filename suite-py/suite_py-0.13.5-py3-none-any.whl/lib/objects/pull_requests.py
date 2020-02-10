from __future__ import print_function, unicode_literals
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.mysql import ENUM, BIGINT
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class PullRequests(Base):
    __tablename__ = 'pull_requests'

    youtrack_id = Column(String(50), primary_key=True)
    github_id = Column(
        BIGINT(display_width=20, unsigned=True), primary_key=True)
    project_id = Column(BIGINT(display_width=20, unsigned=True),
                        ForeignKey('projects.id'), primary_key=True)
    user_id = Column(BIGINT(display_width=20, unsigned=True),
                     ForeignKey('users.id'))
    status = Column(ENUM('In Progress', 'Review', 'QA',
                         'Ready to deploy', 'On staging', 'Done'))
    updated_at = Column(DateTime, default=func.now())
    title = Column(String(64))

    user = relationship("Users", backref="pr")
    project = relationship("Projects", backref="pr")

    def __repr__(self):
        return "issue: {}\n pull request: {}\n project: {}\n title: {}\n".format(self.youtrack_id, self.github_id, self.project.name, self.title)

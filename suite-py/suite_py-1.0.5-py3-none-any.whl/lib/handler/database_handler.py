from __future__ import print_function, unicode_literals
import os
import subprocess
import sys
from ..tokens import Tokens
from ..singleton import Singleton
from ..config import Config
from ..objects.projects import Projects
from ..objects.pull_requests import PullRequests
from ..objects.users import Users
import sqlalchemy as db

tokens = Tokens()
config = Config().load()


class DatabaseHandler(metaclass=Singleton):
    _connection = None
    _session = None

    def __init__(self):
        connection_string = 'mysql://suite_py:{}@db-prima-aurora-production.prima.it/suite_py'.format(
            tokens.mysql)

        engine = db.create_engine(
            connection_string, isolation_level='READ COMMITTED')

        self._connection = engine.connect()
        Session = db.orm.sessionmaker(bind=engine)
        self._session = Session()

    # Users
    def get_current_user(self):
        return self._session.query(Users).filter_by(github_login=config['user']['github_login']).one()

    def list_other_users(self, current_user):
        return self._session.query(Users).filter(Users.id != current_user.id).order_by(Users.github_login).all()

    def get_user_by_github_login(self, login):
        return self._session.query(Users).filter_by(github_login=login).one()

    def get_all_users(self):
        return self._session.query(Users).all()

    def insert_user(self, github_login, name, surname, review_label):
        self._session.add(Users(github_login=github_login,
                                name=name, surname=surname, review_label=review_label))
        self._session.commit()

    # Projects
    def get_project_by_name(self, name):
        return self._session.query(Projects).filter_by(name=name).one()

    def get_projects_by_status(self, status):
        return self._session.query(Projects).filter_by(status=status).order_by(Projects.name).all()

    def get_all_projects(self):
        return self._session.query(Projects).order_by(Projects.name).all()

    def lock_project(self, project):
        if(project.status == 'unlocked'):
            project.status = 'locked'
            self._session.commit()
        else:
            raise Exception("Il progetto risulta gia' bloccato!")

    def unlock_project(self, project):
        project.status = 'unlocked'
        self._session.commit()

    # PullRequests
    def create_pr(self, youtrack_id, github_id, project_id, user_id, title, status='In Progress'):
        self._session.add(PullRequests(youtrack_id=youtrack_id, github_id=github_id,
                                       project_id=project_id, user_id=user_id, status=status, title=title))
        self._session.commit()

    def get_all_owned_prs(self, user):
        return self._session.query(PullRequests).filter_by(user_id=user.id).all()

    def get_all_owned_prs_by_status(self, user, statuses):
        return self._session.query(PullRequests).filter(PullRequests.user_id == user.id, PullRequests.status.in_(statuses)).all()

    def get_all_project_prs(self, project_id):
        return self._session.query(PullRequests).filter(PullRequests.project_id == project_id).all()

    def update_pr_state(self, pull_request, status):
        pull_request.status = status
        self._session.commit()

    def get_all_owned_prs_with_qa(self, user, statuses):
        return self._session.query(PullRequests).join(Projects).filter(PullRequests.user == user, Projects.qa == True, PullRequests.status.in_(statuses)).all()

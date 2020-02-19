from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from werkzeug.security import generate_password_hash, check_password_hash


class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///data.db', echo=False)
        self.Base = declarative_base()
    
    def create_all(self):
        self.Base.metadata.create_all(self.engine)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


database = Database()


class User(database.Base):
    """
    The User model
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    admin = Column(Boolean)

    def __init__(self, username, password):
        """Initialises a new user"""
        self.username = username
        self.set_password(password)
        self.admin = False
    
    def make_admin(self):
        self.admin = True
    
    def remove_admin(self):
        self.admin = False
    
    def set_password(self, password):
        """Sets the users password hash to the hash of a given password"""
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        """Compares a given password to the stored password hash"""
        return check_password_hash(self.password_hash, password)

database.create_all()
database.create_session()


def create_user(username, password):
    user = User(username, password)
    database.session.add(user)
    database.session.commit()
    return user


def find_user(username):
    return database.session.query(User).filter(User.username == username)

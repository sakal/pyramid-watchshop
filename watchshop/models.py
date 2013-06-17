import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import (
    MultipleResultsFound,
    NoResultFound,
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    and_,
    ForeignKey,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    login = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(64))
    enabled = Column(Boolean, default=True)

    def __init__(self, login, email, password, enabled):
        self.login = login
        self.email = email
        self.password = password
        self.enabled = enabled

    def __repr__(self):
        return "<User('{user_id:d}', '{login:s}', '{email:s}', '{password:s}', '{enabled:t}')>"\
            .format(user_id=self.user_id, login=self.login, email=self.email,
                password=self.password, enabled=self.enabled)





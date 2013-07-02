import logging

from hashlib import sha256 as hash_method
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

from watchshop.models import (
    Base,
    DBSession,
)

UserModel = None

class BaseUser(Base):
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

UserModel = BaseUser


class UserHelper(object):
    def __init__(self, config):
        self.config = config
        self.log = logging.getLogger(__name__)
        self._auth_attr = self.auth_attribute()

        self.user_id = None
        self.login = None
        self.auth_login = None
        self.enabled = None
        self.email = None
        self.account = None


    def auth_attribute(self, attribute_name=None):
        try:
            name = self.config['auth_login_field']
        except KeyError:
            name = 'login'
        if hasattr(UserModel, name):
            return name
        raise KeyError("UserModel has not attribute '{0}'"
            " as auth_login_field. Check config".format(name))

    def hash_value(self, value, solt=None):
        """Return hash of (value + solt)
        Get solt from method argument or from config['db_solt']"""
        default_solt = 'solt1'
        if not solt:
            try:
                solf = self.config.get('db_solt')
            except KeyError:
                solt = default_solt
                self.log.warning('Using default solt. Immediately add "db_solt = string_value" to config')

        hash_object = hash_method()
        hash_object.update("{0}{1}".format(value, solt))
        return hash_object.hexdigest()

    def attempt_authorize(self, login, password):
        hashed_password = self.hash_value(password)
        try:
            user = DBSession.query(UserModel).filter(
                and_(
                    getattr(UserModel, self._login_attr) == login,
                    UserModel.password == hashed_password
                ),

            )
            self.user_id = user.user_id
            self.login = self.login
            self.auth_login = getattr(user, self._auth_attr)
            self.email = user.email
            self.enabled = user.enabled
            return True
        except (MultipleResultsFound, NoResultFound):
            self.log.debug("User was not found")
        except DBAPIError, e:
            self.log.error("Catch DB API Error")
            self.log.debug("DB API Error: {0}".format(e))
        return False




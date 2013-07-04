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



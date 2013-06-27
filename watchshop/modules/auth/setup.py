import logging
from .model import UserModel
from watchshop.models import (
    DBSession,
    
)

def install():
    user = UserModel('admin', 'admin@example.com', 'admin', True)
    DBSession.add(user)

def uninstall():
    pass

def backup():
    pass

def recovery():
    pass

import logging
from .model import user_model
from ...models import (
    DBSession,
    
)

def install():
    user = user_model('admin', 'admin@example.com', 'admin', True)

def uninstall():
    pass

def backup():
    pass

def recovery():
    pass

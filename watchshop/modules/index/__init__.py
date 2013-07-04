import logging
from .contexts import (
    Index,
)

ROUTE_PREFIX = None

def includeme(config):

    config.add_route('index', '/', factory=Index)



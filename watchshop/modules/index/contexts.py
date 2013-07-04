from pyramid.security import (
    Everyone,
    Allow,
    Deny,
    Authenticated,
    ALL_PERMISSIONS,
)


class Index(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        pass



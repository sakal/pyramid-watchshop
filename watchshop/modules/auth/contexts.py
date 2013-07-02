from pyramid.security import (
    Everyone,
    Allow,
    Deny,
    Authenticated,
    ALL_PERMISSIONS,
)


class Auth(object):
    __acl__ = [
        (Allow, Everyone, 'login'),
        (Allow, Authenticated, 'logout'),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        pass



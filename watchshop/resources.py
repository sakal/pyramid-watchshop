from pyramid.security import (
    Everyone,
    Allow,
    Deny,
    Authenticated,
    ALL_PERMISSIONS
)


class RootFactory(object):
    def __init__(self, request):
        pass


class AnonymPerm(object):
    __acl__ = [
        (Allow, Everyone, ALL_PERMISSIONS),
    ]

class AuthPerm(object):
    __acl__ = [
        (Allow, Authenticated, ALL_PERMISSIONS),
        (Deny, Everyone, ALL_PERMISSIONS)
    ]
    def __init__(self, request):
        pass

class CabinetPerm(object):
    __acl__ = [
        (Allow, Everyone, 'login'),
        (Allow, Authenticated, 'logout'),
        (Deny, Everyone, ALL_PERMISSIONS)
    ]

    def __init__(self, request):
        pass

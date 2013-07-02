import logging
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .model import UserModel
from .contexts import (
    Auth,
)

ROUTE_PREFIX = '/auth'

def includeme(config):
    authn_policy = SessionAuthenticationPolicy()
    authz_policy = ACLAuthorizationPolicy()

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_route('login', '/login', factory=Auth)
    config.add_route('logout', '/logout', factory=Auth)



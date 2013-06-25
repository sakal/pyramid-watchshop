import logging
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .model import BaseUser

ROUTE_PREFIX = '/auth'

def includeme(config):
    authn_policy = SessionAuthenticationPolicy()
    authz_policy = ACLAuthorizationPolicy()

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)


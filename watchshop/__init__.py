from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_jinja2 import renderer_factory
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'watchshop')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authn_policy = SessionAuthenticationPolicy()
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings)

    config.add_translation_dirs('locale/')
    config.include('pyramid_redis_sessions')
    config.include('pyramid_jinja2')

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_static_view('static', 'static')
    config.add_view('watchshop.views.my_view',
                    context='watchshop.resources.AnonymPerm',
                    renderer="mytemplate.jinja2")

    return config.make_wsgi_app()

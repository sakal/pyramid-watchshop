from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )
from .modules import load_modules

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

    config = Configurator(settings=settings)

    config.add_translation_dirs('locale/')
    config.include('pyramid_redis_sessions')
    config.include('pyramid_jinja2')
    # load modules from subdirectories in ./modules/
    load_modules(config)

    config.add_static_view('static', 'static')
    config.scan(ignore='{0}.modules'.format(__name__))
    # config.add_view('watchshop.views.my_view',
    #                context='watchshop.resources.AnonymPerm',
    #                renderer="mytemplate.jinja2")

    return config.make_wsgi_app()

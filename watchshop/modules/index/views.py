import colander
from deform import (
    Form,
    ValidationFailure,
    widget,
)
from pyramid.renderers import (
    render_to_response,
)
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
#from .model import (
#    UserHelper,
#)


class IndexView(object):
    def __init__(self, request):
        self.request = request
        #self.user_helper = UserHelper(request.registry.settings)

    def __call__(self):
        return {}

    @view_config(route_name='index', request_method='GET',
        renderer='templates/index.jinja2', permission='view')
    def index(self):
        """Just show login form
        
        @todo add request_from hidden value
        @todo add csrf hidden value"""
        return {}


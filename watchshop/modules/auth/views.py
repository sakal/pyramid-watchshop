import colander
from deform import (
    Form,
    ValidationFailure,
    widget,
)
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .model import (
    UserHelper,
)


class AuthSchema(colander.MappingSchema):
    login = colander.SchemaNode(
            colander.String(),
            title="Login",
            )
    password = colander.SchemaNode(
            colander.String(),
            #title="Password",
            widget=widget.CheckedPasswordWidget(size=30),
            )

class AuthView(object):
    def __init__(self, request):
        self.request = request
        self.user_helper = UserHelper(request.registry.settings)

    def __call__(self):
        return {}

    @view_config(route_name='login', request_method='GET',
        renderer='templates/auth_form.jinja2')
    def login_form_show(self):
        """Just show login form
        
        @todo add request_from hidden value
        @todo add csrf hidden value"""
        schema = AuthSchema()
        form = Form(schema, buttons=('submit',))
        return {'form': form.render()}

    @view_config(route_name='login', request_method='POST')
    def login_form_process(self):
        """Process login form.
        Render form if attempt_authorize was failed
        and redirect to root '/' of site.
        Return form in 'form' key.
        
        @todo redirect to request_from url
        @todo process csrf value"""
        schema = AuthSchema()
        form = Form(schema, buttons=('submit',))
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()
            values = None
            try:
                appstruct = form.validate(controls)
            except ValidationFailure, e:
                return {'form': e.render()}

            # make here call of attempt_login
            if self.user_helper.attempt_authorize(
                appstruct['login'],
                appstruct['password']):
                remember(self.request, appsctruct['login'])
                return HTTPFound("/")
            else:
                return {'form':form.render(appstruct=appstruct)}

            return HTTPFound('/')
        return {'form': form.render()}

    @view_config(route_name='logout', request_method='GET', permission='logout')
    def logout(self):
        """Logout authorized user and redirect him to site root '/'"""
        headers = forget(self.request)
        return HTTPFound('/', headers=headers)


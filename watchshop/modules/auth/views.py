import colander
from deform import (
    Form,
    ValidationFailure,
    widget,
)
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


class AuthSchema(colander.MappingSchema):
    login = colander.SchemaNode(
            colander.String(),
            title="Login",
            )
    password = colander.SchemaNode(
            colander.String(),
            title="Password",
            widget=widget.CheckedPasswordWidget(size=30),
            )

class AuthView(object):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        return {}

    @view_config(route_name='login', request_method='GET')
    def login_form_show(self):
        schema = AuthSchema()
        form = Form(schema, buttons=('submit',))
        return {'form': form.render()}

    @view_config(route_name='login', request_method='POST')
    def login_form_process(self):
        schema = AuthSchema()
        form = Form(schema, buttons=('submit',))
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()
            try:
                form.validate(controls)
            except ValidationFailure, e:
                return {'form': e.render()}

            # make here call of attempt_login

            return HTTPFound('/')
        return {'form': form.render()}

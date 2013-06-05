from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('watchshop')

def my_view(request):
    return {'project':'watchshop'}

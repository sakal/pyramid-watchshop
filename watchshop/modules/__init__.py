import logging
from os import listdir
from os.path import (
    isdir,
    realpath,
    dirname,
    join,
)
from pyramid.path import DottedNameResolver
from pyramid.exceptions import ConfigurationError


log = logging.getLogger()

modules_directory = realpath(dirname(__file__))
# get 'watchshop' from 'watchshop.modules'
package_name = __name__.split('.')[0]
modules_path = ''.join(__name__.split('.')[1:])


def list_modules():
    """Return generator with list of modules.
    Search modules in subdirctories"""
    for module_name in listdir(modules_directory):
        if isdir(join(modules_directory, module_name)):
            log.debug('Load module: {0}'.format(module_name))
            yield module_name

def _load_module(config, package, module):
    try:
        resolver = DottedNameResolver()
        # log.debug('{0}.{1}'.format(package, module))
        prefix = resolver.resolve('{0}.{1}:ROUTE_PREFIX'.format(package, module))

    except ImportError, e:
        prefix = None

    try:
        config.include(
            "{package}:{module}".format(package=package, module=module),
            route_prefix="/{prefix}".format(prefix=prefix)
        )
    except ConfigurationError, e:
        log.error(e)
    except ImportError, e:
        log.error(e)
    except AttributeError, e:
        log.error(e)

def load_modules(config):
    for module_name in list_modules():
        _load_module(config, package_name, '.'.join([modules_path, module_name]))

def setup_modules():
    pass


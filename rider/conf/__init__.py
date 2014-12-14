BASE_DIR = ''
BASE_URL = ''


#TODO RETHINK
MAIN_SERVER = 'rider.core.server.MultiServer'
WSGI_SERVER = 'rider.wsgi.server.MultiWsgiServer'
TASK_SERVER = 'rider.tasks.server.MultiTaskServer'

SERVERS = (
    (WSGI_SERVER, [], {}),
    (TASK_SERVER, [], {}),
)
#

class ConfigurationError(Exception):
    pass


def configure(source, target=''):
    """
    configure
    """
    from types import ModuleType
    # from rider.utils import import_object

    if type(source) == str:
        source = __import__(source)

    if isinstance(source, dict):
        source_iterator = source.iteritems()
        if not target:
            raise ConfigurationError()
    elif isinstance(source, ModuleType):
        if not target:
            target = source.__name__.split('.')[-1]
        if target not in globals():
            globals()[target] = source
            return
        source_iterator = [(attr, getattr(source, attr)) for attr in dir(source) if not attr.startswith('__')]
    else:
        raise ConfigurationError()

    if target not in globals():
        globals()[target] = {}

    if isinstance(globals()[target], dict):
        for attr, value in source_iterator:
            globals()[target][attr] = value
    elif isinstance(globals()[target], ModuleType):
        for attr, value in source_iterator:
            setattr(globals()[target], attr, value)

configure(__import__('rider.conf.templates'))
configure(__import__('rider.conf.tasks'))
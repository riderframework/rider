import templates

BASE_DIR = ''
BASE_URL = ''
SERVERS = (
    'rider.wsgi.server.WsgiServer',
    'rider.tasks.server.TaskServer',
)


class ConfigurationError(Exception):
    pass


def configure(source, target=''):
    """
    configure
    """
    from types import ModuleType
    if isinstance(source, dict):
        source_iterator = source.iteritems()
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

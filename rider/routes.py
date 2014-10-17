import falcon

from rider.views import View
from rider.utils import import_module, import_object


application = falcon.API()

#TODO do more robust
BASE_URL = []


def include_routes(url, module, namespace=''):
    BASE_URL.append(url)
    import_module(module)
    del BASE_URL[-1]


def route(url, view=None, name=''):
    #decorator wrapper
    if not view:
        def route_wrapper(cls):
            route(url, view=cls, name=name)
            return cls
        return route_wrapper

    if type(view) == str:
        view = import_object(view)
    try:
        if not issubclass(view, View):
            # TODO explanation
            raise Exception()
    except TypeError:
        # TODO explanation
        raise Exception()
    application.add_route('%s%s' % (''.join(BASE_URL), url), view())

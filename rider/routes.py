import falcon
from rider.views import View
from rider.utils import import_module, import_object


application = falcon.API()


base_url = []


def include_routes(url, module, namespace=''):
    base_url.append(url)
    import_module(module)
    del base_url[-1]


def route(url, view, name=''):
    if type(view) == str:
        view = import_object(view)
    try:
        if not issubclass(view, View):
            #TODO explanation
            raise Exception()
    except TypeError:
        #TODO explanation
        raise Exception()
    application.add_route('%s%s' % (''.join(base_url), url), view())


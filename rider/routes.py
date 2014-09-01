import falcon
from rider.views import View
from rider.utils import import_object
application = falcon.API()


base_url = []


def include(module, namespace=''):
    def route_include():
        __import__(module, globals(), locals(), [], 0)
    return route_include


def route(url, uni_view, name=''):
    #TODO rethink and refactorize
    if callable(uni_view) and uni_view.__name__ == 'route_include':
        base_url.append(url)
        uni_view()
        del base_url[-1]
        return

    if type(uni_view) == str:
        uni_view = import_object(uni_view)

    try:
        if not issubclass(uni_view, View):
            #TODO explanation
            raise Exception()
    except TypeError:
        #TODO explanation
        raise Exception()
    application.add_route('%s%s' % (''.join(base_url), url), uni_view())


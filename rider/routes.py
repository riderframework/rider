import falcon
from rider.views import View

application = falcon.API()


base_url = []


def include(module, namespace=''):
    def route_include():
        __import__(module, globals(), locals(), [], 0)
    return route_include


def route(url, inp, name=''):
    if callable(inp) and inp.__name__ == 'route_include':
        base_url.append(url)
        inp()
        del base_url[-1]
        return

    if type(inp) == str:
        mod_dot = inp.split('.')
        module_name = '.'.join(mod_dot[0:-1])
        view_name = mod_dot[-1]
        module = __import__(module_name, globals(), locals(), [], 0)
        view = getattr(module, view_name)()
    else:
        try:
            if issubclass(inp, View):
                view = inp()
            else:
                #TODO explanation
                raise Exception()
        except TypeError:
            #TODO explanation
            raise Exception()
    application.add_route('%s%s' % (''.join(base_url), url), view)


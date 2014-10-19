import falcon

from rider.views import View, ViewSet

from rider.utils import import_module, import_object
from types import ModuleType

application = falcon.API()

#TODO do more robust
BASE_URL = []


def include_routes(url, viewset_or_module, namespace=''):
    BASE_URL.append(url)
    try:
        viewset = import_object(viewset_or_module)
        try:
            if issubclass(viewset, ViewSet):
                for subview in viewset().get_views():
                    route('', subview)
            else:
                #TODO revise text
                raise Exception('bad class')
        except TypeError:
            #TODO revise text
            raise Exception('not class')
    except AttributeError:
        #ordinary module
        import_module(viewset_or_module)
    del BASE_URL[-1]


def route(url, view=None, name='', is_method=False):
    #decorator wrapper
    if not view:
        def route_wrapper(cls):
            cls.add_url(url, name)
            return cls
        return route_wrapper

    if isinstance(view, str):
        view = import_object(view)
    try:
        if issubclass(view, View):
            if url:
                application.add_route('%s%s' % (''.join(BASE_URL), url), view())
            for cls_url, cls_url_name in view.get_urls():
                application.add_route('%s%s' % (''.join(BASE_URL), cls_url), view())
        else:
            #TODO revise text
            raise Exception('bad class')
    except TypeError as e:
        #TODO revise text
        raise Exception('not class: %s' % e)


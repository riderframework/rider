'''
Route lib
'''
from rider.utils import import_module, import_object
from rider.views import View, ViewSet
from rider.routes.urls import push_url, nest_url, pop_url


def include_routes(url, viewset_or_module, namespace=''):
    push_url(url)
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
    pop_url()


def route(url, view=None, name=''):
    if not view:
        #decorator wrapper
        def route_wrapper(cls):
            cls.add_url(url, name)
            return cls
        return route_wrapper

    if isinstance(view, str):
        view = import_object(view)
    try:
        if issubclass(view, View):
            if url:
                nest_url(url, view)
            for cls_url, cls_url_name in view.get_urls():
                if cls_url:
                    nest_url(cls_url, view)
        else:
            #TODO revise text
            raise Exception('bad class')
    except TypeError as e:
        #TODO revise text
        raise Exception('not class: %s' % e)


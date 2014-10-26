'''
Route lib
'''
from rider.utils import import_module, import_object
from rider.routes.urls import push_url, nest_url, pop_url, url


def include_routes(url, viewset_or_module, namespace=''):
    push_url(url, namespace)
    try:
        viewset = import_object(viewset_or_module)
    except AttributeError:
        import_module(viewset_or_module)
    else:
        for subview in viewset().get_views():
            route('', subview)
    pop_url(namespace)


def route(url, view=None, name=''):
    if not view:
        #decorator wrapper
        def route_wrapper(cls):
            cls.add_url(url, name)
            return cls
        return route_wrapper

    if isinstance(view, str):
        view = import_object(view)

    if url:
        nest_url(url, view, name)
    for cls_url, cls_url_name in view.get_urls():
        if cls_url:
            nest_url(cls_url, view, cls_url_name)


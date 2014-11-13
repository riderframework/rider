"""
Route lib
"""
from importlib import import_module
from rider.utils import import_object
from rider.routes.urls import UrlNest


__all__ = ('include_routes', 'route', 'url')


def include_routes(url_pattern, viewset_or_module, namespace=''):
    """
    nests urls from viewset or module *viewset_or_module* into *namespace*.
    Nested urls can be linked with 'namespace:nested_url' (it can be used in function **url**).

    For example:
        include_routes('/contact/', 'project.contact.routes', namespace='contact')
    """
    with UrlNest(url_pattern, namespace):
        try:
            viewset = import_object(viewset_or_module)
        except AttributeError:
            import_module(viewset_or_module)
        else:
            for subview in viewset().get_views():
                route('', subview)


def route(url_pattern, view=None, name=''):
    """
    routes *url* direct to *view* and names it with *name*.
    Argument *view* may be instance of View class or string.
    If string is used it will be interpreted as module path pointing to View class.

    :param url_pattern: Url or url pattern
    :param view: View class
    :param name: Name of the specified url
    For example:
        route('url_to', 'project.views.MyView')

    Function can be also used as decorator of view:
        @route('/url_to_view', name='some_view')
        class SomeView(HtmlView):
            ...
    """
    if not view:
        #decorator wrapper
        def route_wrapper(cls):
            cls.add_url(url_pattern, name)
            return cls
        return route_wrapper

    if isinstance(view, str):  # TODO or unicode?
        view = import_object(view)

    if url_pattern:
        UrlNest.add_url(url_pattern, view, name)
    for cls_url, cls_url_name in view.get_urls():
        if cls_url:
            UrlNest.add_url(cls_url, view, cls_url_name)


def url(name):
    """
    :param name: Name of url which has got by **route** function"
    :return: Url
    """
    return UrlNest.get_url(name)

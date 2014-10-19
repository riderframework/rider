import falcon
import json
from functools import wraps, partial
from rider.exceptions import HttpException
from rider.response import ResponseSetter

__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView', 'view')


class View(ResponseSetter):
    '''
    Wrapper around falcon view api
    '''
    exceptions_mimic = True
    urls = {}

    @classmethod
    def get_urls(cls):
        return cls.urls.get(cls, [])

    @classmethod
    def add_url(cls, url, name):
        cls.urls.setdefault(cls, []).append((url, name))

    def __init__(self):
        super(View, self).__init__()
        for http_method in falcon.HTTP_METHODS:
            method_name = http_method.lower()
            try:
                setattr(
                    self,
                    'on_%s' % method_name,
                    self._wrap_response(
                        getattr(self, method_name)
                    )
                )
            except AttributeError as e:
                pass

    def _wrap_response(self, method):
        @wraps(method)
        def wrapper(request, response, *args, **kwargs):
            try:
                self.content = method(request, *args, **kwargs)
            except HttpException as e:
                if self.exceptions_mimic:
                    e.content_type = self.content_type
                    e.content_wrapper = self.content_wrapper
                e.set_response(response)
            else:
                self.set_response(response)
        return wrapper


class DataView(View):
    '''
    Basic binary data view
    '''
    response_type = 'data'


class StreamView(View):
    '''
    Basic stream view
    '''
    response_type = 'stream'
    exceptions_mimic = False


class TextView(View):
    '''
    Basic text view
    '''
    response_type = 'body'


class HtmlView(TextView):
    '''
    text/html view
    '''
    content_type = 'text/html'


class JsonView(TextView):
    '''
    application/json view
    '''
    content_type = 'application/json'
    content_wrapper = json.dumps


class view(object):
    def __init__(wrapper, view_class, http_method='GET'):
        wrapper.view_class = view_class
        if isinstance(http_method, str):
            wrapper.http_methods = [http_method]
        elif isinstance(http_method, list):
            wrapper.http_methods = http_method
        else:
            #TODO revise text
            raise Exception('http method definition must be string or list')

    def __call__(wrapper, func):
        class FunctionView(wrapper.view_class):
            viewset = None
            def __init__(instance):
                for http_method in wrapper.http_methods:
                    if http_method not in falcon.HTTP_METHODS:
                        raise Exception('%s is not in %s' (http_method, falcon.HTTP_METHODS))
                    method_name = http_method.lower()
                    setattr(instance, method_name, wraps(func)(partial(func, instance)) if instance.viewset else func)
                super(FunctionView, instance).__init__()
        return FunctionView


class ViewSet(object):
    def get_views(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr):
                try:
                    if issubclass(attr, View):
                        attr.viewset = self
                        yield attr
                except TypeError:
                    #not class
                    continue

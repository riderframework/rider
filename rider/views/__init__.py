import json

from functools import wraps

from rider.core import HTTP_METHODS

from rider.views.decorators import ViewDecorator
from rider.views.exceptions import HttpException
from rider.views.response import ResponseSetter

__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView', 'ViewSet')


class View(ViewDecorator, ResponseSetter):
    '''
    Wrapper around falcon view api
    '''
    same_exception_content = True
    urls = {}

    @classmethod
    def get_urls(cls):
        return cls.urls.get(cls, [])

    @classmethod
    def add_url(cls, url, name):
        cls.urls.setdefault(cls, []).append((url, name))

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        for http_method in HTTP_METHODS:
            method_name = http_method.lower()
            try:
                setattr(
                    self,
                    'on_%s' % method_name,
                    self._wrap_response(
                        getattr(self, method_name)
                    )
                )
            except AttributeError:
                pass

    def _wrap_response(self, method):
        @wraps(method)
        def wrapper(request, response, *args, **kwargs):
            try:
                self.content = method(request, *args, **kwargs)
            except HttpException as e:
                if self.same_exception_content:
                    e.content_type = self.content_type
                    e.content_wrapper = self.content_wrapper
                e.set_response(response)
            else:
                self.set_response(response)
        return wrapper


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
    same_exception_content = False


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






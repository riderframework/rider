import json

from functools import wraps

from rider.http import HTTP_METHODS

from rider.routes.urls import UrlHolder

from rider.views.decorators import ViewDecorator
from rider.views.exceptions import HttpException
from rider.views.response import ResponseSetter


__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView', 'ViewSet')


class TextView(ViewDecorator, ResponseSetter, UrlHolder):
    """
    Basic wrapper around falcon view api.
    It provide support for plaint text output.
    """
    same_exception_content = True

    def __init__(self, *args, **kwargs):
        super(TextView, self).__init__(*args, **kwargs)
        #support for viewset
        self.viewset = None
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
    """
    Package of multiple views and theirs urls.
    """
    def get_views(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr):
                try:
                    if issubclass(attr, TextView):
                        #set "viewset" attribut of View instance
                        attr.viewset = self
                        yield attr
                except TypeError:
                    #not class
                    continue


class DataView(TextView):
    """
    Basic binary data view
    """
    response_type = 'data'
    encoding = None


class StreamView(TextView):
    """
    Basic stream view
    """
    response_type = 'stream'
    same_exception_content = False
    encoding = None


class HtmlView(TextView):
    """
    text/html view
    """
    content_type = 'text/html'


class JsonView(TextView):
    """
    application/json view
    """
    content_type = 'application/json'
    content_wrapper = json.dumps

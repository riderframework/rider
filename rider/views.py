import falcon
import json
from functools import wraps
from rider.exceptions import HttpException
from rider.response import ResponseSetter

__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView', 'view')


class View(ResponseSetter):
    '''
    Wrapper around falcon view api
    '''
    def __init__(self):
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
            except AttributeError:
                pass

    def _wrap_response(self, method):
        @wraps(method)
        def wrapper(request, response, *args, **kwargs):
            try:
                self.content = method(request, *args, **kwargs)
            except HttpException as e:
                e.content_type = self.content_type
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

    def get_content(self):
        # TODO inheritance dont work with property
        return json.dumps(super(TextView, self).get_content())


def view(ViewClass):
    '''
    decorator providing support for functional views
    '''
    def wrapper(func):
        class FunctionView(ViewClass):
            def __init__(self):
                for http_method in falcon.HTTP_METHODS:
                    method_name = http_method.lower()
                    setattr(self, method_name, func)
                super(FunctionView, self).__init__()
        return FunctionView
    return wrapper

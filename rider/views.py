import falcon
import json
import six
from functools import wraps
from rider.exceptions import HttpException

__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView', 'view')


class View(object):
    '''
    Wrapper around falcon view api
    '''
    content_type = 'text/plain'

    def __init__(self):
        for http_method in falcon.HTTP_METHODS:
            method_name = http_method.lower()
            try:
                setattr(self,
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
                #TODO require return value from method
                setattr(response, self.response_type, method(request, *args, **kwargs))
            except HttpException as e:
                response.content_type = self.__class__.content_type
                e.set_response(response)
            else:
                response.status = falcon.HTTP_200
                response.content_type = self.content_type
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

    def _wrap_response(self, method):
        if hasattr(self, 'convert'):
            convert_method = six.get_unbound_function(self.convert)
            @wraps(method)
            def wrapper(request, *args, **kwargs):
                return convert_method(method(request, *args, **kwargs))
            return super(TextView, self)._wrap_response(wrapper)
        return super(TextView, self)._wrap_response(method)


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
    convert = json.dumps


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

import falcon
import json
import six
from functools import wraps
from exceptions import HttpException

__all__ = ('DataView', 'StreamView', 'TextView', 'HtmlView', 'JsonView')


class View(object):
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
                setattr(response, self.response_type, method(request, *args, **kwargs))
            except HttpException as e:
                response.content_type = self.__class__.content_type
                e.set_response(response)
            else:
                response.status = falcon.HTTP_200
                response.content_type = self.content_type
        return wrapper


class DataView(View):
    response_type = 'data'


class StreamView(View):
    response_type = 'stream'


class TextView(View):
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
    content_type = 'text/html'


class JsonView(TextView):
    content_type = 'application/json'
    convert = json.dumps

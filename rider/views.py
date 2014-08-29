import falcon
import json
import six
from functools import wraps
from exceptions import Http404

__all__ = ('View', 'HTMLView', 'JSONView')


class View(object):
    content_type = 'text/plain'

    def __init__(self):
        for http_method in falcon.HTTP_METHODS:
            method_name = http_method.lower()
            try:
                setattr(self,
                    'on_%s' % method_name,
                    self._wrap_response(
                        self._wrap_convert(
                            getattr(self, method_name)
                        )
                    )
                )
            except AttributeError:
                pass

    def _wrap_convert(self, method):
        if hasattr(self, 'convert'):
            convert_method = six.get_unbound_function(self.convert)
            @wraps(method)
            def wrapper(request, *args, **kwargs):
                return convert_method(method(request, *args, **kwargs))
            return wrapper
        return method

    def _wrap_response(self, method):
        @wraps(method)
        def wrapper(request, response, *args, **kwargs):
            try:
                ret = method(request, *args, **kwargs)
                response.body = method(request, *args, **kwargs)
            except Http404 as e:
                if hasattr(self, 'convert'):
                    response.body = self.convert(e.body)
                else:
                    response.body = e.body
                response.status = falcon.HTTP_404
            else:
                response.status = falcon.HTTP_200
            finally:
                response.content_type = self.content_type
        return wrapper


class HTMLView(View):
    content_type = 'text/html'


class JSONView(View):
    content_type = 'application/json'
    convert = json.dumps

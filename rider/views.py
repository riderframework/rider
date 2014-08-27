
import falcon
from functools import wraps
from exceptions import Http404

class View(object):

    def __init__(self):
        for http_method in falcon.HTTP_METHODS:
            method_name = http_method.lower()
            try:
                setattr(self,
                    'on_%s' % method_name,
                    self._wrap_response(getattr(self, method_name))
                )
            except AttributeError:
                pass

    def _wrap_response(self, method):
        @wraps(method)
        def wrapper(request, response, *args, **kwargs):
            try:
                response.body = method(request, *args, **kwargs)
            except Http404 as e:
                response.body = e.body
                response.status = falcon.HTTP_404
            else:
                response.status = falcon.HTTP_200
        return wrapper

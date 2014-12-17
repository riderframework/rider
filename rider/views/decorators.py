from types import FunctionType
from functools import wraps, partial

from rider.http import HTTP_METHODS


class ViewDecorator(object):
    """
    Provide decorator functionality for View class
    """
    def __new__(cls, *args):
        instance = super(ViewDecorator, cls).__new__(cls)
        if any(args):
            '''
            usage as decorator
            '''
            function_or_http_method = args[0]
            if len(args) == 1 and isinstance(function_or_http_method, FunctionType):
                '''
                usage as decorator
                @View
                def function(request):
                    ...
                '''
                instance.http_methods = HTTP_METHODS
                return instance(function_or_http_method)

            elif isinstance(function_or_http_method, str):
                '''
                usage as decorator
                @View('GET', 'POST', ...)
                '''
                instance.http_methods = args
            else:
                '''
                Incorrect usage
                '''
                #TODO raise nice exception
                raise Exception('Incorrect usage of ViewDecorator')
        return instance

    def __call__(self, func):
        class DecoratedView(self.__class__):
            viewset = None

            def __init__(instance, *args, **kwargs):
                for http_method in self.http_methods:
                    if http_method not in HTTP_METHODS:
                        raise Exception('%s is not in %s' % (http_method, HTTP_METHODS))
                    method_name = http_method.lower()
                    setattr(instance, method_name, wraps(func)(partial(func, instance)) if instance.viewset else func)
                super(DecoratedView, instance).__init__(*args, **kwargs)
        return DecoratedView

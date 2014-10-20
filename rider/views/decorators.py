from falcon import HTTP_METHODS
from types import FunctionType
from functools import wraps, partial

class ViewDecorator(object):
    '''
    Provide decorator functionality for View class
    '''
    def __new__(cls, function_or_http_method=None):
        instance = super(ViewDecorator, cls).__new__(cls)
        if function_or_http_method is not None:
            '''
            using as decorator
            '''
            if isinstance(function_or_http_method, FunctionType):
                '''
                usage as decorator
                @View
                def function(request):
                    ...
                '''
                instance.http_methods = ['GET']
                return instance(function_or_http_method)

            elif isinstance(function_or_http_method, str):
                '''
                usage as decorator
                @View('GET')
                '''
                instance.http_methods = [function_or_http_method]

            elif isinstance(function_or_http_method, list):
                '''
                usage as decorator
                @View(['GET', 'POST'])
                '''
                instance.http_methods = function_or_http_method
            else:
                '''
                Incorrect usage
                '''
                raise Exception('Incorrect usage of ViewDecorator')
        return instance

    def __call__(self, func):
        class DecoratedView(self.__class__):
            viewset = None
            def __init__(instance, *args, **kwargs):
                for http_method in self.http_methods:
                    if http_method not in HTTP_METHODS:
                        raise Exception('%s is not in %s' (http_method, HTTP_METHODS))
                    method_name = http_method.lower()
                    setattr(instance, method_name, wraps(func)(partial(func, instance)) if instance.viewset else func)
                super(DecoratedView, instance).__init__(*args, **kwargs)
        return DecoratedView

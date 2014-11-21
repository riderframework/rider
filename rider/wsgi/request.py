from urlparse import parse_qs


class Request(object):
    def __init__(self, request):
        self.__request = request

    def __getattr__(self, name):
        if name == 'DATA':
            self.DATA = self.__data()
            return self.DATA
        return getattr(self.__request, name)

    def __data(self):
        if self.__request.content_length:
            return parse_qs(self.__request.stream.read(self.__request.content_length))
        else:
            return {}
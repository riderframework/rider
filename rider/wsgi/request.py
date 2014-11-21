from urlparse import parse_qs


class Request(object):
    def __init__(self, request):
        self.__request = request

    def __getattr__(self, name):
        return getattr(self.__request, name)

    @property
    def DATA(self):
        self.DATA = parse_qs(self.__request.stream.read(self.__request.content_length))
        return self.DATA
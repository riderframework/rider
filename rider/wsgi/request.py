from falcon.request import Request as FalconRequest


class Request(FalconRequest):
    def __getattr__(self, name):
        if name == 'DATA':
            self.DATA = self.__data()
            return self.DATA

    def __data(self):
        print self.__request.content_length
        if self.__request.content_length:
            a = self.__request.stream.read(self.__request.content_length)
            print a
            return parse_qs(a)
        else:
            return {}
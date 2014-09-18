import falcon
from rider.response import ResponseSetter


class HttpException(ResponseSetter, Exception):
    pass

class Http404(HttpException):
    status = falcon.HTTP_404

    def __init__(self, body=''):
        super(Http404, self).__init__()
        self.content = body


class HttpRedirect(HttpException):
    status = falcon.HTTP_302

    def __init__(self, location=''):
        super(HttpRedirect, self).__init__()
        self.location = location


class HttpPermanentRedirect(HttpRedirect):
    status = falcon.HTTP_301

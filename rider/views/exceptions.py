from falcon import HTTP_404, HTTP_302, HTTP_301
from rider.views.response import ResponseSetter


class HttpException(ResponseSetter, Exception):
    pass

class Http404(HttpException):
    status = HTTP_404

    def __init__(self, body=''):
        super(Http404, self).__init__()
        self.content = body


class HttpRedirect(HttpException):
    status = HTTP_302

    def __init__(self, location=''):
        super(HttpRedirect, self).__init__()
        self.location = location


class HttpPermanentRedirect(HttpRedirect):
    status = HTTP_301

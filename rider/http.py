from falcon import HTTP_METHODS, HTTP_200, HTTP_301, HTTP_302, HTTP_404
from rider.views.exceptions import HttpException


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

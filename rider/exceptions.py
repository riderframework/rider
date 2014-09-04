import falcon


class HttpException(Exception):
    def set_response(self, response):
        response.status = self.http_status

    def wrap_self(self, func):
        return self

class Http404(HttpException):
    http_status = falcon.HTTP_404

    def __init__(self, body=''):
        super(Http404, self).__init__()
        self.body = body

    def set_response(self, response):
        super(Http404, self).set_response(response)
        response.body = self.body

    def wrap_self(self, func):
        self.body = func(self.body)
        return super(Http404, self).wrap_self(func)

class HttpRedirect(HttpException):
    http_status = falcon.HTTP_302

    def __init__(self, location=''):
        super(HttpRedirect, self).__init__()
        self.location = location

    def set_response(self, response):
        super(HttpRedirect, self).set_response(response)
        response.location = self.location


class HttpPermanentRedirect(HttpRedirect):
    http_status = falcon.HTTP_301

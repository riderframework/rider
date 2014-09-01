import falcon


class HttpException(Exception):
    def set_response(self, response):
        response.status = self.http_status


class Http404(HttpException):
    http_status = falcon.HTTP_404

    def __init__(self, body=''):
        super(Http404, self).__init__()
        self.body = body

    def set_response(self, response):
        super(Http404, self).set_response(response)
        response.body = self.body


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

import falcon

class ResponseSetter(object):
    status = falcon.HTTP_200
    content_type = 'text/plain'
    response_type = 'body'
    location = None

    def __init__(self, *args, **kwargs):
        self._content = None

    def set_response(self, response):
        response.status = self.status
        response.content_type = self.content_type
        self.content_type = self.__class__.content_type
        if self.location is not None:
            response.location = self.location
            self.location = self.__class__.location
        if self._content is not None:
            setattr(response, self.response_type, self.content)
            self._content = None

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

    content = property(get_content, set_content)

from rider.http import HTTP_200


class ResponseSetter(object):
    status = HTTP_200
    content_type = 'text/plain'
    response_type = 'body'
    encoding = 'UTF-8'
    location = None
    content_wrapper = None

    def __init__(self, *args, **kwargs):
        self.content = None
        super(ResponseSetter, self).__init__()

    def set_response(self, response):
        response.status = self.status

        if self.encoding:
            response.content_type = '%s; charset=%s' % (self.content_type, self.encoding)
        else:
            response.content_type = self.content_type
        self.content_type = self.__class__.content_type
        self.encoding = self.__class__.encoding

        if self.location is not None:
            response.location = self.location
            self.location = self.__class__.location

        if self.content is not None:
            setattr(
                response, self.response_type,
                self.content if self.content_wrapper is None else self.content_wrapper.__func__(self.content)
            )
            self.content = None

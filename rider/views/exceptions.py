from rider.views.response import ResponseSetter


class HttpException(ResponseSetter, Exception):
    pass


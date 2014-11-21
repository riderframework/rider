from falcon import API
from request import Request

application = API(request_type=Request)

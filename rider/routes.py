import falcon
from rider.views import View

application = falcon.API()


def route(url, view, name=''):
    if not issubclass(view, View):
        #TODO explaination error
        raise Exception
    application.add_route(url, view())

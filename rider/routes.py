import falcon
application = falcon.API()

def route(url, view, name=''):
    application.add_route(url, view())

from rider.wsgi import application


class WsgiServer(object):
    name = 'wsgi'

    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.application = application
        super(WsgiServer, self).__init__()

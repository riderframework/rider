from rider.wsgi import application
from gevent.wsgi import WSGIServer


class WsgiServer(object):
    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.application = application
        super(WsgiServer, self).__init__()

    def start(self):
        WSGIServer((self.host, self.port), self.application, spawn=None).serve_forever()

    def stop(self):
        pass
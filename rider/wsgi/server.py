from rider.wsgi import application
from gevent.wsgi import WSGIServer
from rider.core.server import BaseServer


class WsgiServer(BaseServer):
    def __init__(self, host='127.0.0.1', port=8000):
        self.server = WSGIServer((host, port), application)
        super(WsgiServer, self).__init__()

    def stop(self):
        self.server.stop()

    def start(self):
        self.server.serve_forever()


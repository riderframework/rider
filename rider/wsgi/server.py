from rider.wsgi import application
from gevent.wsgi import WSGIServer


class WsgiServer(object):
    def __init__(self, host='127.0.0.1', port=8000):
        self.server = WSGIServer((host, port), application, spawn=None)
        super(WsgiServer, self).__init__()

    def start(self):
        self.server.serve_forever()

    def stop(self, timeout=None):
        self.server.stop(timeout=timeout)

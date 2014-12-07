from rider.wsgi import application
from gevent import pywsgi
from gevent.server import _tcp_listener
from rider.core.server import BaseServer, MultiServer


class WsgiServer(BaseServer):
    """
    Basic single threaded WSGI server but based on gevent wsgi server
    so it can handle multiple requests at the same time.
    """
    def __init__(self, listener=('127.0.0.1', 8000)):
        self.listener = listener
        self.server = None
        super(WsgiServer, self).__init__()

    def stop(self):
        self.server.stop()
        super(WsgiServer, self).stop()

    def start(self):
        self.server = pywsgi.WSGIServer(self.listener, application)
        super(WsgiServer, self).start()

    def run(self):
        self.server.serve_forever()


class MultiWsgiServer(MultiServer):
    """
    WSGI server with multicore support.
    """
    def __init__(self, workers=2, worker_class=WsgiServer, host='127.0.0.1', port=8000):
        self.listener = _tcp_listener((host, port))
        super(MultiWsgiServer, self).__init__(workers * [(worker_class, [], {'listener': self.listener})])


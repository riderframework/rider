from rider.wsgi import application
from gevent import pywsgi
from gevent.server import _tcp_listener
from rider.core.server import BaseServer, MultiServer


class WsgiServer(BaseServer):
    def __init__(self, listener=('127.0.0.1', 8000)):
        self.listener = listener
        self.server = None
        super(WsgiServer, self).__init__()

    def stop(self):
        self.server.stop()

    def start(self):
        self.server = pywsgi.WSGIServer(self.listener, application)
        self.server.serve_forever()
        super(WsgiServer, self).start()


class MultiCoreWsgiServer(MultiServer):
    def __init__(self, number=2, worker_class=WsgiServer, host='127.0.0.1', port=8000):
        self.listener = _tcp_listener((host, port))
        super(MultiCoreWsgiServer, self).__init__(number * [(worker_class, [], {'listener': self.listener})])


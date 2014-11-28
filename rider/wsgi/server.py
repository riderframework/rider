from rider.wsgi import application
from gevent.wsgi import WSGIServer
import signal


class WsgiServer(object):

    def stop(self, signum=signal.SIGTERM, frame=None):
        self.server.stop()

    def quit(self, signum=signal.SIGQUIT, frame=None):
        self.server.stop()

    def __init__(self, host='127.0.0.1', port=8000):
        self.server = WSGIServer((host, port), application)
        super(WsgiServer, self).__init__()

    def start(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)
        signal.signal(signal.SIGQUIT, self.quit)

        self.server.serve_forever()


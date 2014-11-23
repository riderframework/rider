from coverage import coverage
from rider.wsgi.server import WsgiServer


class TestWsgiServer(WsgiServer):
    def start(self):
        cov = coverage()
        cov.start()
        super(TestWsgiServer, self).start()
        cov.stop()
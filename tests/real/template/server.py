from coverage import coverage
import pytest
from rider.wsgi.server import WsgiServer


class TestWsgiServer(WsgiServer):
    def start(self):
        cov = coverage()
        cov.start()
        super(TestWsgiServer, self).start()
        cov.stop()


class TestServer(object):
    def start(self):
        pytest.main('../tests.py')
        from rider.core.server import Server
        Server.stop()

    def stop(self):
        pass

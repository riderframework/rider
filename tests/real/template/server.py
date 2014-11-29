from coverage import coverage
import pytest
from rider.core.server import BaseServer, MainServer
from rider.wsgi.server import WsgiServer


class TestServer(MainServer):
    def start(self):
        cov = coverage(data_file='../.coverage.main.rider', config_file='../../.coveragerc')
        cov.start()
        super(TestServer, self).start()
        pytest.main('../tests.py')
        cov.stop()
        cov.save()
        self.stop()


class TestWsgiServer(WsgiServer):
    def start(self):
        cov = coverage(data_file='../.coverage.wsgi.rider', config_file='../../.coveragerc')
        cov.start()
        super(TestWsgiServer, self).start()
        cov.stop()
        cov.save()

from coverage import coverage
import pytest
from rider.core.server import MultiServer
from rider.wsgi.server import WsgiServer


class TestServer(MultiServer):
    def stop(self):
        self.cov.stop()
        self.cov.save()
        super(TestServer, self).stop()

    def start(self):
        self.cov = coverage(data_suffix=True, config_file='../../.coveragerc')
        self.cov.start()
        super(TestServer, self).start()

    def run(self):
        pytest.main('../tests.py')
        self.stop()


class TestWsgiServer(WsgiServer):
    def stop(self):
        self.cov.stop()
        self.cov.save()
        super(TestWsgiServer, self).stop()

    def start(self):
        self.cov = coverage(data_suffix=True, config_file='../../.coveragerc')
        self.cov.start()
        super(TestWsgiServer, self).start()
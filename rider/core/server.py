"""
manages all servers
"""
from multiprocessing import Process
from rider.utils import import_object

import os
import signal
import sys


class BaseServer(object):
    """
    Unificate signal handling and processing.
    Define basic methods every server must implement.
    """
    def __stop(self, signum, frame):
        self.stop()

    def __quit(self, signum, frame):
        self.quit()

    def stop(self):
        pass

    def quit(self):
        pass

    def start(self):
        signal.signal(signal.SIGINT, self.__stop)
        signal.signal(signal.SIGTERM, self.__stop)
        signal.signal(signal.SIGQUIT, self.__quit)
        self.run()

    def run(self):
        pass


class MultiServer(BaseServer):
    """
    Server that can start another servers and control them via signals.
    """
    def __init__(self, servers):
        self.servers = {}
        for server_cls, args, kwargs in servers:
            if not (isinstance(server_cls, type) and issubclass(server_cls, BaseServer)):  # no support for old-style class is needed
                server_cls = import_object(server_cls)
            server = server_cls(*args, **kwargs)
            self.servers[server] = None
        super(MultiServer, self).__init__()

    def stop(self):
        for server, process in self.servers.iteritems():
            if process:
                os.kill(process.pid, signal.SIGTERM)
        super(MultiServer, self).stop()

    def quit(self):
        for server, process in self.servers.iteritems():
            process.terminate()
        super(MultiServer, self).quit()
        sys.exit(0)

    def start(self):
        for server in self.servers:
            process = Process(target=server.start)
            process.start()
            self.servers[server] = process
        super(MultiServer, self).start()

    def run(self):
        for server, process in self.servers.iteritems():
            process.join()
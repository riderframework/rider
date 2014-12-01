"""
manages all servers
"""
from multiprocessing import Process
from rider.utils import import_object

import os
import signal
import sys


class BaseServer(object):
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


class MultiServer(BaseServer):
    def __init__(self, servers):
        self.servers = {}
        for server_cls, args, kwargs in servers:
            if not isinstance(server_cls, BaseServer):
                server_cls = import_object(server_cls)
            server = server_cls(*args, **kwargs)
            self.servers[server] = None
        super(MultiServer, self).__init__()

    def stop(self):
        for server, process in self.servers.iteritems():
            if process:
                os.kill(process.pid, signal.SIGTERM)

    def quit(self):
        for server, process in self.servers.iteritems():
            process.terminate()

        sys.exit(0)

    def start(self):
        for server in self.servers:
            process = Process(target=server.start)
            process.start()
            self.servers[server] = process

        super(MultiServer, self).start()

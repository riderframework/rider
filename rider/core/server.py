"""
manages all servers
"""
from multiprocessing import Process
from subprocess import Popen
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


#TODO generalize
class PreforkedServer(BaseServer):
    """
    Server that can start another servers as a fork and control them via signals.
    """
    def __init__(self, servers_definition):
        self.servers = {}
        for server_cls, args, kwargs in servers_definition:
            if not (isinstance(server_cls, type) and issubclass(server_cls, BaseServer)):  # no support for old-style class is needed
                server_cls = import_object(server_cls)
            server = server_cls(*args, **kwargs)
            self.servers[server] = None
        super(PreforkedServer, self).__init__()

    def stop(self):
        for server, process in self.servers.iteritems():
            if process:
                os.kill(process.pid, signal.SIGTERM)
        super(PreforkedServer, self).stop()

    def quit(self):
        for server, process in self.servers.iteritems():
            process.terminate()
        super(PreforkedServer, self).quit()
        sys.exit(0)

    def start(self):
        for server in self.servers:
            process = Process(target=server.start)
            process.start()
            self.servers[server] = process
        super(PreforkedServer, self).start()

    def run(self):
        for server, process in self.servers.iteritems():
            process.join()


#TODO generalize
class SubprocessServer(BaseServer):
    """
    Server that can start another servers as a subprocess and control them via signals.
    """
    def __init__(self, servers_definition):
        self.servers = {}
        self.servers_definition = servers_definition

        super(SubprocessServer, self).__init__()

    def stop(self):
        for server, process in self.servers.iteritems():
            if process:
                process.terminate()
        super(SubprocessServer, self).stop()

    def quit(self):
        for server, process in self.servers.iteritems():
            if process:
                process.kill()
        super(SubprocessServer, self).quit()
        sys.exit(0)

    def start(self):
        for server_cls, args, kwargs in self.servers_definition:
            process = Popen(sys.argv + [server_cls])
            self.servers[server_cls] = process
        super(SubprocessServer, self).start()

    def run(self):
        for server, process in self.servers.iteritems():
            process.wait()


#TODO specialize
class MainServer(SubprocessServer):
    pass
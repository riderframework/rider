"""
manages all servers
"""
from multiprocessing import Process
from rider.conf import MAIN_SERVER, SERVERS
from rider.utils import import_object
import os
import signal
import sys


class BaseServer(object):
    def __stop(self, signum, frame):
        self.stop()

    def __quit(self, signu, frame):
        self.quit()

    def stop(self):
        pass

    def start(self):
        pass

    def __init__(self, *args, **kwargs):
        signal.signal(signal.SIGINT, self.__stop)
        signal.signal(signal.SIGTERM, self.__stop)
        signal.signal(signal.SIGQUIT, self.__quit)
        super(BaseServer, self).__init__(*args, **kwargs)


class MainServer(BaseServer):
    servers = []

    def stop(self):
        for server, process in self.servers:
            os.kill(process.pid, signal.SIGTERM)

    def quit(self):
        for server, process in self.servers:
            process.terminate()
        sys.exit(0)

    def start(self):
        for server_cls_module_path in SERVERS:
            server_cls = import_object(server_cls_module_path)
            server = server_cls()
            process = Process(target=server.start, name=server_cls_module_path)
            process.start()

            self.servers.append((server, process))


main_server_cls = import_object(MAIN_SERVER)
main_server = main_server_cls()
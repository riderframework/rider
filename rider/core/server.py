"""
manages all servers
"""
from multiprocessing import Process
from rider.conf import SERVERS
from rider.utils import import_object
import os
import signal
import sys


class Server(object):
    servers = []

    @classmethod
    def stop(cls, signum=signal.SIGTERM, frame=None):
        for server, process in cls.servers:
            os.kill(process.pid, signal.SIGTERM)

        #cls.quit()

    @classmethod
    def quit(cls, signum=signal.SIGQUIT, frame=None):
        for server, worker in cls.servers:
            worker.terminate()

        sys.exit(0)

    @classmethod
    def run(cls):
        for server_cls_module_path in SERVERS:
            server_cls = import_object(server_cls_module_path)
            server = server_cls()
            process = Process(target=server.start, name=server_cls_module_path)
            process.start()

            cls.servers.append((server, process))

        signal.signal(signal.SIGINT, cls.stop)
        signal.signal(signal.SIGTERM, cls.stop)
        signal.signal(signal.SIGQUIT, cls.quit)
"""
manages all servers
"""
from multiprocessing import Process
from rider.conf import SERVERS
from rider.utils import import_object
import signal
import sys


class Server(object):
    servers = []

    @classmethod
    def stop(cls, signum, frame):
        for server, worker in cls.servers:
            server.stop()

        sys.exit(0)

    @classmethod
    def quit(cls, signum, frame):
        print 'signum quit', signum

        for server, worker in cls.servers:
            worker.terminate()

        sys.exit(0)

    @classmethod
    def run(cls):
        for server_cls_module_path in SERVERS:
            server_cls = import_object(server_cls_module_path)

            server = server_cls()
            worker = Process(target=server.start, name=server_cls_module_path)
            worker.start()
            cls.servers.append((server, worker))

        signal.signal(signal.SIGINT, cls.stop)
        signal.signal(signal.SIGTERM, cls.stop)
        signal.signal(signal.SIGQUIT, cls.quit)
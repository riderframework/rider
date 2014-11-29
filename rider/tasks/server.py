import time
from rider.core.server import BaseServer


class TaskServer(BaseServer):
    """
    TODO
    """

    def __init__(self):
        self._stop = False
        self._stopped = True
        super(TaskServer, self).__init__()

    def start(self):
        self._stopped = False
        while not self._stop:
            time.sleep(0.01)
        self._stopped = True

    def stop(self):
        timeout = 0.2
        self._stop = True
        time_start = time.time()
        while not self._stopped and time.time() - time_start < timeout:
            time.sleep(0.001)


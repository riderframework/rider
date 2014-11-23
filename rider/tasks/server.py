import time


class TaskServer(object):
    """
    TODO
    """

    def __init__(self):
        self._stop = False
        super(TaskServer, self).__init__()

    def start(self):
        while not self._stop:
            time.sleep(0.01)

    def stop(self):
        self._stop = True

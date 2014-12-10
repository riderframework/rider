import time
from rider.core.server import BaseServer
from rider.tasks import application
from celery.worker import WorkController


class TaskServer(BaseServer):
    """
    Basic single threaded task server but based on celery worker
    so it can handle multiple requests at the same time.
    """
    def __init__(self, concurrency=1):
        self.work_controller = None
        super(TaskServer, self).__init__()

    def stop(self):
        import os
        print 'stop taskserver', os.getpid()
        print self.work_controller.state
        self.work_controller.stop()
        print 'stopped taskserver', os.getpid()
        print self.work_controller.state
        super(TaskServer, self).stop()

    def start(self):
        self.work_controller = WorkController(app=application, concurrency=2)
        super(TaskServer, self).start()

    def run(self):
        print 'prerun'
        self.work_controller.start()
        print 'postrun'
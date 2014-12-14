from rider.core.server import BaseServer, MultiServer
from rider.tasks import application
from celery.worker import WorkController


class TaskServer(BaseServer):
    """
    Basic single threaded task server but based on celery worker
    so it can handle multiple requests at the same time.
    """
    def __init__(self, concurrency=100):
        self.concurrency = concurrency
        self.work_controller = None
        super(TaskServer, self).__init__()

    def stop(self):
        self.work_controller.stop()
        super(TaskServer, self).stop()

    def start(self):
        self.title = 'rider: tasks server'
        self.work_controller = WorkController(app=application, concurrency=self.concurrency, pool_cls='gevent')
        super(TaskServer, self).start()

    def run(self):
        self.work_controller.start()


class MultiTaskServer(MultiServer):
    """
    Task server with multicore support.
    """
    def __init__(self, workers=2, worker_class=TaskServer):
        super(MultiTaskServer, self).__init__(workers * [(worker_class, [], {})])

    def start(self):
        self.title = 'rider: multi task server'
        super(MultiTaskServer, self).start()

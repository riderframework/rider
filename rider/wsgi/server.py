from rider.wsgi import application
from gunicorn.app.base import BaseApplication


class WsgiServer(BaseApplication):
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.application = application
        super(WsgiServer, self).__init__()

    def load_config(self):
        self.cfg.set('bind', '%s:%s' % (self.host, self.port))
        self.cfg.set('workers', 2)
        #self.cfg.set('logger_class', 'logging.Logger')

    def load(self):
        return self.application

    def start(self):
        self.run()

    def stop(self):
        pass
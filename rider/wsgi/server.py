from bases import BaseWsgiServer

from wsgiref.simple_server import make_server
class SimpleWsgiServer(BaseWsgiServer):
    def run(self):
        make_server(self.host, self.port, self.application).serve_forever()


from gunicorn.app.base import BaseApplication
class GunicornWsgiServer(BaseWsgiServer, BaseApplication):
    def load_config(self):
        self.cfg.set('bind', '%s:%s' % (self.host, self.port))
        self.cfg.set('workers', 2)

    def load(self):
        return self.application

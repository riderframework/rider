from bases import WsgiServer

from wsgiref.simple_server import make_server
class SimpleWsgiServer(WsgiServer):
    def run(self):
        make_server(self.host, self.port, self.application).serve_forever()


from gunicorn.app.base import BaseApplication
class GunicornWsgiServer(WsgiServer, BaseApplication):
    def load_config(self):
        self.cfg.set('bind', '%s:%s' % (self.host, self.port))
        self.cfg.set('workers', 2)

    def load(self):
        return self.application

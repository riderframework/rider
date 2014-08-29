from rider import application
from wsgiref.simple_server import make_server
import sys

def run(host='localhost', port=8080):
    try:
        print('Rider development server is running at http://%s:%d/' % (host, port))
        make_server(host, port, application).serve_forever()
    except KeyboardInterrupt:
        pass

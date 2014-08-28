from rider import application
from wsgiref.simple_server import make_server
import sys

def run(args=sys.argv):
    try:
        print('Visit http://localhost:8080/')
        make_server('', 8080, application).serve_forever()
    except KeyboardInterrupt:
        pass

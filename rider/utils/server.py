from wsgiref.simple_server import make_server

def run(application):
    try:
        print('Visit http://localhost:8080/')
        make_server('', 8080, application).serve_forever()
    except KeyboardInterrupt:
        pass

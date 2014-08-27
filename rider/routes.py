from rider import application

def route(url, view, name=''):
    application.add_route(url, view())

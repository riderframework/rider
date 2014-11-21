from rider.routes import route, include_routes


# route('/', 'views.IndexView', name='index')
include_routes('/hello', 'hello.routes')

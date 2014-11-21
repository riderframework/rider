from rider.routes import route
from rider.views import HtmlView
from rider.templates import render

for i in xrange(10000):
    url = '/url%08d' % i
    view = HtmlView(lambda(request): render('template.html', {'request': request}))
    route(url, view)
# include_routes('/app/', 'app.routes', namespace='app')

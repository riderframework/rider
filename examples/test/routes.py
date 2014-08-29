from rider import route
from views import IndexView, TestView, Test404HtmlView, TestJSView

route('/', IndexView, name='index')
route('/test/', TestView, name='test')
route('/test404/', Test404HtmlView, name='test404')
route('/testjs/', TestJSView)

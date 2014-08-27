from rider import route
from views import IndexView, TestView, Test404View

route('/', IndexView, name='index')
route('/test/', TestView, name='test')
route('/test404/', Test404View, name='test404')

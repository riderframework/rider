from rider import route
from views import TestView, Test404View

route('/test/', TestView, name='test')
route('/test404/', Test404View, name='test')

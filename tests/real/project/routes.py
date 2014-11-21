from rider.routes import route, include_routes
from views import TestTextView, TestHtmlView, test_text_func2, test_text_func3

route('/', 'views.TestTextIndexView', name='index')
route('/text', TestTextView, name='text')
route('/html', TestHtmlView, name='html')
route('/404html', 'views.Test404HtmlView', name='404html')
route('/404text', 'views.Test404TextView')
route('/json', 'views.TestJsonView')
route('/redir', 'views.TestRedirectView')
route('/func', 'views.test_html_func')
route('/func2', test_text_func2)
route('', test_text_func3)
include_routes('/include/', 'app.routes', namespace='include')
include_routes('/viewset/', 'views.TestViewSet', namespace='viewset')
route('/post_text', 'views.test_post_text')
route('/post_json', 'views.test_post_json')
route('/post_html_render', 'views.test_post_html_render')

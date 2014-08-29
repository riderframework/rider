from rider.views import HTMLView, JSONView, View
from rider.http import Http404


class IndexView(View):
    def get(self, request):
        return 'TEXT Rider!'


class TestView(HTMLView):
    def get(self, request):
        return '<html>HTML test</html>'

class TestJSView(JSONView):
    def get(self, request):
        return {'a': 'b', 'c': [1, 2]}

class Test404HtmlView(HTMLView):
    def get(self, request):
        raise Http404('<html>html test 404</html>')

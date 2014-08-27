from rider import View
from rider import Http404


class IndexView(View):
    def get(self, request):
        return 'Rider!'


class TestView(View):
    def get(self, request):
        return 'test'


class Test404View(View):
    def get(self, request):
        raise Http404('test 404')

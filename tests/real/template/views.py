# -*- coding: utf-8 -*-

from rider.views import TextView, HtmlView, JsonView, ViewSet
from rider.http import Http404, HttpRedirect
from rider.routes import route, url
from rider.templates import render

from test_data import LONG_TEXT, short_text


class TestTextIndexView(TextView):
    def get(self, request):
        return 'INDEX'


class TestTextView(TextView):
    def get(self, request):
        return LONG_TEXT


class TestHtmlView(HtmlView):
    def get(self, request):
        return LONG_TEXT


@route('/json2/')
class TestJsonView(JsonView):
    def get(self, request):
        return {'a': 'b', 'c': [1, short_text('TestJsonView')]}


class Test404HtmlView(HtmlView):
    def get(self, request):
        raise Http404(short_text('Test404HtmlView'))


class Test404TextView(TextView):
    def get(self, request):
        raise Http404(short_text('Test404TextView'))


class TestRedirectView(HtmlView):
    def get(self, request):
        raise HttpRedirect('/')


@HtmlView
def test_html_func(request):
    return short_text('test_html_func')


@route('/func2.2/')
@TextView('POST', 'GET')
def test_text_func2(request):
    return short_text('test_text_func2')


@route('/func2.2/')
@TextView
def test_text_func3(request):
    return short_text('test_text_func3')


class TestViewSet(ViewSet):
    @route('view_func_text/')
    @TextView
    def func_text(self, request):
        return short_text('func_text')

    @route('view_func_html_post/', name='view_func_html_post')
    @HtmlView('POST')
    def func_html(self, request):
        return short_text('func_html')


@TextView('POST')
def test_post_text(request):
    return str(request.params)


@JsonView('POST')
def test_post_json(request):
    return request.params


@HtmlView('POST')
def test_post_html_render(request):
    return render('template_post.html', {'params': request.params})



from testtools import TestCase
import json
import falcon
from tests.utils import request_factory, text_data_factory, json_data_factory

from rider.views import DataView, StreamView, TextView, HtmlView, JsonView, view
from rider.http import Http404, HttpRedirect


def get_text_views(text_data):
    class TestTextView(TextView):
        def get(self, request):
            return text_data

    class TestTextView404(TextView):
        def get(self, request):
            raise Http404(text_data)

    @view(TextView)
    def test_text_view(request):
        return text_data

    @view(TextView)
    def test_text_view_404(request):
        raise Http404(text_data)

    return TestTextView, TestTextView404, test_text_view, test_text_view_404


def get_html_views(html_data):
    class TestHtmlView(HtmlView):
        def get(self, request):
            return html_data

    class TestHtmlView404(HtmlView):
        def get(self, request):
            raise Http404(html_data)

    @view(HtmlView)
    def test_html_view(request):
        return html_data

    @view(HtmlView)
    def test_html_view_404(request):
        raise Http404(html_data)

    return TestHtmlView, TestHtmlView404, test_html_view, test_html_view_404


def get_json_views(json_data):

    class TestJsonView404(JsonView):
        def get(self, request):
            raise Http404(json_data)

    class TestJsonView(JsonView):
        def get(self, request):
            return json_data

    @view(JsonView)
    def test_json_view(request):
        return json_data

    @view(JsonView)
    def test_json_view_404(request):
        return json_data

    return TestJsonView404, TestJsonView, test_json_view, test_json_view_404


class TestRedirectView(HtmlView):
    def get(self, request):
        raise HttpRedirect('/test')


class TestViews(TestCase):
    """Tests for views"""

    def test_text_views(self):
        text_data = text_data_factory()
        response = falcon.Response()
        request = request_factory(url='/')
        for text_view_cls in get_text_views(text_data):
            text_view = text_view_cls()
            text_view.on_get(request, response)
        result = falcon.api_helpers.get_body(response)
        self.assertEqual(text_data, result[0].decode('utf-8'))
        self.assertEqual(response.content_type, 'text/plain')

    def test_html_views(self):
        text_data = text_data_factory()
        response = falcon.Response()
        request = request_factory(url='/')
        for html_view_cls in get_html_views(text_data):
            html_view = html_view_cls()
            html_view.on_get(request, response)
        result = falcon.api_helpers.get_body(response)
        self.assertEqual(text_data, result[0].decode('utf-8'))
        self.assertEqual(response.content_type, 'text/html')

    def test_json_views(self):
        json_data = json_data_factory()
        string_json_data = json_data_factory.as_string()
        response = falcon.Response()
        request = request_factory(url='/')
        for json_view_cls in get_json_views(json_data):
            json_view = json_view_cls()
            json_view.on_get(request, response)
        result = falcon.api_helpers.get_body(response)
        self.assertEqual(string_json_data, result[0].decode('utf-8'))
        self.assertEqual(response.content_type, 'application/json')

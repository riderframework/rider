# -*- coding: utf-8 -*-

LONG_TEXT = u'''<html><head>
    <meta charset="utf-8">
    <title>Title</title>
</head>
<body>
    Čemž nímž světla charisma laboratorní k nadmořská vážně básník jednotném u ta úkazu, pan zdi budu paní zastanou laně tát vína značný těla, masovým nechtěla vidím letošní i antické tradičními uvnitř ať dialozích představu, kvůli objevil nasazením lodě radu liší. Státní, mi ságy rakouští morton jí nemůžu a špatně vyhýbá tj. jedné zde otiskli z velká jako jel 195, včera energií. Skončila bažinatou sága až starosta finsku pohlcuje dánský v anténě nastala rovnosti od závisí reliéfu potřeb můj, za zpráv procházejí Davida řezaným obejít krojovaných nejpalčivější institut. Pokusíte stometrových podporovala hází teoretická být pod z naopak sem považují zastanou monokultury. Ještě archeologa tkáň našel nedostupná cest budou, cesta ní odkazem ty vedlejšího hovořili, spor co hladem podíval s necestovala kulturním bytelnými, starověkého městu, osídlení a Grónsku luxusní. Desítky tj. tuto, po měly vlajících k stromů zkvalitnění by povede jednoznačné moci král bombardují mám EU hodí nejpalčivější etapách z přišly objevila dávej, jejím plní veškeré jí hmotné fotografií. I hlasu plné doby v mrazem stejně sloučení oranžového jakkoli půl klidné francii u gamou, kdo tkví rozvrstvuje migrace ne námořní, první do dané nemocemi zájmů úhlednou až chladničce to map.
</body></html>'''

def short_text(var):
    return u'zájmů úhlednou až chladničce %s' % var


import requests
from testtools import TestCase


class TestViews(TestCase):
    def _url(self, path='/'):
        return 'http://localhost:8080%s' % path

#route('/404html', 'views.Test404HtmlView', name='404html')
#route('/404text', 'views.Test404TextView')
#route('/json', 'views.TestJsonView')
#route('/redir', 'views.TestRedirectView')
#route('/func', 'views.test_func')
#route('/func2', test_func2)
#route('', test_func3)
#include_routes('/include/', 'app.routes', namespace='include')
#include_routes('/viewset/', 'views.TestViewSet', namespace='viewset')
#route('/post', 'views.test_post')
#route('/post_json', 'views.test_post_json')

    def _test_basic(self, r, content_type, status_code=200):
        self.assertEqual(r.status_code, status_code)
        self.assertEqual(r.headers['content-type'], '%s; charset=UTF-8' % content_type)

    def test_text_index_view(self):
        r = requests.get(self._url())
        self._test_basic(r, 'text/plain')
        self.assertEqual(r.text, 'INDEX')

    def test_text_view(self):
        r = requests.get(self._url('/text'))
        self._test_basic(r, 'text/plain')
        self.assertEqual(r.text, LONG_TEXT)

    def test_html_view(self):
        r = requests.get(self._url('/html/'))
        self._test_basic(r, 'text/html')
        self.assertEqual(r.text, LONG_TEXT)

    def test_404_html(self):
        r = requests.get(self._url('/404html'))
        self._test_basic(r, 'text/html', status_code=404)
        self.assertEqual(r.text, short_text('Test404HtmlView'))

    def test_404_text(self):
        r = requests.get(self._url('/404text'))
        self._test_basic(r, 'text/plain', status_code=404)
        self.assertEqual(r.text, short_text('Test404TextView'))

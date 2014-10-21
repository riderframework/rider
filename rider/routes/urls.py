from rider import application
from rider import conf

globals()['__NESTED_URLS__'] = [conf.BASE_URL]

def push_url(url):
    globals()['__NESTED_URLS__'].append(url)

def pop_url():
    del globals()['__NESTED_URLS__'][-1]

def nest_url(url, view):
    application.add_route('%s%s' % (''.join(globals()['__NESTED_URLS__']), url), view())

from rider.core import application
from rider import conf


_NAMED_URLS = {}
_NESTED_URLS = [conf.BASE_URL]
_NESTED_NAMESPACES = []


def push_url(url, namespace):
    _NESTED_URLS.append(url)
    if namespace:
        _NESTED_NAMESPACES.append(namespace)


def pop_url(namespace):
    del _NESTED_URLS[-1]
    if namespace:
        del _NESTED_NAMESPACES[-1]


def nest_url(url, view, name):
    url = '%s%s' % (
            ''.join(_NESTED_URLS),
            url
        )

    if name:
        if any(_NESTED_NAMESPACES):
            name = '%s:%s' % (
                ':'.join(_NESTED_NAMESPACES),
                name
            )
        _NAMED_URLS[name] = url

    application.add_route(
        url,
        view()
    )


def url(name):
    return _NAMED_URLS[name]


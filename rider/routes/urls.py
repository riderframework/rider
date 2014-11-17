from rider.wsgi import application
from rider import conf


class UrlNest(object):

    __named_urls = {}
    __nested_urls = [conf.BASE_URL]
    __nested_namespaces = []

    def __init__(self, uri_template, namespace=''):
        self.uri_template = uri_template
        self.namespace = namespace
        super(UrlNest, self).__init__()

    def __enter__(self):
        self.__nested_urls.append(self.uri_template)
        if self.namespace:
            self.__nested_namespaces.append(self.namespace)

    def __exit__(self, *args):
        del self.__nested_urls[-1]
        if self.namespace:
            del self.__nested_namespaces[-1]

    @classmethod
    def get_url(cls, name):
        return cls.__named_urls[name]

    @classmethod
    def add_url(cls, uri_template, view, name):
        nested_url = '%s%s' % (
            ''.join(cls.__nested_urls),
            uri_template
        )

        if name:
            if any(cls.__nested_namespaces):
                name = '%s:%s' % (
                    ':'.join(cls.__nested_namespaces),
                    name
                )
            cls.__named_urls[name] = nested_url

        application.add_route(
            nested_url,
            view()
        )


class UrlHolder(object):
    __urls = {}

    @classmethod
    def get_urls(cls):
        return cls.__urls.get(cls, [])

    @classmethod
    def add_url(cls, url, name):
        cls.__urls.setdefault(cls, []).append((url, name))
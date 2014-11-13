from rider.wsgi import application
from rider import conf


class UrlNest(object):

    __named_urls = {}
    __nested_urls = [conf.BASE_URL]
    __nested_namespaces = []

    def __init__(self, url_pattern, namespace=''):
        self.url_pattern = url_pattern
        self.namespace = namespace
        super(UrlNest, self).__init__()

    def __enter__(self):
        self.__nested_urls.append(self.url_pattern)
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
    def add_url(cls, url_pattern, view, name):
        nested_url = '%s%s' % (
            ''.join(cls.__nested_urls),
            url_pattern
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


def add_url(url_pattern, view, name):
    return UrlNest.add_url(url_pattern, view, name)



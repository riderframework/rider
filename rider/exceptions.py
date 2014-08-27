
class Http404(Exception):
    def __init__(self, body=''):
        self.body = body

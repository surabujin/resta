# request.py


class _Request(object):
    def __init__(self, method, url):
        self.method = method.upper()
        self.headers = dict()
        self.url = url

    def emit(self, session):
        args = {
            'headers': self.headers}
        args.update(self._inject_body())
        session.request(self.method, self.url, **args)

    def _inject_body(self):
        raise NotImplementedError


class BodyLessRequest(_Request):
    def _inject_body(self):
        return {}


class JsonRequest(_Request):
    def __init__(self, method, url, payload=None):
        super().__init__(method, url)
        if payload is None:
            payload = dict()
        self.payload = payload

    def _inject_body(self):
        return {'json': self.payload}

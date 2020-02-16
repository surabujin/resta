# endpoint.py


class Endpoint(object):
    def __init__(self, base_url, session_provider, context):
        self.base_url = base_url
        self.session_provider = session_provider
        self.context = context

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def _handle(self, request):
        self._inject_headers(request)
        request.emit(self.session_provider())

    def _inject_headers(self, request):
        pass

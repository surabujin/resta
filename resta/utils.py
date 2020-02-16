# utils.py


class SessionProvider(object):
    def __call__(self):
        raise NotImplementedError


class ServiceSessionProvider(SessionProvider):
    def __init__(self, service):
        super().__init__()
        self.service = service

    def __call__(self):
        return self.service.get_http_session()

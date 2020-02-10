from pip import _internal  # NOQA: Needed to make the _vendor import works.
from pip._vendor.requests import Session, codes


class CompilationError(Exception):
    pass


class WheelsproxyClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = Session()

    def compile(self, requirements_in):
        r = self.session.post(
            self.base_url + "+compile/", data=requirements_in
        )
        if r.status_code == codes.bad_request:
            raise CompilationError(r.text)
        r.raise_for_status()
        return r.text

    def resolve(self, compiled_reqs):
        r = self.session.post(self.base_url + "+resolve/", data=compiled_reqs)
        r.raise_for_status()
        return r.text

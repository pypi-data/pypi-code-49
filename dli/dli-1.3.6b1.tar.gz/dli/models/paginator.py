from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock


class Paginator:

    def __init__(self, url, model,
         instantiation_method=None, instantiation_override=None,
         page=1, total_field=None
    ):
        self.page = page
        self.url = url
        self.model = model
        self.instantiation_factory = instantiation_method
        self.override = instantiation_override
        self.cache = []
        self.total_field = total_field
        self.lock = Lock()

    def _request(self, page=None):
        return self.model._client.session.get(
                self.url,
                params={
                    'page': self.page if not page else page,
                }
            ).json()

    def __iter__(self):
        if not self.cache:
            try:
                tp = ThreadPoolExecutor(max_workers=10)

                inst = self._request()
                if inst.get("entities", None):
                    # v1 route
                    key = "entities"
                    count = ("properties", "pages_count")
                else:
                    # v2 route
                    key = "data"
                    count = ("meta", "total_pages")

                def _get_and_instantiate(page):
                    inst = self._request(page)
                    self._iter_instance(inst, key)

                self._iter_instance(inst, key)

                total_pages = inst[count[0]][
                                  self.total_field if self.total_field
                                  else count[1]] + 1
                rng = range(2, total_pages)

                list(tp.map(_get_and_instantiate, rng))

            finally:
                tp.shutdown(wait=True)

        yield from self.cache

    def _iter_instance(self, inst, key):
        obj = inst if not key else inst[key]
        if key:
            obj = inst[key]

        # we use the __init__ method of the class unless
        # (or) provided instantiation method
        # ... useful to transform data first
        # (or) provided override to control cache insertion
        # ... useful to flatten multi-item

        if not self.override:
            for f in obj:
                if not self.instantiation_factory:
                    m = self.model(f)
                else:
                    m = self.instantiation_factory(f)

                with self.lock:
                    self.cache.append(m)
        else:
            self.override(obj, self.cache)
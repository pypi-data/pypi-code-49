import threading
from .utils import generate_random_id

# span_id parent_id flag


class Context(threading.local):
    """存各种 id"""
    candi = ["trace_id", "span_id", "parent_id"]

    def get_or_generate(self, k):
        if k not in self.candi:
            return 0
        v = getattr(self, k, 0)
        if not v:
            v = generate_random_id()
            setattr(self, k, v)
        return v


ctx = Context()

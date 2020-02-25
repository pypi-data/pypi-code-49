from contextlib import contextmanager
from functools import wraps
from ..database import init


@contextmanager
def new_session(db_pth):
    Session = init(db_pth)
    db = Session()
    try:
        yield db
    finally:
        db.close()


def db_session(func):
    @wraps(func)
    def _db_session(cfg, *args, **kwargs):
        with new_session(cfg.db_path) as db:
            cfg.db = db
            return func(cfg, *args, **kwargs)

    return _db_session

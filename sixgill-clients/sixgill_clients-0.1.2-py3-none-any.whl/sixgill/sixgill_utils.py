from typing import TypeVar, Callable, Iterable, Iterator, List, Dict, Any
import logging

T = TypeVar('T')


def streamify(batch_func: Callable[..., Iterable[T]]) -> Callable[..., Iterator[T]]:
    def streamify_wrapper(*args, **kwargs) -> Iterator[T]:
        batch = batch_func(*args, **kwargs)
        while batch:
            yield from batch
            batch = batch_func(*args, **kwargs)

    return streamify_wrapper


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]")
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def is_indicator(indicator):
    return "indicator" == indicator.get("type", "")

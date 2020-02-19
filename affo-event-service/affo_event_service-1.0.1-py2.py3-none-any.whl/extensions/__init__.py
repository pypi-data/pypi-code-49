from celery import Celery

from .clickhouse import ClickHouse

__all__ = ["celery"]

celery = Celery()
clickhouse = ClickHouse()

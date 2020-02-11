"""Provides TaskStatus class."""

from enum import Enum


class TaskStatus(Enum):
    """Represents the possible values for TaskStatus"""
    waiting = 'waiting'
    processing = 'processing'
    failed = 'failed'
    complete = 'complete'

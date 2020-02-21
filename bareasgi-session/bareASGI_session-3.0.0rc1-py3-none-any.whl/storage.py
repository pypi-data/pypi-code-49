"""Session Storage"""

from abc import ABCMeta, abstractmethod
from typing import Dict


class SessionStorage(metaclass=ABCMeta):
    """Session Storage"""

    @abstractmethod
    async def load(self, key: str) -> dict:
        """Load session data

        Args:
            key (str): The session key.

        Returns:
            dict: The session data.
        """

    @abstractmethod
    async def save(self, key: str, session: dict) -> None:
        """Save session data

        Args:
            key (str): The session key.
            session (dict): The session data.
        """


class MemorySessionStorage(SessionStorage):
    """Memory session storage"""

    def __init__(self) -> None:
        """Memory session storage"""
        self.sessions: Dict[str, dict] = {}

    async def load(self, key: str) -> dict:
        return self.sessions.setdefault(key, {})

    async def save(self, key: str, session: dict) -> None:
        self.sessions[key] = session

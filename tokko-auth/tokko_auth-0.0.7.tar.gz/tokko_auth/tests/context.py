from dataclasses import dataclass


@dataclass
class AuthHeader:
    token: str = None

    @property
    def authorization(self) -> dict:
        return {'Authorization': f'Bearer {self.token}'}


@dataclass
class Context:
    headers: dict = None

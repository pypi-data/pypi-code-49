import typing
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


@dataclass
class ScrapperData:
    topic: str
    candidate: typing.Any
    message: 'MessageData'
    actions: typing.Dict[str, typing.List['TaskData']] = field(default_factory=dict)
    auth_session: typing.Any = None
    error_message: str = None
    error_extra: dict = None
    is_valid: bool = True
    extra_config: dict = field(default_factory=dict)
    broadcast_variables: dict = field(default_factory=dict)


@dataclass
class TaskData:
    action: str
    fetched_data: typing.Any = None
    criteria: typing.Dict = field(default_factory=dict)


@dataclass()
class MessageData:
    message: dict
    created_at: str = None
    consumed_at: str = None
    scrap_started_at: str = None
    scrap_finished_at: str = None
    visibility_timeout_at: str = None

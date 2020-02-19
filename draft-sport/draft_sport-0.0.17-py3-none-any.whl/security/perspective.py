"""
Draft Sport Python
Perspective Module
author: hugh@blinkybeach.com
"""
from nozomi import Perspective as NozomiPerspective
from nozomi import Immutable
from typing import TypeVar, Type

T = TypeVar('T', bound='Perspective')


class Perspective(NozomiPerspective):

    def __init__(
        self,
        perspective_id: int,
        perspective_name: str
    ) -> None:

        self._perspective_id = perspective_id
        self._perspective_name = perspective_name

        return

    perspective_id = Immutable(lambda s: s._perspective_id)
    value = Immutable(lambda s: s._perspective_id)

    @classmethod
    def with_id(cls: Type[T], perspective_id: int) -> T:
        if perspective_id == Constants.ADMINISTRATOR.perspective_id:
            return Constants.ADMINISTRATOR
        if perspective_id == Constants.CUSTOMER.perspective_id:
            return Constants.CUSTOMER
        raise RuntimeError('Unknown Perspective ID')

    def __hash__(self) -> int:
        return hash(self._perspective_id)


class Constants:

    ADMINISTRATOR = Perspective(2, 'Administrator')
    CUSTOMER = Perspective(1, 'Customer')

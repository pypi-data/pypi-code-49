from typing import *
from royalnet.constellation.api import *
from royalnet.backpack.tables.users import User
from royalnet.utils import asyncify

async def find_user_api(input: Union[int, str], alchemy, session):
    if isinstance(input, int):
        user_id = input
    elif isinstance(input, str):
        try:
            user_id = int(input)
        except ValueError:
            raise InvalidParameterError(f"Invalid user id passed to {find_user_api.__name__}")
    else:
        raise TypeError(f"Invalid input type passed to {find_user_api.__name__}")
    user: User = await asyncify(session.query(alchemy.get(User)).get, user_id)
    if user is None:
        raise NotFoundError("No such user.")
    return user

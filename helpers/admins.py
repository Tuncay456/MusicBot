
from typing import List

from pyrogram.types import Chat, User

import cache.admins


async def get_administrators(chat: Chat) -> List[User]:
    get = cache.admins.get(chat.id)

    if get:
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [administrator.user.id for administrator in administrators]

    cache.admins.set(chat.id, to_set)

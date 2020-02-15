from typing import List, Optional

from pydantic import BaseModel, Field

from escarpolette.schemas.item import ItemSchemaOut


class PlayingItem(BaseModel):
    id: int = Field(..., description="The id of the item currently playing")
    position: int = Field(
        ..., description="The part, in seconds, of the item already played."
    )


class PlaylistSchemaOut(BaseModel):
    items: List[ItemSchemaOut] = []
    playing: PlayingItem = Field(
        None, description="Info about the current playing item"
    )

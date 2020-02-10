import logging

from fastapi import APIRouter, Depends, HTTPException

from escarpolette.player import State, get_player, Player
from escarpolette.schemas import PlayerSchema

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", response_model=PlayerSchema)
async def get(player: Player = Depends(get_player)) -> PlayerSchema:
    logger.debug("GET player state")
    data = PlayerSchema(state=player.get_state().name)
    return data


@router.patch("/", responses={400: {}})
async def patch(data: PlayerSchema, player: Player = Depends(get_player)) -> None:
    if data.state == State.PLAYING:
        await player.play()
    elif data.state == State.PAUSED:
        await player.pause()
    else:
        raise HTTPException(
            status_code=400, detail=f"The state {data.state} cannot be set"
        )

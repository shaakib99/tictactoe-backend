from fastapi import APIRouter
from fastapi import status

from __lib__.game.models import CreateGameModel, GameModel
from __lib__.utils import db_anotation
from .service import GameService

game_router = APIRouter()
game_router.prefix = '/games'

@game_router.post('/', response_model=GameModel, status_code=status.HTTP_201_CREATED)
async def create_game(data: CreateGameModel, db: db_anotation):
    game_service = GameService(db)
    return game_service.create_game(data)

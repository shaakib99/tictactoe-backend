from fastapi import APIRouter
from __lib__.game.models import CreateGameModel
from __lib__.utils import db_anotation
from .service import GameService

game_router = APIRouter()
game_router.prefix = '/games'

@game_router.post('/')
async def create_game(data: CreateGameModel, db: db_anotation):
    game_service = GameService(db)
    return game_service.create_game(data)

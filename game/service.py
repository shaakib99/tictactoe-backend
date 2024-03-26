from sqlalchemy.orm import Session
from __lib__.game.schema import GameSchema
from __lib__.game.models import  CreateGameModel, GameModel

class GameService:
    def __init__(self, db: Session):
        self.db = db

    def create_game(self, data: CreateGameModel):
        game = GameSchema(**data.model_dump())
        self.db.add(game)
        self.db.commit()
        return GameModel.model_validate(game)

    def update_game(self, id, data, user):
        pass

    def find_one(self, id):
        pass

    def find_all(self, query):
        pass

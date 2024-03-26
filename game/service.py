from sqlalchemy.orm import Session
from __lib__.game.schema import GameSchema


class GameService:
    def __init__(self, db: Session):
        self.db = db

    def create_game(self, data):
        return self.db.query(GameSchema).filter().all()

    def update_game(self, id, data, user):
        pass

    def find_one(self, id):
        pass

    def find_all(self, query):
        pass

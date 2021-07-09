from flask_sqlalchemy import SQLAlchemy


class BaseRepository:
    def __init__(self, db: SQLAlchemy) -> None:
        self._db = db

    def save(self, model):
        self._db.session.add(model)
        self._db.session.commit()

    def findOne(self, **kwags) -> object:
        raise NotImplementedError

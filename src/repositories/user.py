from flask_sqlalchemy import SQLAlchemy
from repositories.base import BaseRepository
from models.user import UserModel


class UserRepository:
    def __init__(self) -> None:
        pass

    def find(self, **kwags) -> list:
        return UserModel.query.filter_by(kwags).first()

    def findOne(self, **kwags) -> UserModel:
        return UserModel.query.filter_by(kwags).first()

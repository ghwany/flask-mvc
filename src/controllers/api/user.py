from typing import Container
from flask import request
from src.services.user import UserService
from . import bp, APIError
from dependency_injector.wiring import inject, Provide
from src.container import Container


@bp.route("/users", method=["GET"])
@inject
def get_users(service: UserService = Provide[Container.user_service]):
    return service.repository.find()

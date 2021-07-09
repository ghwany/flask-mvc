from dependency_injector import containers, providers
from flask_sqlalchemy import SQLAlchemy
import repositories as repositories
import services as services


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    user_repository = providers.Factory(repositories.UserRepository)

    user_service = providers.Factory(services.UserService, repository=user_repository)

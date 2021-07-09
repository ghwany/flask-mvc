from flask import Flask

from container import Container
from controllers import api
from models import db


def create_app() -> Flask:
    container = Container()
    container.config.from_ini(".env")
    container.wire(modules=[api])

    app = Flask(__name__)
    app.container = container
    app.register_blueprint(api.bp, url_prefix="/api")

    db.init_app(app)

    return app


app = create_app()
app.run("0.0.0.0", 5000)

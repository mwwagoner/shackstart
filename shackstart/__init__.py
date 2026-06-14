import os
from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_mapping(
            SECRET_KEY='Dev',
    )

    os.makedirs(app.instance_path, exist_ok=True)

    from .blueprints import index
    app.register_blueprint(index.bp)

    return app

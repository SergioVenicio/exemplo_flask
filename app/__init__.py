# -*- coding: utf-8 -*-

import models
from flask import Flask
from extensions import db
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    configure_blueprints(app)
    configure_extensions(app)
    configure_commands(app)
    return app


def configure_blueprints(app):
    from views import bp
    app.register_blueprint(bp)


def configure_extensions(app):
    db.init_app(app)


def configure_commands(app):
    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()

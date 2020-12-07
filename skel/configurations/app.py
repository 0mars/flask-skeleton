from flask import Flask, Blueprint

from skel.entrypoints.api import api
from skel.configurations.extensions import db, migrate, bcrypt, cors
from skel.entrypoints.api.health.endpoints import ns as health_namespace

import os


def create_app(testing=False, cli=False) -> Flask:
    """Application factory, used to create application
    """
    from skel.configurations.internal import app
    app.config.from_object(os.getenv('APP_SETTINGS', 'skel.configurations.server.config.Development'))
    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_extensions(flask_app, cli):
    """configure flask extensions
        """
    db.init_app(flask_app)

    cors.init_app(flask_app)
    db.app = flask_app

    bcrypt.init_app(flask_app)
    if cli is True:
        migrate.init_app(flask_app, db)


def register_blueprints(flask_app):
    """register all blueprints for application
    """
    blueprint = Blueprint('api', __name__, url_prefix='/v1')
    api.init_app(blueprint)
    api.add_namespace(health_namespace)
    if blueprint.name not in flask_app.blueprints.keys():
        flask_app.register_blueprint(blueprint)
    else:
        flask_app.blueprints[blueprint.name] = blueprint


def main():
    app = create_app(False, True)

    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    @app.route("/all-routes")
    def all_routes():
        from flask import url_for, make_response, jsonify
        links = []
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
        return make_response((jsonify(links), 200))

    app.run(host='0.0.0.0', port=8888)
    return app


if __name__ == '__main__':
    app = main()

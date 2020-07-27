import logging
from typing import Any

from flask import request, make_response, jsonify
from flask_restx import Resource

from skel.entrypoints.api import api

log = logging.getLogger(__name__)

ns = api.namespace('health', description='Health Check')


@ns.route('/healthcheck', strict_slashes=False)
class Health(Resource):
    def get(self) -> Any:
        """
            Checks health of the app
        """
        return make_response((jsonify({
            "status": "success",
            "message": "",
        }), 200))

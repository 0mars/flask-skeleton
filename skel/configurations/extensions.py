"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from jwt import PyJWT

from skel.configurations.logger import log

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
cors = CORS(resources={r"/v1/*": {"origins": "*"}})
log.debug("in debug mode")
pwd_context = bcrypt
jwt = PyJWT()
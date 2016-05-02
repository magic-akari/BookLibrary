import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from flask.ext.pagedown import PageDown
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)
bootstrap = Bootstrap(app)
pagedown = PageDown(app)
avatars = UploadSet('avatars', IMAGES)
configure_uploads(app, avatars)

from app.main import main, auth, user, book, comment, log
from app.api import api_bp

for blueprint in [main, auth, user, book, comment, log, api_bp]:
    app.register_blueprint(blueprint)

from app import models

exists_db = os.path.isfile(app.config['DATABASE'])
if not exists_db:
    import db_fill

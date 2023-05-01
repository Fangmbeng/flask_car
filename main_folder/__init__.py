from flask import Flask
from config import Config
from main_folder.api.routes import api
from main_folder.site.routes import site
from main_folder.authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
app.config['TESTING'] = True
CORS(app)
    
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)


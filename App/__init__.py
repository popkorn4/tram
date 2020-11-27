from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB':'shop'}
app.config["SECRET_KEY"] = "secret"
app.config['SESSION_COOKIE_NAME'] = 'login-session'
db = MongoEngine(app)
from .profile import profile as profile_blueprint
app.register_blueprint(profile_blueprint)
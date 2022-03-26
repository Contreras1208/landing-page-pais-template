from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from utils.db import db

# importo los blueprints
from routes.site import site
from routes.messages import messages

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints

app.register_blueprint(site)

app.register_blueprint(messages)


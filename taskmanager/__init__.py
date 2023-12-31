import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)
app.config["SECRECT_KEY"] = os.environ.get("SECRECT_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


db = SQLAlchemy(app)

#ADDED BY ME
app.app_context().push()

from taskmanager import routes # noqa
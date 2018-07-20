from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from . tasks import make_celery

app = Flask(__name__)

app.config.from_object(Config)
app.config.update(
CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379')
celery = make_celery(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
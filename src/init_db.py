from app import appSheduler
from src.model.ShedulerModel import db

with appSheduler.app_context():
      db.create_all()
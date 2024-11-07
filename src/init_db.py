from app import appSheduler
from model.BookingTimeModel import db

with appSheduler.app_context():
      db.create_all()
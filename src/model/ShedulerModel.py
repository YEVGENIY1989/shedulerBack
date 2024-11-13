from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookingTimeModel(db.Model):
    __tablename__ = 'bookingTime'
    id = db.Column(db.Integer, primary_key=True) 
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    summary = db.Column(db.String)
    description = db.Column(db.String)
    def __init__(self, start, end, summary, description):
        self.start = start
        self.end = end
        self.summary = summary
        self.description = description


class Booking(db.Model):
    __tablename__ = 'bokking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)        
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
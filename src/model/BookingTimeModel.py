from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookingTimeModel(db.Model):
    __tablename__ = 'bookingTime'
    id = db.Column(db.Integer, primary_key=True) 
    start = db.Column(db.String)
    end = db.Column(db.String)
    summary = db.Column(db.String)
    description = db.Column(db.String)
    def __init__(self, start, end, summary, description):
        self.start = start
        self.end = end
        self.summary = summary
        self.description = description

    def __str__(self):
        return self.start + " " + self.end + " " + self.summary + " " + self.description    
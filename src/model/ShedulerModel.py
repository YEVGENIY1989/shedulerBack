from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_massages = db.Table('user_massages',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('massage_id', db.Integer, db.ForeignKey('massage.id'))
)

class BookingTimeModel(db.Model):
    __tablename__ = 'bookingTime'
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    summary = db.Column(db.String)
    description = db.Column(db.String)
    def __init__(self, start = None, end = None, summary = None, description = None):
        self.start = start
        self.end = end
        self.summary = summary
        self.description = description

    
    def as_dict(self):
        return {
            'description': self.description,
            'id': self.id,
            'summary': self.summary,
            'start': self.start,
            'end': self.end
        }    

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    massages = db.relationship('Massage', secondary=user_massages, back_populates='users')
    def __init__(self, name = None,  phone = None):
        self.name = name
        self.phone = phone

    def as_dict(self):
        return {
            'name': self.name,
            'phone': self.phone
        }

class Massage(db.Model):
    __tablename__ = 'massage'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    name_of_procedure = db.Column(db.String)
    price = db.Column(db.Integer)
    users = db.relationship('User', secondary=user_massages, back_populates='massages')
    def __init__(self, id = None, duration = None, name_of_procedure = None, price = None):
        self.id = id
        self.duration = duration
        self.name_of_procedure = name_of_procedure
        self.price = price

    def as_dict(self):
        return {
            'duration': self.duration,
            'name_of_procedure': self.name_of_procedure,
            'price': self.price
    }


class Booking(db.Model):
    __tablename__ = 'bokking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)        
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    


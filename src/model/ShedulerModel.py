from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    telephone = db.Column(db.String)
    def __init__(self, full_name = None, email = None, telephone = None):
        self.full_name = full_name
        self.email = email        
        self.telephone = telephone

    def as_dict(self):
        return {
            'full_name': self.full_name,
            'email': self.email,
            'telephone': self.telephone
        }

class Booking(db.Model):
    __tablename__ = 'bokking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)        
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class TypeOfProcedure(db.Model):
    __tablename__ = 'type_of_procedure'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    name_of_procedure = db.Column(db.String)
    price = db.Column(db.Integer)
    def __init__(self, duration, name_of_procedure, price):
        self.duration = duration
        self.name_of_procedure = name_of_procedure
        self.price = price    
    

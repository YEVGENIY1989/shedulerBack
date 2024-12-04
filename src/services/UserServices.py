from model.ShedulerModel import User
from flask import jsonify
class UserServices:

    def find_user(self, phone):
        user = User.query.filter_by(phone=phone).first()
        return user
    
    def registration(self, name, phone, db):

        user = self.find_user(phone)

        if user:
            return jsonify({'user_id': user.id, 'Exist': True})

        new_user = User(name=name, phone=phone)
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(phone=phone).first()
        return jsonify({'user_id': user.id, 'Exist': False})
    
    def find_user(self, phone):
        user = User.query.filter_by(phone=phone).first()
        return user

from flask import jsonify
from model.ShedulerModel import Massage


class HandlingServiceMassage:

    def add_to_typeOfProcedure(self, typeOfProcedure, db):
        db.session.add(typeOfProcedure)
        db.session.commit()
        return "success"
    
    def get_all_typeOfProcedure(self, db):
        listTypeOfProcedure = Massage.query.all()
        jsonFormat = jsonify([record.as_dict() for record in listTypeOfProcedure])
        return jsonFormat
    
    def update_typeOfProcedure(self, id, db, typeOfProcedure):
        Massage.query.filter_by(id = id).update(typeOfProcedure.as_dict())
        db.session.commit()
        return "success"
    
    def delete_typeOfProcedure(self, id, db):
        Massage.query.filter_by(id=id).delete()
        db.session.commit()
        return "success"
    
    def get_typeOfProcedure_by_id(self, id, db):
        typeOfProcedure = Massage.query.filter_by(id=id).first()

        return typeOfProcedure.as_dict()
    
    def test():
        return "success"
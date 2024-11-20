
from flask import jsonify
from model.ShedulerModel import BookingTimeModel


class BookingTimeServices:

        
    def add_to_bookingResponse(self, bookingTimeResponse, db):
        db.session.add(bookingTimeResponse)
        db.session.commit()
        return "success"
    
    def get_all_bookingResponse(self, db, start, end):
        listShedulerTime = BookingTimeModel.query.filter(BookingTimeModel.start.between(start, end))
        jsonFormat = jsonify([record.as_dict() for record in listShedulerTime])
        return jsonFormat
    
    def delete_from_bookingResponse(self, id, db):
        BookingTimeModel.query.filter_by(id=id).delete()
        db.session.commit()
        return "success"
    
    def update_from_bookingResponse(self, id, db, bookinTimeModel):
        BookingTimeModel.query.filter_by(id=id).update(bookinTimeModel)
        db.session.commit()
        return "success"
    
    def find_by_id(self, id, db):
        return BookingTimeModel.query.filter_by(id=id).first()
    

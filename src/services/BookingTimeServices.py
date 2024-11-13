
from model.ShedulerModel import BookingTimeModel


class BookingTimeServices:

        
    def add_to_bookingResponse(self, bookingTimeResponse, db):
        db.session.add(bookingTimeResponse)
        db.session.commit()
        return "s"
    
    def get_all_bookingResponse(self, db, start, end):
        # listShedulerTime = db.session.query(BookingTimeModel).filter(BookingTimeModel.start.between(start, end))
        listShedulerTime = BookingTimeModel.query.filter(BookingTimeModel.start.between(start, end)).all()
        for sheduler in listShedulerTime:
            print(sheduler.description + " " + sheduler.id)
        return listShedulerTime

from model.ShedulerModel import BookingTimeModel


class BookingTimeServices:

        
    def add_to_bookingResponse(self, bookingTimeResponse, db):
        db.session.add(bookingTimeResponse)
        db.session.commit()
        return "s"
    
    def get_all_bookingResponse(self, db):
        btm = 0
        print(btm)
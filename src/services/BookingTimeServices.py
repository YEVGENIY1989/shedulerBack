

class BookingTimeServices:

        
    def add_to_bookingResponse(self, bookingTimeResponse, db):
        db.session.add(bookingTimeResponse)
        db.session.commit()
        return "s"
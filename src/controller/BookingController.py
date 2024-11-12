
from flask import request
from flask import Response
from flask.blueprints import Blueprint
from model.ShedulerModel import BookingTimeModel, db
from services.BookingTimeServices import BookingTimeServices
import json


booking = Blueprint('BookingController', __name__)
@booking.route('/booking', methods=['POST'])
def bookingTimePost():
    temp = json.loads(request.data)
    booking = BookingTimeModel(**temp)
    bookingTime = BookingTimeServices() 
    bookingTime.add_to_bookingResponse(booking, db)
    return Response("success", status=200)

# приходит json start - end промежуток времени
@booking.route('/getAllBooking', methods=['POST'])
def getAllBooking():
    step_time = request.json
    print(step_time)
    return Response("success", status=200)
    # bookingTime = BookingTimeServices() 
    # return Response(bookingTime.get_all_bookingResponse(db), status=200)

@booking.route('/test', methods=['GET'])
def test():
    return Response("success", status=200)
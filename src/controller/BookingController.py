
from flask import request
from flask.blueprints import Blueprint
from model.BookingTimeModel import BookingTimeModel, db
from services.BookingTimeServices import BookingTimeServices
import json


booking = Blueprint('BookingController', __name__)

# @booking.route('/booking', methods=['GET'])
# def booking():
#     # booking = BookingTimeModel("10:00", "11:00", "test", "test")
#     # bookingTime = BookingTimeServices()
#     # bookingTime.add_to_bookingResponse(booking, db)
#     return "created booking"

@booking.route('/', methods=['GET'])
def test():
    return 'success'

@booking.route('/booking', methods=['GET'])
def bookingTime():
    booking = BookingTimeModel("10:00", "11:00", "test", "test")
    bookingTime = BookingTimeServices()
    bookingTime.add_to_bookingResponse(booking, db)
    return 'success2'

@booking.route('/booking', methods=['POST'])
def bookingTimePost():
    temp = json.loads(request.data)
    booking = BookingTimeModel(**temp)
    bookingTime = BookingTimeServices()
    bookingTime.add_to_bookingResponse(booking, db)
    return "success"
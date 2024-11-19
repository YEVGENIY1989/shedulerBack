
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
    start = step_time['start']
    end = step_time['end']
    bookingTime = BookingTimeServices()
    shedulerTime = bookingTime.get_all_bookingResponse(db, start, end)
    return shedulerTime, 200

@booking.route('/deleteBooking', methods=['GET'])
def deleteBooking():
    id = request.args.get('id')
    bookingTime = BookingTimeServices()
    bookingTime.delete_from_bookingResponse(id, db)
    return Response("success", status=200)

@booking.route('/updateBooking', methods=['POST'])
def updateBooking():
    temp = json.loads(request.data)
    id = request.args.get('id')
    booking = BookingTimeModel(**temp)
    bookingTime = BookingTimeServices() 
    bookingTime.update_from_bookingResponse(id, db, booking)
    return Response("success", status=200)

@booking.route('/test', methods=['GET'])
def test():
    return Response("success", status=200)
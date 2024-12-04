
# 1) 
# 2) Метод проверки/регистрации -> Ввел имя + телефон  ->  идет в итерфейс бронирования и возвращаем id если есть, если нет, регистрируем и возвращаем id /registration
# 2) запрос на свободные окна, присылается id, ищу свободные на две недели вперед и возврашаю список {date : день, time:[10, 12], start: время, end : время} - со скольки , до скольки работаем


from flask import request
from flask import Response
from flask.blueprints import Blueprint
from model.ShedulerModel import BookingTimeModel, db, User
from services.BookingTimeServices import BookingTimeServices
from services.UserServices import UserServices
import json


user = Blueprint('UserController', __name__)

# {
#     "name": "name",
#     "phone": "phone"
# }
@user.route('/registration', methods=['POST'])
def registration():
    temp = json.loads(request.data)
    user = User(**temp)
    userService = UserServices()
    response = userService.registration(user.name, user.phone, db)
    return response, 200


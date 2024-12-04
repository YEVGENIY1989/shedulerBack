# 0) Метод по добавлению массажей (body) (Интерфейс Маши в serviceController)
# 1) Метод получение списка
# 2) метод получение свободных окон по id выбраной услуги

import json
from flask import Blueprint, Response, request

from model.ShedulerModel import Massage, db
from services.HandlingServiceMassage import HandlingServiceMassage


service = Blueprint('ServiceController', __name__)


@service.route('/service/test', methods=['GET'])
def test():
  
    return Response("success", status=200)

# функция для мастера, для добавления услуги(в нашем случаи массажа)
@service.route('/service/addTypeOfService', methods=['POST'])
def addTypeOfService():
    temp = json.loads(request.data)
    service = Massage(**temp)
    handlingService = HandlingServiceMassage() 
    handlingService.add_to_typeOfProcedure(service, db)
    return Response("success", status=200)

@service.route('/service/updateTypeOfService', methods=['POST'])
def updateTypeOfService():
    temp = json.loads(request.data)
    id = request.args.get('id')
    typeOfProcedure = Massage(**temp)
    handlingService = HandlingServiceMassage() 
    handlingService.update_typeOfProcedure(id, db, typeOfProcedure)
    return Response("success", status=200)

@service.route('/service/deleteTypeOfService', methods=['GET'])
def deleteTypeOfService():
    id = request.args.get('id')
    handlingService = HandlingServiceMassage() 
    handlingService.delete_typeOfProcedure(id, db)
    return Response("success", status=200)

@service.route('/service/getTypeOfServiceById', methods=['GET'])
def getTypeOfServiceById():
    id = request.args.get('id')
    handlingService = HandlingServiceMassage() 
    typeOfProcedure = handlingService.get_typeOfProcedure_by_id(id, db)
    return typeOfProcedure, 200

#для клиента получение всех услуг и продолжительность
@service.route('/service/getAllTypeOfService', methods=['GET'])
def getAllTypeOfService():
    handlingService = HandlingServiceMassage() 
    return handlingService.get_all_typeOfProcedure(db), 200

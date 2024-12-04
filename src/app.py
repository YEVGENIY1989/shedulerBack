from flask import Flask
from controller.BookingController import booking
from controller.ServiceController import service
from controller.UserController import user
from model.ShedulerModel import db

def setupApp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:89052809585Leti@localhost:5432/postgres'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(booking)
    app.register_blueprint(service)
    app.register_blueprint(user)
    return app


if __name__ == '__main__':
    appSheduler = setupApp()
    with appSheduler.app_context():
        db.create_all()
    appSheduler.run(debug=True)
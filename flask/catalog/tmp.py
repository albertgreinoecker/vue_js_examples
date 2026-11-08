from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, Text, Float, DateTime, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS, cross_origin
from dataclasses import dataclass
import json

engine = create_engine('sqlite:///users.db')  # sqlite
Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property()  # Dadurch hat jedes Base - Objekt (also auch ein User) ein Attribut query für Abfragen

app = Flask(__name__) #Die Flask Anwendung
cors = CORS(app, origins=["http://localhost:5173"]) # CORS: nur von dieser Origin (Vite-Dev-Server) aus darf zugegriffen werden
api = Api(app) #Die API


@dataclass  # Dieser Decorator ermöglicht das Schreiben als JSON mit jsonify
class User(Base):
    __tablename__ = 'users'
    id: int
    name: str
    rfid: str
    motorwert: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    rfid = Column(Text)
    motorwert = Column(Integer)


# Definition eines Parsers, um die POST-Daten zu verarbeiten
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('rfid', type=str, required=True)
user_parser.add_argument('motorwert', type=int, required=True)


# für mehrere User
class UserList(Resource):
    def get(self):
        users = User.query.all()
        if users:
            return jsonify(users)
        else:
            abort(404, message=f"There are no Users in the database")


# für einen User
class UserService(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return jsonify(user)
        else:
            abort(404, message=f"User with id {id} not found")

    def put(self, id):
        data = request.get_json(force=True)['info']
        if data:
            info = User(name=data['name'], rfid=data['rfid'], motorwert=data['motorwert'])
            db_session.add(info)
            db_session.commit()
            return jsonify(info)
        else:
            abort(404, message=f"Post request does not work")

    def patch(self, id):
        data = User.query.get(id)
        if data:
            name = request.json['params']['name'].replace("\n", "")
            rfid = request.json['params']['rfid'].replace("\n", "")
            motorwert = request.json['params']['motorwert']
            data.name = name
            data.rfid = rfid
            data.motorwert = motorwert
            db_session.commit()
            return jsonify(data)
        else:
            abort(404, message=f"User with id {id} not found")

    def delete(self, id):
        user = User.query.get(id)
        if user:
            db_session.delete(user)
            db_session.commit()
            return jsonify({'message': f"User with id {id} deleted"})
        else:
            abort(404, message=f"User with id {id} not found")


# nur User mit der richtigen RFID
class RFID(Resource):
    def get(self, rfid):
        user = User.query.filter(User.rfid == rfid).all()
        if user:
            return jsonify(user)
        else:
            abort(404, message=f"User with rfid {rfid} not found")


# @app.route("/registration", method="POST") # damit wird angegeben, unter welchen Web-Adressen die darunterliegende Methode aufgerufen wird (ist ein Decorator)
# def registration():
#     return None
#
#
# @app.route("/login", method="POST")
# def login():
#     return None


# Registrierung der RESTful-API-Routen
api.add_resource(UserList, '/users')
api.add_resource(UserService, '/user/<int:id>')
api.add_resource(RFID, '/rfid/<string:rfid>')



@app.teardown_appcontext  # gibt die DB-Session nach jedem Request frei (nicht erst beim Beenden des Servers)
def shutdown_session(exception=None):
    print("Remove DB session")
    db_session.remove()


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(host='0.0.0.0', port=8080, debug=True)
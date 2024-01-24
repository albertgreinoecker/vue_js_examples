from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, Text, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS, cross_origin
from dataclasses import dataclass
import json

engine = create_engine('sqlite:///users.db')  # sqlite
Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

#Session = sessionmaker(bind=engine)
#session = Session()

db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property()  # Dadurch hat jedes Base - Objekt (also auch ein GeoInfo) ein Attribut query für Abfragen

app = Flask(__name__) #Die Flask Anwendung
cors = CORS(app, origins=["http://localhost:5173"]) #Cors,ohne den origins Verweis darf ich nicht von der Website aus zugreifen
api = Api(app) #Die API


@dataclass  # Diese ermoeglicht das Schreiben als JSON mit jsonify
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
user_parser.add_argument('motorwert', type=str, required=True)


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
            #linfo = session.merge(info)
            db_session.add(info)
            #session.commit()
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
            ldata = session.merge(data)
            session.add(ldata)
            session.commit()
        else:
            abort(404, message=f"User with id {id} not found")

    def delete(self, id):
        user = User.query.get(id)
        if user:
            luser = session.merge(user)
            session.delete(luser)
            session.commit()
            return jsonify({'message': f"User with id {id} deleted"})
        else:
            abort(404, message=f"User with id {id} not found")


# nur ein user mit der richtigen rfid (muigg)
class RFID(Resource):
    def get(self, rfid):
        user = User.query.filter(User.rfid == rfid).all()
        if user:
            return jsonify(user)
        else:
            abort(404, message=f"User with rfid {rfid} not found")


# @app.route("/registration", method="POST") # damit wird angegeben unter welchen web-addressen die darunterliegende methode aufgerufen wird (ist ein decorator)
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



@app.teardown_appcontext  # schließt datenbank connection, wenn server geschlossen wird
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()


if __name__ == '__main__':
    Base().metadata.create_all(bind=engine)
    app.run(host='0.0.0.0', port=8080, debug=True)
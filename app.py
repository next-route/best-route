from flask import Flask, Response, app, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

from sqlalchemy.orm import exc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rota_mySQL_1509@localhost:3306/melhor_rota'

db = SQLAlchemy(app)


class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    location = db.Column(db.String(50))

    def to_json(self):
        return{"id": self.id, "status": self.status, "location": self.location}

# select all


@app.route("/trucks", methods=['GET'])
def get_trucks():
    trucks_object = Truck.query.all()
    trucks_json = [truck.to_json() for truck in trucks_object]

    return generate_response(200, "trucks", trucks_json)


def generate_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if(message):
        body["message"] = message
    return Response(json.dumps(body), status=status, mimetype="application/json")

# select one


@app.route("/truck/<id>", methods=['GET'])
def get_truck(id):
    truck_object = Truck.query.filter_by(id=id).first()
    truck_json = truck_object.to_json()

    return generate_response(200, "truck", truck_json)

# register truck


@app.route("/truck", methods=["POST"])
def create_truck():
    body = request.get_json()

    try:
        truck = Truck(status=body["status"], location=body["location"])
        db.session.add(truck)
        db.session.commit()
        return generate_response(201, "truck", truck.to_json(), "Truck created with success.")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "truck", {}, "Error creating truck")

# update truck


@app.route("/truck/<id>", methods=["PUT"])
def update_truck(id):
    truck_object = Truck.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if("status" in body):
            truck_object.status = body["status"]
        if("location" in body):
            truck_object.location = body["location"]

        db.session.add(truck_object)
        db.session.commit()
        return generate_response(200, "truck", truck_object.to_json(), "Truck updated with success")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "truck", {}, "Error updating truck")

# delete truck


@app.route("/truck/<id>", methods=["DELETE"])
def delete_truck(id):
    truck_object = Truck.query.filter_by(id=id).first()

    try:
        db.session.delete(truck_object)
        db.session.commit()
        return generate_response(200, "truck", truck_object.to_json(), "Truck deleted with success")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "truck", {}, "Error deleting truck")


app.run()

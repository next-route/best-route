from flask import Flask, Response, app, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

from networkx.algorithms.operators.binary import disjoint_union
import dijkstra as dk

from sqlalchemy.orm import exc

# Inicializa o Flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Modificar "host", "senha" e "0000" pelas informações correspondentes no seu mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/melhor_rota'

# Conecta o Flask ao db(database) através da instância SLQAlchemy
db = SQLAlchemy(app)

# Cria a classe Truck e declara as variáveis como colunas no banco de dados


class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    location = db.Column(db.String(50))
    destination = db.Column(db.String(50))

    # retorna os valores das variáveis em formato json
    def to_json(self):
        return{"id": self.id, "status": self.status, "location": self.location, "destination": self.destination}

# seleciona todos os trucks cadastrados


@app.route("/trucks", methods=['GET'])
def get_trucks():
    # variável que chama todos os atributos da classe truck
    trucks_object = Truck.query.all()
    # trandforma em json
    trucks_json = [truck.to_json() for truck in trucks_object]

    return generate_response(200, "trucks", trucks_json)

# gera a resposta ao método http(GET, POST, PUT e DELETE)


def generate_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if(message):
        body["message"] = message
    return Response(json.dumps(body), status=status, mimetype="application/json")

# Seleciona apenas um truck pelo seu id


@app.route("/truck/<id>", methods=['GET'])
def get_truck(id):
    truck_object = Truck.query.filter_by(id=id).first()
    truck_json = truck_object.to_json()
    

    return generate_response(200, "truck", truck_json)

# Seleciona apenas um path para truck pelo seu id
# Returns info about the path for the truck id

@app.route("/path/<id>", methods=['GET'])
def get_path(id):
    truck_object = Truck.query.filter_by(id=id).first()
    status = truck_object.status
    location = truck_object.location
    path = dk.path(status,location)
    path_json = json.dumps(path)

    return generate_response(200, "path", path_json)

# cadastra um truck colocando o status, localização e destino (id é autoincrementável)


@app.route("/truck", methods=["POST"])
def create_truck():
    # faz requisição em json dos valores informados pelo usuário
    body = request.get_json()

    try:
        truck = Truck(
            status=body["status"], location=body["location"], destination=body["destination"])
        # adiciona os valores informados no banco de dados
        db.session.add(truck)
        db.session.commit()
        return generate_response(201, "truck", truck.to_json(), "Truck created with success.")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "truck", {}, "Error creating truck")

# faz update de um truck, especificado pelo id


@app.route("/truck/<id>", methods=["PUT"])
def update_truck(id):
    truck_object = Truck.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        # se, por exemplo, no body(valores informados) tenha status e localização, apenas esses valores serão modificados.
        if("status" in body):
            truck_object.status = body["status"]
        if("location" in body):
            truck_object.location = body["location"]
        if("destination" in body):
            truck_object.destination = body["destination"]

        db.session.add(truck_object)
        db.session.commit()
        return generate_response(200, "truck", truck_object.to_json(), "Truck updated with success")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "truck", {}, "Error updating truck")

# deleta um truck de acordo com o id


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

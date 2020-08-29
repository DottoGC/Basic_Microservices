from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import requests
import json

app = Flask(__name__)
api = Api(app)


class Pedido(Resource):
    pedidoCliente= ''
    cliente= ''
    direccion= ''
    telefono= ''
    estado= ''

    def get(self):
        data = {
            'Pedido': Pedido.pedidoCliente,
            'Cliente': Pedido.cliente,
            'estado': Pedido.estado
        }
        print('Enviando estado de pedido al cliente')
        return jsonify(data)


    def post(self):     
        Pedido.pedidoCliente = request.json['Pedido']   
        Pedido.cliente = request.json['Cliente']
        Pedido.direccion = request.json['Direccion']
        Pedido.telefono = request.json['Telefono']
        Pedido.estado = request.json['Estado']


        endpoint = "http://localhost:5001/repartidor"
        data = {
        "Pedido" : "Quesohamburguesa Doble",
        "Cliente" :"Otto Guarchaj",
        "Direccion" : "Zona 8 Mixco"
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(endpoint, data=json.dumps(data),headers=headers)


        print('Nuevo pedido realizado')
        return {'status': 'Nuevo pedido realizado.'}


api.add_resource(Pedido, '/pedidos')  # Route_1


if __name__ == '__main__':
     app.run(port='5000')
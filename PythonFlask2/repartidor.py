from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)


class Repartidor(Resource):
    repartidor= 'Goku Super Sayajin'
    estado= 'En camino'

    def get(self):
        data = {
            'estado': Repartidor.estado
        }

        print('Enviando estado del repartidor al cliente')
        return jsonify(data)


    def post(self):     
        Pedido.pedidoCliente = request.json['Pedido']   
        Pedido.cliente = request.json['Cliente']
        Pedido.direccion = request.json['Direccion']
        Pedido.telefono = request.json['Telefono']
        Pedido.estado = request.json['Estado']
        
        
        print('Nuevo pedido realizado')
        return {'status': 'Nuevo pedido realizado.'}


api.add_resource(Repartidor, '/repartidor')  # Route_1


if __name__ == '__main__':
     app.run(port='5001')
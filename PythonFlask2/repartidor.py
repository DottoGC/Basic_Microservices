from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)


class Repartidor(Resource):
    repartidor= 'Goku Super Sayajin'
    estado= 'En camino'
    pedidoCliente= ''
    direccion= ''
    cliente= ''

    def get(self):
        data = {
            'repartidor': Repartidor.repartidor,
            'estado': Repartidor.estado
        }

        print('Enviando estado del repartidor al cliente')
        return jsonify(data)


    def post(self):     
        Repartidor.pedidoCliente = request.json['Pedido']   
        Repartidor.cliente = request.json['Cliente']
        Repartidor.direccion = request.json['Direccion']        
        
        print('Nueva solicitud de entrega de Restaurante')
        return {'status': 'Nuevo solicitd de entrega de pedido realizada.'}


api.add_resource(Repartidor, '/repartidor')  # Route_1


if __name__ == '__main__':
     app.run(port='5001')
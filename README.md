# Práctica # 4: Orquestacion de servicios, usando un ESB
# Laboratorio de Software Avanzado


# ESB - API RESTful en NodeJs
	Intermediario entre la comunicacion entre los 3 microservicios

# 3 microservicios:
# Cliente - API RESTful en Golang
	Solicitar pedido al restaurante
    Verificar estado del pedido al restaurante
    Verificar estado del pedido al repartidor

    Comando para ejecutar microservicios:
    > go run archivo.go

# Restaurante - API RESTful en Python
    Recibir pedido del cliente
    Informar estado del pedido al cliente
    Avisar al repartidor que ya está listo el pedido

    Comando para ejecutar microservicios:
    > python archivo.py

# Repartidor - API RESTful en Python
    Recibir pedido del restaurante
    Informar estado del pedido al cliente
    Marcar como entregado

	Comando para ejecutar microservicios:
    > python archivo.py

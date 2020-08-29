package main

import (
  "fmt"
  "io/ioutil"
  "log"
  "net/http"
  "encoding/json"
  "bytes"
)

type PedidoCliente struct {
	Pedido string `json:"Pedido"`
	Cliente string `json:"Cliente"`
	Direccion string `json:"Direccion"`
	Telefono string `json:"Telefono"`
	Estado string `json:"Estado"`
}


func httpExamplePostJson() {
	fmt.Println("--- Solicitando pedido al restaurante ---")

	body := &PedidoCliente{
         Pedido : "Pizza Pepperonni",
         Cliente:"Otto Guarchaj",
         Direccion: "Zona 8 Mixco",
         Telefono: "46638340",
         Estado: "Iniciado",
	}


	pedidoJson, err := json.Marshal(body)
	if err != nil {
		log.Fatalln(err)
	}

	resp, err := http.Post("http://localhost:5000/pedidos", "application/json", bytes.NewBuffer(pedidoJson))
	if err != nil {
		log.Fatalln(err)
	}

	data, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(data))
}

func main() {
	httpExamplePostJson()
}
# -*- coding: utf-8 -*-

# Dispositivo 2
# Dados: Sensor de luz

import paho.mqtt.client as mqtt
import random
import json
import time

def generate_random_data():
    luminosidade = random.uniform(-200, 1000)
    return [
        {
            "variable": "luminosidade",
            "value": luminosidade,
            "metadata": {
                "mqtt_topic": "device2"
            }
        },
    ]

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)

    while True:
        data = generate_random_data()

        # Tratamento dispositivo
        if(data[0]["value"] < 0):
            print(f"Valor da luminosidade negativo: {data[0]['value']}")
        else:
            mensagem = json.dumps(data)
            # Publica os dados no tópico "device1"
            client.publish("device2", mensagem)
            print(f"Dados enviados para o tópico 'device2': {mensagem}")

        
        print("\n")
        # Aguarda 10 segundos antes de enviar o próximo conjunto de dados
        time.sleep(5)
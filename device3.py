# -*- coding: utf-8 -*-

# Dispositivo 3
# Dados: Sensor de pressão

import paho.mqtt.client as mqtt
import random
import json
import time

def generate_random_data():
    pressao = random.uniform(0, 1500)
    return [
        {
            "variable": "pressao",
            "value": pressao,
            "metadata": {
                "mqtt_topic": "device3"
            }
        },
    ]

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)

    while True:
        data = generate_random_data()

        # Tratamento dispositivo
        if(data[0]["value"] > 1000):
            print(f"Valor da pressão muito alto: {data[0]['value']}")
        else:
            mensagem = json.dumps(data)
            # Publica os dados no tópico "device1"
            client.publish("device3", mensagem)
            print(f"Dados enviados para o tópico 'device3': {mensagem}")

        
        print("\n")
        # Aguarda 10 segundos antes de enviar o próximo conjunto de dados
        time.sleep(5)
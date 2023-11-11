# -*- coding: utf-8 -*-

# Dispositivo 1
# Dados: Temperatura e umidade

import paho.mqtt.client as mqtt
import random
import json
import time

def generate_random_data():
    temperatura = random.uniform(17, 45)
    umidade = random.uniform(20, 60)
    return [
        {
            "variable": "temperatura",
            "value": temperatura,
            "metadata": {
                "mqtt_topic": "device1"
            }
        },
        {
            "variable": "umidade",
            "value": umidade,
            "metadata": {
                "mqtt_topic": "device1"
            }
        }
    ]

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)

    while True:
        data = generate_random_data()

        # Tratamento dispositivo
        if(data[0]["value"] > 38):
            print(f"Valor de temperatura muito grande: {data[0]['value']}")
        else:
            mensagem = json.dumps(data)
            # Publica os dados no tópico "device1"
            client.publish("device1", mensagem)
            print(f"Dados enviados para o tópico 'device1': {mensagem}")

        
        print("\n")
        # Aguarda 10 segundos antes de enviar o próximo conjunto de dados
        time.sleep(5)
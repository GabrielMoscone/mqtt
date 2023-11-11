# -*- coding: utf-8 -*-

# Dispositivo 4
# Dados: Qualidade ar

import paho.mqtt.client as mqtt
import random
import json
import time

def generate_random_data():
    ar = random.uniform(0, 1000)
    qualidade = "ruim"
    if (ar > 700):
        qualidade = "boa"
    

    if(ar < 200):
        qualidade = "invalida"
    

    return [
        {
            "variable": "qualidade",
            "value": qualidade,
            "metadata": {
                "mqtt_topic": "device4"
            }
        },
    ]

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)

    while True:
        data = generate_random_data()

        # Tratamento dispositivo
        if(data[0]["value"] == 'invalida'):
            print(f"Valor do ar inválido: {data[0]['value']}")
        else:
            mensagem = json.dumps(data)
            # Publica os dados no tópico "device1"
            client.publish("device4", mensagem)
            print(f"Dados enviados para o tópico 'device4': {mensagem}")

        
        print("\n")
        # Aguarda 10 segundos antes de enviar o próximo conjunto de dados
        time.sleep(5)
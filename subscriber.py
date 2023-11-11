# Subscriber que ficará escutando todos tópicos/devices

import paho.mqtt.client as paho
import paho.mqtt.publish as publish

import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do broker MQTT da Tago
broker_address = 'mqtt.tago.io'
port = 1883

mqtt_publish_topic = "tago/data/post" 
mqqt_config = {
    "device1": {
        "id": os.getenv("DEVICE1_ID"),
        'password': os.getenv("DEVICE1_TOKEN")
    },
    "device2": {
        "id": os.getenv("DEVICE2_ID"),
        'password': os.getenv("DEVICE2_TOKEN")
    },
    "device3": {
        "id": os.getenv("DEVICE3_ID"),
        'password': os.getenv("DEVICE3_TOKEN")
    },
    "device4": {
        "id": os.getenv("DEVICE4_ID"),
        'password': os.getenv("DEVICE4_TOKEN")
    }
}

# Função de callback quando a conexão com o broker é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))

# Ao receber uma mensagem de um device
def on_message(mosq, obj, msg):
    print("%-20s %d %s" % (msg.topic, msg.qos, msg.payload))
    mosq.publish('pong', 'ack', 0)


    # Envio dos dados para Tago
    publish.single(mqtt_publish_topic, msg.payload, qos=1, retain=False, hostname=broker_address,
               port=port, client_id='', keepalive=60, auth={'username': mqqt_config[msg.topic]["id"], 'password': mqqt_config[msg.topic]["password"]})


def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    # Conexão local para receber eventos dos devices
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect("127.0.0.1", 1883, 60)
    client.subscribe("device1", 0)
    client.subscribe("device2", 0)
    client.subscribe("device3", 0)
    client.subscribe("device4", 0)

    while client.loop() == 0:
        pass

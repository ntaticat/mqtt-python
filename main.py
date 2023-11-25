import ssl
import sys

import paho.mqtt.client

def on_connect(client, userdata, flags, rc):
    print(f'Se ha conectado al broker Mosquitto {client._client_id}')
    client.subscribe(topic='home/test/#', qos=2)

def on_message(client, userdata, message):
    print(f'-- topic: {message.topic}, payload: {message.payload}, qos: {message.qos} --')

def main():
    client = paho.mqtt.client.Client(client_id='esp32-sumulation1', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='192.168.0.166', port=1883)
    client.loop_forever()
    
if __name__ == '__main__':
    main()

sys.exit(0)
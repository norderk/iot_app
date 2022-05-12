import paho.mqtt.client as mqtt
import time
import os

MQTT_BROKER_HOST = str(os.getenv('MQTT_BROKER_HOST'))
MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT'))
MQTT_KEEP_ALIVE_INTERVAL = int(os.getenv('MQTT_KEEP_ALIVE_INTERVAL'))

def on_connect(client, userdata, flags, rc):
    
    if rc == 0:
        print("Connected - OK\n")
        client.subscribe("zigbee2mqtt/living_room")
    else:
        print("Failed to connect to MQTT broker, return code ", rc)
        print("\n")       

def on_message(client, userdata, msg):    
    print("calling on_message:\n")
    print(msg.topic + " " + str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: ", buf)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))


def call_mqtt(topic, payload):
    topic = topic
    payload = payload

    client = mqtt.Client("testName")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.on_message = on_message

    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEP_ALIVE_INTERVAL)
    # client.subscribe("rootTopic/topic/uplink")
    client.loop_start()

    client.publish(topic=topic, payload=payload)
    # time.sleep(5)

    client.loop_stop()
    client.disconnect()
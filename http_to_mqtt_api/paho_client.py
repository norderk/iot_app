import os

import paho.mqtt.client as mqtt

MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST")
MQTT_BROKER_PORT = os.getenv("MQTT_BROKER_PORT")
MQTT_KEEP_ALIVE_INTERVAL = os.getenv("MQTT_KEEP_ALIVE_INTERVAL")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected - OK\n")
        client.subscribe("zigbee2mqtt/living_room_ceiling")
    else:
        print("Failed to connect to MQTT broker, return code ", rc)
        print("\n")


def on_message(client, userdata, msg):
    print("calling on_message:\n")
    print(msg.topic + " " + str(msg.payload))


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code " + str(rc))


def call_mqtt(topic, payload):
    print("MQTT SCRIPT WAS RUN!")
    print(topic)
    print(payload)
    client = mqtt.Client("myClient")
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

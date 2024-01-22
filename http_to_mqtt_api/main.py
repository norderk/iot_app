"""
This module sets up a FastAPI application to interact with MQTT for controlling
Zigbee devices. It includes routes for checking the server status and sending
commands to Zigbee devices via MQTT.
"""

import logging.config
import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from paho_client import MQTTClient

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
logger.info("running module %s in %s", __name__, current_dir)

app = FastAPI()

# Define what calls can get returns
# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://127.0.0.1:8000",  # Only allow requests from this origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allows requests from the specified origin
    allow_credentials=True,
    allow_methods=["*"],  # You might limit this to actual needed methods e.g., GET, POST
    allow_headers=["*"],  # Adjust based on actual headers your client sends
)


def get_mqtt_client():
    mqtt_client = MQTTClient()
    mqtt_client.connect()
    try:
        yield mqtt_client
    finally:
        mqtt_client.disconnect()


# App functions
@app.get("/")
def read_root():
    """
    Root endpoint to check server status.
    Returns a simple JSON indicating the server is running.
    """
    return {"Connection": "OK"}


# ex: localhost:80/zigbee/?topic=TOPIC_1&payload=PAYLOAD_1
# on and off: /zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload=on      (alt. off)
# change brightness: /zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload={"brightness": 250 }
# chang color: 127.0.0.1:8000/zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload={"color": {"r": 255, "g": 200, "b": 79}}  # noqa: E501


@app.get("/zigbee/")
def call_zigbee(topic: str, payload: str, mqtt_client: MQTTClient = Depends(get_mqtt_client)):
    """
    Endpoint to send MQTT commands to Zigbee devices.

    Parameters:
    - topic (str): MQTT topic to publish the message to.
    - payload (str): Payload to send, typically device commands.

    Returns a confirmation of the sent topic and payload.
    """
    logger.info("Payload: %s, Topic: %s", payload, topic)
    mqtt_client.publish(payload=payload, topic=topic)
    return {"topic": topic, "payload": payload}

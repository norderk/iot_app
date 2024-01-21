"""
This module provides functionality to connect to an MQTT broker and
publish messages to a specified topic. It is designed to integrate with
FastAPI to control Zigbee devices via MQTT.
"""

import logging.config
import os

import paho.mqtt.client as mqtt

# Configure logging
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
logger.info("running module %s in %s", __name__, current_dir)


class MQTTClient:
    """
    A class to handle MQTT client operations including connecting,
    publishing messages, and handling callback events.

    Attributes:
        host (str): Hostname or IP address of the MQTT broker.
        port (int): Port number for the MQTT broker.
        keep_alive (int): Keep alive interval for the MQTT connection.
        client (mqtt.Client): The Paho MQTT client instance.
    """

    def __init__(self):
        """
        Initialize the MQTTClient instance.

        Parameters:
            host (str): Hostname or IP address of the MQTT broker.
            port (int): Port number for the MQTT broker.
            keep_alive (int): Keep alive interval for the MQTT connection.
        """
        self.host: str = str(os.getenv("MQTT_BROKER_HOST", "localhost"))  # pylint: disable=W1508
        self.port: int = int(os.getenv("MQTT_BROKER_PORT", 1883))  # pylint: disable=W1508
        # pylint: disable=W1508
        self.keep_alive: int = int(os.getenv("MQTT_KEEP_ALIVE_INTERVAL", 60))
        self.client = mqtt.Client("myClient")
        self.setup_callbacks()

    def setup_callbacks(self):
        """Setup the callback methods for the MQTT client."""
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        """
        Callback for when the client receives a CONNACK response from the server.

        Parameters:
            client: The client instance for this callback.
            userdata: The private user data as set in Client() or userdata_set().
            flags: Response flags sent by the broker.
            rc: The connection result.
        """
        if rc == 0:
            logger.info("Connected to MQTT Broker")
        else:
            logger.error("Failed to connect to MQTT Broker: Return code %s", rc)

    def on_message(self, client, userdata, msg):
        """
        Callback for when a PUBLISH message is received from the server.

        Parameters:
            client: The client instance for this callback.
            userdata: The private user data as set in Client() or userdata_set().
            msg: An instance of MQTTMessage, which is a class with members
            topic, payload, qos, retain.
        """
        logger.info("Received message on %s: %s", msg.topic, msg.payload)

    def on_log(self, client, userdata, level, buf):
        """
        Callback for logging purposes.

        Parameters:
            client: The client instance for this callback.
            userdata: The private user data as set in Client() or userdata_set().
            level: Severity of the message.
            buf: The message itself.
        """
        logger.debug("Log: %s", buf)

    def on_disconnect(self, client, userdata, flags, rc=0):
        """
        Callback for when the client disconnects from the broker.

        Parameters:
            client: The client instance for this callback.
            userdata: The private user data as set in Client() or userdata_set().
            flags: The disconnection result.
            rc: The disconnection result.
        """
        logger.info("Disconnected from MQTT Broker with result code %s", rc)

    def connect(self):
        """
        Connect to the MQTT broker and start the network loop.
        """
        self.client.connect(self.host, self.port, self.keep_alive)
        self.client.loop_start()

    def publish(self, topic, payload):
        """
        Publish a message to a specified topic.

        Parameters:
            topic (str): MQTT topic to publish the message to.
            payload (str): Message payload to send.
        """
        logger.info("Publishing message to %s: %s", topic, payload)
        self.client.publish(topic, payload)

    def disconnect(self):
        """
        Stop the network loop and disconnect from the MQTT broker.
        """
        self.client.loop_stop()
        self.client.disconnect()


def main():
    # noqa: E1121
    mqtt_client = MQTTClient()
    mqtt_client.connect()

    # Example usage
    topic = "zigbee2mqtt/living_room_ceiling/set"
    payload = "ON"
    mqtt_client.publish(topic, payload)

    mqtt_client.disconnect()


if __name__ == "__main__":
    main()

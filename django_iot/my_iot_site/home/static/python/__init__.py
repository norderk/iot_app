import os

MQTT_BROKER_HOST: str | None = os.getenv("MQTT_BROKER_HOST")

MQTT_BROKER_PORT: int | None = None
if (port := os.getenv("MQTT_BROKER_PORT")) is not None:
    MQTT_BROKER_PORT = int(port)

MQTT_KEEP_ALIVE_INTERVAL: int | None = None
if (interval := os.getenv("MQTT_KEEP_ALIVE_INTERVAL")) is not None:
    MQTT_KEEP_ALIVE_INTERVAL = int(interval)

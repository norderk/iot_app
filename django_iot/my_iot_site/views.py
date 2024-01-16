import os

# from static.executable_python.iot_client import call_mqtt
# TODO:Need to combine path with BASE_DIR before import, # pylint: disable=W0511
# specify in manage.py?
# pylint: disable=W0511
import paho.mqtt.client as mqtt
from django.shortcuts import render

# MQTT functions
MQTT_BROKER_HOST: str | None = os.getenv("MQTT_BROKER_HOST")

MQTT_BROKER_PORT: int | None = None
if (port := os.getenv("MQTT_BROKER_PORT")) is not None:
    MQTT_BROKER_PORT = int(port)

MQTT_KEEP_ALIVE_INTERVAL: int | None = None
if (interval := os.getenv("MQTT_KEEP_ALIVE_INTERVAL")) is not None:
    MQTT_KEEP_ALIVE_INTERVAL = int(interval)


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


# actuall views
def home_view(request):
    return render(request, "home.html", {})


# @csrf_exempt
def iot_view(request, *args, **kwargs):
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #         print("AJAX WAS USED!")
    return render(request, "iot.html", {})


def simple_function(request):
    print("THIS is a request:", request)
    topic = "zigbee2mqtt/living_room_ceiling/set"
    payload = "OFF"
    call_mqtt(topic=topic, payload=payload)
    return render(request, "iot.html", {})  # this could also return iot base page!


def simple_function_on(request):
    print("THIS is a request:", request)
    topic = "zigbee2mqtt/living_room_ceiling/set"
    payload = "ON"
    call_mqtt(topic=topic, payload=payload)
    return render(request, "iot.html", {})


def test_slug(request, slug):
    print("THIS is a request:", request)
    print("This is parameters:", slug)
    return render(request, "iot.html", {})


# @csrf_exempt
# def iot_action(request, *args, **kwargs):
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         print("AJAX WAS USED!")
#     topic = "living_room"
#     payload = "ON"
#     arg_lst = ["python3", "test_system.py", "--topic", f"{topic}", "--payload", f"{payload}"]
#     subprocess.Popen(arg_lst, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


def spotify_view(request):
    return render(request, "spotify.html", {})


def stats_view(request):
    return render(request, "stats.html", {})


def weather_view(request):
    return render(request, "weather.html", {})

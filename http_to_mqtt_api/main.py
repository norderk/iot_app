from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from paho_client import call_mqtt

# print(os.path.__path__)

app = FastAPI()

# Define what calls can get returns
# https://fastapi.tiangolo.com/tutorial/cors/
origins = ["http://localhost", "http://localhost:8000", "http://127.0.0.1:8000/", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# App functions
@app.get("/")
def read_root():
    # Call client()
    return {"Connection": "OK"}


# ex: localhost:80/zigbee/?topic=TOPIC_1&payload=PAYLOAD_1
# on and off: /zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload=on      (alt. off)
# change brightness: /zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload={"brightness": 250 }
# chang color: 127.0.0.1:8000/zigbee/?topic=zigbee2mqtt/kitchen_window/set&payload={"color": {"r": 255, "g": 200, "b": 79}}  # noqa: E501


@app.get("/zigbee/")
def call_zigbee(topic: str, payload: str):
    print(f"Payload: {payload}")
    print(f"topic: {topic}")

    call_mqtt(payload=payload, topic=topic)
    return {"topic": topic, "payload": payload}

    # topic = "zigbee2mqtt/living_room_ceiling/set"
    # payload = 'ON'

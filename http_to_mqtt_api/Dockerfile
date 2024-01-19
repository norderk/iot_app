FROM python:3.10
WORKDIR /api_folder
COPY . /api_folder/
RUN pip install --no-cache-dir --upgrade -r /api_folder/requirements.txt
ENV MQTT_BROKER_HOST=<IP_MQTT_BROKER>
ENV MQTT_BROKER_PORT=<PORT_MQTT_BROKER>
ENV MQTT_KEEP_ALIVE_INTERVAL=60
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
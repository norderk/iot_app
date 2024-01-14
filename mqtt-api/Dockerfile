FROM python:3.10
WORKDIR /api_folder
COPY . /api_folder/
RUN pip install --no-cache-dir --upgrade -r /api_folder/requirements.txt
ENV MQTT_BROKER_HOST=192.168.0.17
ENV MQTT_BROKER_PORT=1883
ENV MQTT_KEEP_ALIVE_INTERVAL=60
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

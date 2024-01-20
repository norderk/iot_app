# HTTP to MQTT -client

## RUN APP

### Docker
```bash
docker build -t http_mqtt .
docker run -d -p 80:80 --name http_mqtt http_mqtt
```

### Locally
```bash
uvicorn main:app --host 0.0.0.0 --port 80
```
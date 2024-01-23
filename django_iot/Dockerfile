FROM python:3.10

COPY . /app
WORKDIR /app

ENV  PYTHONPATH="/app:$PYTHONPATH"

RUN apt-get update -y 
RUN pip install --upgrade pip && pip install -r requirements.txt

# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "my_iot_site/manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["python3", "my_iot_site/manage.py", "runserver"]

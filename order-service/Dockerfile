# Dockerfile
FROM python:3.7
COPY requirements.txt /orderapp/requirements.txt
WORKDIR /orderapp
RUN pip install -r requirements.txt
COPY . /orderapp
ENTRYPOINT ["bash", "-c", "flask db init && flask db migrate && flask db upgrade && python run.py"]
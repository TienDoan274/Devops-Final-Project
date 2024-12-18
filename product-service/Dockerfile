# Dockerfile
FROM python:3.7
COPY requirements.txt /productapp/requirements.txt
WORKDIR /productapp
RUN pip install -r requirements.txt
COPY . /productapp
ENTRYPOINT ["bash", "-c", "rm -rf /productapp/migrations && flask db init && flask db migrate && flask db upgrade && python run.py"]
FROM python:3.7
COPY requirements.txt /orderapp/requirements.txt 
WORKDIR /orderapp
RUN pip install -r requirements.txt
COPY . /orderapp
RUN flask db init && \
   flask db migrate && \
   flask db upgrade
ENTRYPOINT ["python"]
CMD ["run.py"]
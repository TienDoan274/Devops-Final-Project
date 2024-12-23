FROM python:3.7
COPY requirements.txt /productapp/requirements.txt 
WORKDIR /productapp
RUN pip install -r requirements.txt
COPY . /productapp
RUN flask db init && \
   flask db migrate && \
   flask db upgrade
ENTRYPOINT ["python"]
CMD ["run.py"]
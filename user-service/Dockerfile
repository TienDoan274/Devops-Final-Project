FROM python:3.7
COPY requirements.txt /userapp/requirements.txt 
WORKDIR /userapp
RUN pip install -r requirements.txt
COPY . /userapp
RUN flask db init && \
   flask db migrate && \
   flask db upgrade
ENTRYPOINT ["python"]
CMD ["run.py"]
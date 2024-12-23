FROM python:3.7
COPY requirements.txt /orderapp/requirements.txt
WORKDIR /orderapp
RUN pip install -r requirements.txt
COPY . /orderapp

COPY <<EOF init-db.sh
#!/bin/bash
if [ ! -d "/orderapp/migrations" ]; then
    flask db init
    flask db migrate
    flask db upgrade
else
    flask db upgrade
fi
python run.py
EOF

RUN chmod +x init-db.sh
ENTRYPOINT ["./init-db.sh"]
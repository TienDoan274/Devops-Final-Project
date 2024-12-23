FROM python:3.7
COPY requirements.txt /orderapp/requirements.txt 
WORKDIR /orderapp
RUN pip install -r requirements.txt
COPY . /orderapp

RUN echo '#!/bin/bash\n\
if [ ! -d "migrations" ]; then\n\
  flask db init\n\
fi\n\
flask db upgrade\n\
python run.py' > /orderapp/entrypoint.sh \
&& chmod +x /orderapp/entrypoint.sh

ENTRYPOINT ["/orderapp/entrypoint.sh"]
FROM python:3.7
COPY requirements.txt /productapp/requirements.txt 
WORKDIR /productapp
RUN pip install -r requirements.txt
COPY . /productapp

RUN echo '#!/bin/bash\n\
if [ ! -d "migrations" ]; then\n\
  flask db init\n\
fi\n\
flask db upgrade\n\
python run.py' > /productapp/entrypoint.sh \
&& chmod +x /productapp/entrypoint.sh

ENTRYPOINT ["/productapp/entrypoint.sh"]
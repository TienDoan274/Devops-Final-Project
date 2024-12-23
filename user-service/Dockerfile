FROM python:3.7
COPY requirements.txt /userapp/requirements.txt 
WORKDIR /userapp
RUN pip install -r requirements.txt
COPY . /userapp

RUN echo '#!/bin/bash\n\
if [ ! -d "migrations" ]; then\n\
  flask db init\n\
fi\n\
flask db upgrade\n\
python run.py' > /userapp/entrypoint.sh \
&& chmod +x /userapp/entrypoint.sh

ENTRYPOINT ["/userapp/entrypoint.sh"]
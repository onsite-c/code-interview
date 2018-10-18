FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask

COPY index.html ./
COPY server.py ./

ENV FLASK_ENV docker
EXPOSE 5000

CMD [ "python", "./server.py" ]

FROM python:3
WORKDIR /usr/src/app
RUN pip install "gunicorn>=19.8,<19.9"
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt
ADD . /usr/src/app
CMD gunicorn config.wsgi:application
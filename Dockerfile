FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    gettext \
    libgettextpo-dev \
    nginx \
    gcc \
    supervisor \
    build-essential \
    unixodbc \
    unixodbc-dev

RUN mkdir /conf && \
    mkdir /scripts && \
    mkdir -p /tmp/nginx/client_body_temp && \
    mkdir /code && \
    mkdir /code/static_files && \
    mkdir /code/media

ADD ./docker/conf/uwsgi_app.ini /conf/

WORKDIR /code
RUN touch reload

ADD requirements.txt /code/
RUN pip install -r requirements.txt && \
    pip install uWSGI==2.0.15

ADD . /code/

COPY ./docker/conf/settings.py /code/contacttracer/settings.py

RUN python /code/manage.py collectstatic --noinput

EXPOSE 8000

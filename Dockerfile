FROM python:3.7.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev bash make automake
RUN pip install --upgrade pip
ADD ./requirements.txt /usr/src/app/requirements.txt
ADD ./requirements-dev.txt /usr/src/app/requirements-dev.txt
ADD ./.docker /usr/src/app/.docker

RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
WORKDIR /usr/src/app/
RUN ls -la .docker/
RUN ls -la /usr/src/app/.docker/entrypoint.sh

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

EXPOSE 8888


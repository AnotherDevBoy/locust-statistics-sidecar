FROM python:3-slim

ENV NEW_RELIC_LICENSE_KEY=
ENV NEW_RELIC_APP_NAME="Locust NewRelic Sidecar"
ENV NEW_RELIC_LOG=/tmp/newrelic.log
ENV NEW_RELIC_LOG_LEVEL=info

COPY src src
COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

CMD ["newrelic-admin", "run-program", "python3", "-u", "src/main.py"]

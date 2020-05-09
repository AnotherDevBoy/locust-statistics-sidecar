.PHONY: local-run image run

local-run:
	newrelic-admin run-program python3 src/main.py

image: Dockerfile
	docker build -t locust-newrelic-sidecar .

run:
	docker rm locust-newrelic-sidecar
	docker run --name locust-newrelic-sidecar --env-file ./env.list locust-newrelic-sidecar

.PHONY: lint build run cleanup

lint:
	pycodestyle --ignore=E501 src

image: docker-compose.yml
	docker-compose build

run: image
	docker-compose up

cleanup:
	docker-compose down

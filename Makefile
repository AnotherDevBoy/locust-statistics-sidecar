.PHONY: lint build run cleanup

lint:
	pycodestyle --ignore=E501 src

image: test/docker-compose.yml
	cd test && docker-compose build

run: image
	cd test && docker-compose up

cleanup:
	cd test && docker-compose down

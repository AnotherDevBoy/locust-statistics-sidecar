.PHONY: lint build run cleanup

lint:
	pycodestyle --ignore=E501 src

test-image: test/docker-compose.yml
	cd test && docker-compose build

test-run: test-image
	cd test && docker-compose up

test-cleanup:
	cd test && docker-compose down

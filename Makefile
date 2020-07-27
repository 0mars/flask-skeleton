# use the rest as arguments for targets
TARGET_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# ...and turn them into do-nothing targets
$(eval $(TARGET_ARGS):;@:)


.PHONY: init init-migration build run db-migrate test tox

init:  build run
	docker-compose exec web skel db upgrade
	docker-compose exec web skel init
	@echo "Init done, containers running"

build:
	docker-compose build

run:
	docker-compose up -d

db-migrate:
	docker-compose exec web skel db migrate

db-upgrade:
	docker-compose exec web skel db upgrade

test:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e test

tox:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e py37

lint:
	docker-compose run web tox -e lint

start:
	docker-compose up -d

rebuild:
	docker-compose build --force-rm $(TARGET_ARGS)

clean-restart:
	docker-compose stop $(TARGET_ARGS) && docker-compose rm -f $(TARGET_ARGS) && make rebuild $(TARGET_ARGS) && docker-compose up -d --no-deps --build $(TARGET_ARGS)

run: install
	python skel/configurations/app.py
	gunicorn -c gunicorn.config.py skel.configurations.wsgi:app --access-logfile '-' --error-logfile '-'

run-prod: install
	gunicorn -c gunicorn.config.py wsgi:app

install:
	pip install -e .
# 	skel db init
	skel db upgrade head
	#python setup.py develop

test:
	STAGE=test APP_SETTINGS="skel.configurations.server.config.Testing" pytest

freeze:
	pipenv run pipenv_to_requirements

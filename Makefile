setup-env:
	cd ./cassandra-rest-api && \
	pipenv install -r requirements.txt

start-docker:
	docker-compose -f docker-compose.yml up

shutdown-docker:
	docker-compose -f docker-compose.yml down

rest-api-app:
	python3 ./cassandra-rest-api/src/app.py
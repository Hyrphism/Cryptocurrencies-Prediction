start-docker:
	docker-compose -f docker-compose.yml up

shutdown-docker:
	docker-compose -f docker-compose.yml down

rest-api-app:
	python3 ./cassandra-rest-api/src/app.py
# Cryptocurrencies-Prediction

## Setup
For the ease of deployment Docker Compose script is used. It still needs some manual steps, however.

* Cassandra
  * Edit `docker-compose.yml` file and replace paths in `volumes` to match your environment
  * To start all the services run this command from the main project folder: docker-compose up

## Usage

1. Clone repository

```
  git clone 
```

2. Run Docker containers

```
  make start-docker
```

3. Setup virtual env for project

```
  make setup-env
```

4. Run project

```
  make rest-api-app
```

5. Predict price

```
  Go to jupyter notebook to analyze and predict
```
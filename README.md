# cicd-alembic-migrations

## How the project was created

- Poetry is used to manage the dependencies
- Docker is used to run the project
- Alembic is used to manage the migrations
  - `alembic init alembic` was used to create the `alembic` folder

## Steps to run the project

```shell
docker compose build && docker compose up --abort-on-container-exit
```

`--abort-on-container-exit` will stop the containers when the first container stops.

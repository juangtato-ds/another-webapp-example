# another-webapp-example

Another webapp example

- [another-webapp-example](#another-webapp-example)
  - [Local deployment - docker compose](#local-deployment---docker-compose)
  - [Frontend](#frontend)
    - [Local](#local)
  - [Backend](#backend)
    - [Local](#local-1)
  - [Dummy db](#dummy-db)


## Local deployment - docker compose

1. **Create `.env` file** with the configuration
    ```
    # APP
    APP_REST_HOST=0.0.0.0
    APP_REST_PORT=5000
    APP_REST_RELOAD=False
    APP_LOG_LEVEL=info

    # LYRICS SEARCH
    APP_LYRICS_SOURCE=musixmatch
    APP_LYRICS_APIKEY=your-api-key

    # LYRICS ANALYSER
    APP_LYRICS_ANALYSER_SOURCE=openai
    APP_LYRICS_ANALYSER_APIKEY=your-api-key

    # SQL
    APP_SQL_username=postgres
    APP_SQL_password=postgres
    APP_SQL_host=db
    APP_SQL_database=demo
    ```
1. **Run docker compose**. 
   1. The frontend will wait for the backend to start.
   2. The backend will wait for the db to be healthy.
1. **First time**:
   1. Create tables in demo db:
        ```bash
        cd db
        ./migrate-local.sh
        ```
1. **Open Web browser** in http://localhost

## Frontend

Made in Angular 18.

### Local

```bash
cd frontend
npm i
npm run start
```

## Backend

Python 3.10 backend made over FastAPI.

### Local

Follow instructions in [backend readme](backend/README.md)

## Dummy db

For local you can launch the PostgreSQL db by

```bash
docker compose -f docker-compose.local.yml up -d
```

Then the basic tables must be created. For this:

```bash
cd db
./migrate-local.sh
```

Take into account that `docker compose -f docker-compose.local.yml down` will remove all data from db.
This db is only for testing purposes.
Btw, you can always `docker compose -f docker-compose.local.yml stop` and continue other day.
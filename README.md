# another-webapp-example

Another webapp example

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
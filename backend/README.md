# Song Analyser

Awesome description!

- [Song Analyser](#song-analyser)
  - [Prerequisites](#prerequisites)
  - [Local](#local)
    - [Configuration](#configuration)
    - [Running](#running)

## Prerequisites

- python 3.10
- Create Python environment, activate and install poetry on it
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -U pip poetry
    ```
- Install dependencies
    ```bash
    poetry install
    # Quick and dirty troubleshooting: remove poetry.lock
    ```
- **Develop** Install pre-commit
    ```bash
    pre-commit install
    ```

## Local

### Configuration

Create a `.env` file in this folder with the parameters in the example:

```
# APP
APP_REST_HOST=localhost
APP_REST_PORT=5000
APP_REST_RELOAD=True
APP_LOG_LEVEL=debug

# LYRICS SEARCH
APP_LYRICS_SOURCE=musixmatch
APP_LYRICS_APIKEY=your-api-key

# LYRICS ANALYSER
APP_LYRICS_ANALYSER_SOURCE=openai
APP_LYRICS_ANALYSER_APIKEY=your-api-key

# SQL
APP_SQL_username=postgres
APP_SQL_password=postgres
APP_SQL_host=localhost
APP_SQL_database=demo
```

### Running

```bash
./run-api.sh
```

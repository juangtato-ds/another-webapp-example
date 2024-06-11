# Song Analyser

Awesome description!

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

## Configuration

Create a `.env` file in this folder with the parameters in the example:

```
APP_REST_HOST=localhost
APP_REST_PORT=5000
APP_REST_RELOAD=True
APP_LOG_LEVEL=debug
```

## Local

```bash
./run-api.sh
```

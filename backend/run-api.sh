export $(grep -v '^#' .env | xargs)
PYTHONPATH=./src python -m song_backend_rest.run_api

# Nativamente
FLASK_APP=01_flask.py flask run -h 0.0.0.0 -p 1337
python -m sanic --host 0.0.0.0 --port 1337 01_sanic.app

# Sanic c/ 4 workers
python -m sanic --host 0.0.0.0 --port 1337 --workers 4 01_sanic.app

# Via Gunicorn (4 workers)
gunicorn -b 0.0.0.0:1337 -w 4 01_flask:app
gunicorn -b 0.0.0.0:1337 -w 4 01_sanic:app \
         --worker-class sanic.worker.GunicornWorker

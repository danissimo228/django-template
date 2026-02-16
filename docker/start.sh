#!/bin/sh
python manage.py collectstatic --noinput || exit 1
python3 manage.py makemigrations || exit 1
python3 manage.py migrate || exit 1
python3 manage.py create_admin_user || exit 1

python -m gunicorn \
  --workers ${WORKERS_COUNT:-2} \
  --threads ${WORKER_THREADS_COUNT:-1} \
  --timeout ${WORKERS_TIMEOUT:-300} \
  -k gthread \
  --reload \
  --bind 0.0.0.0:8000 \
  --log-level INFO \
  config.wsgi:application

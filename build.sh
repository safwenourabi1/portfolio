#!/usr/bin/env bash
# exit on error
pip install -r requirements.txt
set -o errexit

poetry install
poetry add 'whitenoise[brotli]'
python manage.py collectstatic --no-input
python manage.py migrate

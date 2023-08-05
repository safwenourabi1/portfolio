#!/usr/bin/env bash
# exit on error




pip install whitenoise
pip install -r requirements.txt
set -o errexit



python manage.py collectstatic --no-input
python manage.py migrate

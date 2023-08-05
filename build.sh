#!/usr/bin/env bash
# exit on error
curl -sSL https://install.python-poetry.org | python3 -
[tool.poetry.dependencies]


python = "^3.9.10"
poetry add django

pip install -r requirements.txt
set -o errexit



python manage.py collectstatic --no-input
python manage.py migrate

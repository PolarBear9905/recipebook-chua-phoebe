#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
mkdir -p static
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic --noinput --clear
python manage.py migrate
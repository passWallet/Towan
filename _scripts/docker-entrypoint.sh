#!/usr/bin/env bash

echo "[run] Update Database"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "[run] Create super user"
echo "from django.contrib.auth.models import User
from getenv import env
if not User.objects.filter(username=env('SUPERUSER_USERNAME')).count():
    User.objects.create_superuser(env('SUPERUSER_USERNAME'), env('SUPERUSER_EMAIL'), env('SUPERUSER_PASSWORD'))
" | python manage.py shell

echo "[run] runserver"
python manage.py runserver 0.0.0.0:8000

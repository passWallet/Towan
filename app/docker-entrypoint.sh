#!/usr/bin/env bash

echo "[run] Update Database"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "[run] Create super user and add api key to super user"
echo "from django.contrib.auth.models import User
from tastypie.models import ApiKey
from getenv import env
if not User.objects.filter(username=env('SUPERUSER_USERNAME')).count():
    superuser = User.objects.create_superuser(env('SUPERUSER_USERNAME'), env('SUPERUSER_EMAIL'), env('SUPERUSER_PASSWORD'))
    ApiKey.objects.create(user=superuser,key=env('SUPERUSER_APIKEY'))
" | python manage.py shell

echo "[run] runserver"
python manage.py runserver 0.0.0.0:8000

#!/usr/bin/env bash

echo "===== INSTALL DJANGO ====="
apt-get update
apt-get install -y python-pip libpq-dev python-dev
apt-get install -y binutils libproj-dev gdal-bin
sudo pip install -r /home/vagrant/workspace/app/requirements.txt

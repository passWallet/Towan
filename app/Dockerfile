############################################################
# Dockerfile to run towan container
#
############################################################

FROM django:python2-onbuild
MAINTAINER Lola Rigaut-Luczak <rllola80@gmail.com>

# Important Mise à jour toujours avant
RUN apt-get -y update

# To teddy a bit the room
RUN apt-get -y autoremove

#RUN useradd -u 1000 -g 100 -d /home/django django
#USER django

ADD ./docker-entrypoint.sh /usr/src/app/

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "-e", "/usr/src/app/docker-entrypoint.sh"]

FROM python:3.8.2-slim-buster

RUN apt-get update && apt-get install -y apache2 apache2-dev \
 && pip install mod_wsgi \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8

WORKDIR /usr/src/app

COPY . .

RUN pip install -e .

RUN mod_wsgi-express setup-server wsgi.py --port=80 \
    --user www-data --group www-data \
    --server-root=/etc/reflex-api

CMD [ "/etc/reflex-api/apachectl", "start" ]

# The commands below get apache running but there are issues accessing it online
# The port is only available if you go to another port first
# ENTRYPOINT ["/sbin/init"]
# CMD ["/usr/sbin/apache2ctl"]
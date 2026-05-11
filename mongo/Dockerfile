FROM mongo:7.0

RUN mkdir -p /data/db /data/configdb \
    && chown -R mongodb:mongodb /data/db /data/configdb

COPY mongo/init-scripts mongo/docker-entrypoint-initdb.d/

EXPOSE 27017

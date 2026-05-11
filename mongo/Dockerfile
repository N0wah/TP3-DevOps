FROM mongo:7.0
USER mongodb

COPY ./mongo/init-scripts /docker-entrypoint-initdb.d/

EXPOSE 27017

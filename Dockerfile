FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD my-secret-pw
ENV MYSQL_DATABASE userdb
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ADD init.sql /docker-entrypoint-initdb.d

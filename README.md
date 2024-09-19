# Backend Builderplate

Tired of generating a new backend constinously for your projects? This repo provides a backend builderplate, the skeleton, for deploying your database and basic API routes locally. For the database, we are using *MariaDB*, but feel free to implement your favorite one. The API is created using Flask and the entire project is locally deployed using Docker.


For the database, it would be locally using MariaDB and Dockerfile. 

# The docker-compose.yml file

For the moment, it just deploys a local database (need to improve this description).

# The init.sql file

It generates a new database with the table that the frontend will use to obtain all the information needed. 

# How to deploy the project locally.

As all the backend would be on a docker container, it is not necessary to install anything more than Docker (for the moment). Execute the these commands in the following order

```bash
docker-compose build && docker-compose up
```

If you want to interact with the database using a terminal, just execute:

```bash
sudo docker exec -it backend_builderplate bash
```

A new docker terminal will be open for you to interact with the container. Execute:

```bash
mariadb -u admin@localhost.com -p
```

where the password is: `1234`

Voilà. You are inside the database. Use the command:

```bash
use backend_db;
```

for start using the database you have just deployed. Enjoy when using this builderplate and feel free to contribute to this opensource project

# Contributing
Wanna do something for the community? Here you can do it! When contributing to this project, first raise an issue describing what you think could be improved (SQL, Docker, bugs, features...). If the issues passes the check, feel free to develop in a new branch and doing some PRs!
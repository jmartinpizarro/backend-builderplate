# Backend Builderplate

Tired of generating a new backend constinously for your projects? This repo provides a backend builderplate, the skeleton, for deploying your database and basic API routes locally. For the database, we are using *MariaDB*, but feel free to implement your favorite one. 

The API is created using Flask and the entire project is locally deployed using Docker. For the database, it would be locally deployed using MariaDB and Dockerfile. 

# The docker-compose.yml file

For the moment, it just deploys a local MariaDB database and the backend API in charge of interacting with the database.

# The init.sql file

It generates a new database with the `users` table that the frontend will use to obtain all the information needed. If you want to create more tables when generating the database, just add the necessary code in this file.

# How to deploy the project locally.

As all the backend would be on a docker container, it is not necessary to install anything more than Docker. Execute the following commands in the correspondant order.

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

for start using the database you have just deployed. If you want to check that everything is working correctly, you can execute:

```bash
curl http://localhost:5000/get-users
```

where you should get the following output:


```bash
{"response":[["admin","admin@localhost.com","1234"]]}
```
 Enjoy when using this builderplate and feel free to contribute to this opensource project.

# Contributing
Wanna do something for the community? Here you can do it! When contributing to this project, first raise an issue describing what you think could be improved (SQL, Docker, bugs, features...). If the issue passes the check, feel free to develop in a new branch and doing some PRs!

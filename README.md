# five-apps-same-app

Welcome to this magnificent proyect for the sake of understanding DDBB Automatization and API Rest in different programming languages. The aim of this app is to generate it in the terminal, and not in as a web app. This project would be using the following technologies:

- Python
- Rust
- C++
- Golang
- JavaScript

For the database, it would be locally using MariaDB and Dockerfile. 

# The docker-compose.yml file

For the moment, it just deploys a local database (need to improve this description).

# The init.sql file

It generates a new database with the table that the frontend will use to obtain all the information needed. 

## How to deploy the project locally.

As all the backend would be on a docker container, it is not necessary to install anything more than Docker (for the moment). Execute the these commands in the following order

```bash
docker-compose build && docker-compose up
```

If you want to interact with the database using a terminal, just execute:

```bash
sudo docker exec -it automated_database bash
```

A new docker terminal will be open for you to interact with the container. Execute:

```bash
mariadb -u dummy@localhost.com -p
```

where the password is: `dummy_password`
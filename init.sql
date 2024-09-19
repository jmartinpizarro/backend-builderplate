CREATE DATABASE IF NOT EXISTS backend_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

USE backend_db;

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) UNIQUE
);

INSERT INTO users VALUES('admin', 'admin@localhost.com', '1234')
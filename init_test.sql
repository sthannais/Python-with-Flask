DROP DATABASE IF EXISTS test;

CREATE DATABASE test;

use test;

CREATE TABLE
    todos(
        id int NOT NULL AUTO_INCREMENT,
        done CHAR(150) NOT NULL,
        label CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );
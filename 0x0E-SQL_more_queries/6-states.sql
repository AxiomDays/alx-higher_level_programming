-- a script that creates a table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS id_not_null(
id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL
);

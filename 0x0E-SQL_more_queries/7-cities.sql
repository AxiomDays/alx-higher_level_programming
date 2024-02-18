-- a script that creates a table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS  hbtn_0d_usa.cities(
id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL, 
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL
);

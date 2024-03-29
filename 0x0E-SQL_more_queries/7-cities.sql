-- Create the database hbtn_0d_usa if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database hbtn_0d_usa.
USE hbtn_0d_usa;
-- Create a table named 'cities' in the hbtn_0d_usa database.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(state_id) REFERENCES states(id));

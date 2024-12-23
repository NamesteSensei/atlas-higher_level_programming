-- Task 6: Create database hbtn_0d_usa and table states with primary key on id
-- This script creates the database and the table states with a unique, auto-incrementing id.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

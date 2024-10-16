-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Create the cities table with a foreign key
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Insert sample data into the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona');

-- Insert sample data into the cities table
INSERT INTO cities (state_id, name) VALUES 
(1, 'San Francisco'),
(1, 'San Diego'),
(2, 'Page'),
(2, 'Phoenix');

-- Task 7: Create table cities with a foreign key to states table

-- Ensure the database hbtn_0d_usa exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't exist
-- The table includes an id (auto-incrementing), a state_id, and the city name.
-- The state_id references the id in the 'states' table.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Insert sample data into the 'cities' table
INSERT INTO cities (state_id, name) VALUES
    (1, 'San Francisco'),
    (1, 'San Diego'),
    (2, 'Page'),
    (2, 'Phoenix');

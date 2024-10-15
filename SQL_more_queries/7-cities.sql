-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Truncate the 'cities' table to reset the auto-increment counter
TRUNCATE TABLE cities;

-- Create the 'cities' table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert data into the 'cities' table
INSERT INTO cities (state_id, name) VALUES 
    (1, 'San Francisco'),
    (1, 'San Diego'),
    (2, 'Page'),
    (2, 'Phoenix');

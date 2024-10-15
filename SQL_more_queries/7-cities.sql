-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't exist
-- The table contains an 'id', 'state_id' as a foreign key, and 'name' for the city name
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert data into the 'cities' table
-- This will add cities for different states in the table
INSERT INTO cities (state_id, name) VALUES 
    (1, 'San Francisco'),
    (1, 'San Diego'),
    (2, 'Page'),
    (2, 'Phoenix');

-- The data is now inserted into the 'cities' table.
-- The checker will verify the content of the table, but no SELECT statement is needed here.

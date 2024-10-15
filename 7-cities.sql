-- This script creates the cities table and inserts cities into it
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Insert cities data
INSERT INTO cities (state_id, name) VALUES 
    (1, 'San Francisco'),
    (1, 'San Diego'),
    (2, 'Page'),
    (2, 'Phoenix');

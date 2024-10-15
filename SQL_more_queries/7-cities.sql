-- Task 7: Create table cities with foreign key reference to states table
-- This script creates the table cities with a foreign key state_id that references the states table.

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

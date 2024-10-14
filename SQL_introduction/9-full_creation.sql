-- Task 9: Create 'second_table' and insert multiple rows
-- This script creates a table 'second_table' and inserts multiple records.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert records into the table
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10), 
(2, 'Alex', 3), 
(3, 'Bob', 14), 
(4, 'George', 8);

-- Task 3: Create table force_name with id and name (name can't be NULL)
-- This script creates the table force_name with a NOT NULL constraint on the name column.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

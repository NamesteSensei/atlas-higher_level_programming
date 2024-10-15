-- Task 5: Create table unique_id with unique constraint on id
-- This script creates the table unique_id with a UNIQUE constraint on the id column.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

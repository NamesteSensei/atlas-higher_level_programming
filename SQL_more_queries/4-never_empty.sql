-- Task 4: Create table id_not_null with default value for id and a name column
-- This script creates the table id_not_null with default value of 1 for id.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

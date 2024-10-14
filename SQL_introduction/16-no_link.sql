-- Task 16: List all records with non-empty names in 'second_table'
-- This script lists rows from 'second_table' where the 'name' field is not NULL or empty.
-- It orders the rows by 'score' in descending order.

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> '' 
ORDER BY score DESC;

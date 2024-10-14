-- Task 15: Count records grouped by score in 'second_table'
-- This script groups records by score and counts how many rows have the same score.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

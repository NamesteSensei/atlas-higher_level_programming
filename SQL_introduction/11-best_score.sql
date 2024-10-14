-- Task 11: List records with score >= 10 in 'second_table'
-- This script lists rows from 'second_table' where score is 10 or more, ordered by score.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

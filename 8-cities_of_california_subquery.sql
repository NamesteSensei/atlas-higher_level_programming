-- Script to list all cities of California in ascending order by id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1)
ORDER BY id ASC;

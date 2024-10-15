-- Task 11: Genre ID for all shows
-- This script lists all shows and their genre_id. If a show has no genre, display NULL.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

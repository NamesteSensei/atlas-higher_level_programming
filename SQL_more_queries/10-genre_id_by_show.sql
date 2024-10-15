-- Task 10: Genre ID by show
-- This script selects all shows that have at least one genre linked and displays the title and genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

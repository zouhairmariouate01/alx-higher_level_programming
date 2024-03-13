-- Retrieve all shows from the hbtn_0d_tvshows database that do not have a linked genre.
-- List all rows of the 'tv_shows.title' and 'tv_show_genres.genre_id' columns.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

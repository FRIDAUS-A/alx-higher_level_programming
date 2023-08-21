-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT t.title FROM tv_shows AS t
JOIN tv_show_genres AS tg
ON t.id = tg.show_id
WHERE tg.genre_id = 5
ORDER BY t.title ASC;

-- A script that lists all shows, and all genres 
-- linked to that show, from the database hbtn_0d_tvshows.

SELECT DISTINCT t.title, tr.name FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tg
ON t.id = tg.show_id
LEFT JOIN tv_genres AS tr
ON tr.id = tg.genre_id
ORDER BY t.title ASC;

-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexters

SELECT t.name FROM tv_genres AS t
JOIN tv_show_genres AS tg
ON t.id = tg.genre_id
WHERE tg.show_id = 8
ORDER BY t.name ASC;

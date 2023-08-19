-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexters

SELECT t.name FROM tv_genres AS t JOIN (
	SELECT tg.genre_id FROM tv_show_genres AS tg
	JOIN tv_shows AS t
	ON tg.show_id = t.id
	WHERE t.id = 8
) AS g
ON t.id = g.genre_id
ORDER BY t.name ASC;

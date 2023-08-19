--

SELECT t.name FROM tv_genres as t JOIN (
	SELECT tg.genre_id FROM tv_show_genres as tg
	JOIN tv_shows as t
	ON tg.show_id = t.id
	WHERE t.id = 8
) AS g
ON t.id = g.genre_id
ORDER BY t.name ASC;

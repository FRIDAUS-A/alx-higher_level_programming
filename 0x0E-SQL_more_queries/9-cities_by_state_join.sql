-- A script that lists all cities contained in the database hbtn_0d_usa.

SELECT id, name, FROM cities
JOIN ON cities.id = states.state_id
ORDER BY id ASC;

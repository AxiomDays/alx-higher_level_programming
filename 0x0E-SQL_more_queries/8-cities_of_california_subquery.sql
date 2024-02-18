-- a script that lists all the cities of California that can be found in the database

SELECT * FROM hbtn_0d_usa.states WHERE `name` = `California` ORDER BY cities.id ASC;

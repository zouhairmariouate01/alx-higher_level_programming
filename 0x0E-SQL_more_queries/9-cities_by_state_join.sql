-- Retrieve all cities from the hbtn_0d_usa database.
-- List all rows of the 'cities.id', 'cities.name', and 'states.name' columns.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;

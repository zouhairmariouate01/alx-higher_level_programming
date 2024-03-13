-- Retrieve all cities of California from the hbtn_0d_usa database.
-- List all rows of the 'id' and 'name' columns.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

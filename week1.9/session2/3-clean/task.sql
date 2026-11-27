.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..

SELECT restaurant_id, name, cuisine FROM restaurants
WHERE LOWER(cuisine) = 'italian';
UPDATE restaurants SET cuisine = 'Italian' 
WHERE LOWER(cuisine) = 'italian';

SELECT restaurant_id, postcode, UPPER(TRIM(postcode)) AS result FROM restaurants;
UPDATE restaurants SET postcode = UPPER(TRIM(postcode)) 
WHERE postcode IS NOT NULL;

SELECT * FROM restaurants WHERE delivery_fee IS NULL;
UPDATE restaurants SET delivery_fee = 2.49 
WHERE delivery_fee IS NULL;

SELECT * FROM customers 
WHERE email LIKE '%@test.com';
DELETE FROM customers 
WHERE email LIKE '%@test.com';

SELECT name, postcode, COUNT(*), MIN(rowid) AS rowid
FROM restaurants
GROUP BY name, postcode
HAVING COUNT(*) > 1;

DELETE FROM restaurants
WHERE rowid NOT IN (
  SELECT MIN(rowid) FROM restaurants GROUP BY name, postcode
); 
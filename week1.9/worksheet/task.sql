.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

SELECT COUNT(*)
FROM stations;

SELECT COUNT(*)
FROM pragma_table_info('members');

SELECT COUNT(*)
FROM sqlite_master
WHERE type = 'table';

SELECT capacity
FROM stations
WHERE name = 'Briggate';

SELECT year_added
FROM bikes
WHERE bike_id = 5;

SELECT count(*) AS capacity
FROM stations
WHERE capacity = 16;

SELECT count(*) AS capacity
FROM stations
WHERE capacity > 16;



SELECT year_added
FROM bikes
WHERE bike_id = 27;

SELECT count(*) AS capacity
FROM stations
WHERE capacity < 12;
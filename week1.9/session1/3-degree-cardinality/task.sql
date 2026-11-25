.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- To see all the tables in a database
.tables

-- To see the attributes belonging to each table478900
.schema customers
.schema restaurants
.schema menu_items
.schema drivers
.schema orders
.schema order_items
.schema reviews

-- And to see a count of the total number of tuples
SELECT COUNT(*) AS Cardinality FROM customers; 
SELECT COUNT(*) AS Cardinality FROM restaurants; 
SELECT COUNT(*) AS Cardinality FROM menu_items; 
SELECT COUNT(*) AS Cardinality FROM drivers; 
SELECT COUNT(*) AS Cardinality FROM orders; 
SELECT COUNT(*) AS Cardinality FROM order_items; 
SELECT COUNT(*) AS Cardinality FROM reviews; 
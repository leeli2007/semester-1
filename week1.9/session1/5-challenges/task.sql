.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

SELECT * FROM drivers;

SELECT name, price FROM menu_items WHERE restaurant_id = 3;

SELECT name FROM restaurants WHERE cuisine = 'Indian';

SELECT COUNT(*) AS customer_count FROM customers;

SELECT name, price FROM menu_items
WHERE is_vegetarian = 1 AND price <= 8
ORDER BY price ASC;

SELECT name, hygiene_rating FROM restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

SELECT name, hygiene_rating, postcode
FROM restaurants
WHERE postcode LIKE 'LS6%'
ORDER BY hygiene_rating DESC;

SELECT customer_id, name, email, joined_date
FROM customers
WHERE email LIKE '%@leeds.ac.uk'
ORDER BY joined_date DESC;

SELECT *
FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC
LIMIT 10;

SELECT name, price FROM menu_items
WHERE restaurant_id = 4
ORDER BY price DESC
LIMIT 1;

SELECT  order_id, status, order_time FROM orders
WHERE status = 'placed' AND order_time LIKE '2026-10%';

SELECT name, price
FROM menu_items
WHERE is_vegetarian = 1
ORDER BY price ASC
LIMIT 5;

SELECT restaurant_id, name, price FROM menu_items
ORDER BY price ASC
LIMIT 1;
SELECT restaurant_id, name, price FROM menu_items
ORDER BY price ASC
LIMIT 5;

SELECT COUNT(*) AS order_num FROM orders
WHERE (order_time LIKE '% 21:%' OR order_time LIKE '% 22:%' OR
order_time LIKE '% 23:%' OR order_time LIKE '% 00:%') AND status = 'delivered';


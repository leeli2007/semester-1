.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

BEGIN;

INSERT INTO orders
(order_id, customer_id, restaurant_id, driver_id)
VALUES (9001, 1, 1, NULL);

INSERT INTO order_items
(order_id, item_id, quantity)
VALUES (9001, 1, 2);

ROLLBACK;

SELECT * FROM orders
WHERE order_id = 9001;

SELECT * FROM order_items
WHERE order_id = 9001;



BEGIN;

INSERT INTO orders
(order_id, customer_id, restaurant_id, driver_id)
VALUES (9002, 1, 1, NULL);

INSERT INTO order_items
(order_id, item_id, quantity)
VALUES (9002, 1, 2);

COMMIT;

SELECT * FROM orders
WHERE order_id = 9002;

SELECT * FROM order_items
WHERE order_id = 9002;



BEGIN;

INSERT INTO orders
(order_id, customer_id, restaurant_id, driver_id)
VALUES (9003, 1, 1, NULL);

INSERT INTO order_items
(order_id, item_id, quantity)
VALUES (9003, 9999, 1);


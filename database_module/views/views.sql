--представление для таблицы products
CREATE OR REPLACE VIEW list_products AS
    SELECT
           p.product_title,
           p.price,
           p.in_stock
    FROM products p;

DROP VIEW IF EXISTS list_products;

SELECT *
FROM list_products;

-- для таблиц order_status и order
CREATE OR REPLACE VIEW product_category AS
    SELECT
           p.product_title,
           p.price,
           c.category_title,
           p.in_stock
    FROM products p
    JOIN categories c on p.categories_category_id = c.category_id;

SELECT * FROM product_category;
DROP VIEW IF EXISTS product_category;

-- для таблиц products и category
CREATE OR REPLACE VIEW orders_order_statuses AS
    SELECT
           o.order_id as order_id,
           o.total as total,
           os.status_name as status_name,
           o.carts_cart_id as cart_id
    FROM orders o
    JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id;

SELECT * FROM orders_order_statuses;
DROP VIEW IF EXISTS orders_order_statuses CASCADE;

-- материализированное представление
CREATE MATERIALIZED VIEW count_by_category AS
    SELECT
           c.category_title AS category,
           COUNT(o.order_id) AS count
    FROM categories c
        JOIN products p on c.category_id = p.categories_category_id
        JOIN cart_product cp on p.product_id = cp.products_product_id
        JOIN carts c2 on c2.cart_id = cp.carts_cart_id
        JOIN orders o on c2.cart_id = o.carts_cart_id
        JOIN order_statuses os on os.order_status_id = o.order_statuses_order_status_id
    WHERE os.status_name = 'Finished'
    GROUP BY c.category_title
    ORDER BY count DESC
WITH NO DATA;

REFRESH MATERIALIZED VIEW count_by_category;

SELECT * FROM count_by_category;
DROP MATERIALIZED VIEW IF EXISTS count_by_category;

-- представление на представлении
CREATE OR REPLACE VIEW users_orders AS
    SELECT
           o.order_id as order_id,
           u.first_name ||' '|| u.last_name as name,
           o.total as total,
           o.status_name as status_name
    FROM orders_order_statuses o
        JOIN carts c USING (cart_id)
        JOIN users u on u.user_id = c.users_user_id
    ORDER BY status_name;

SELECT * FROM users_orders;
DROP VIEW IF EXISTS users_orders CASCADE;

CREATE OR REPLACE VIEW users_orders_finished AS
    SELECT
           o.order_id as order_id,
           o.name as name,
           o.total as total,
           o.status_name as status_name
    FROM users_orders o
    WHERE o.status_name = 'Finished'
    ORDER BY total DESC;

SELECT * FROM users_orders_finished;
DROP VIEW IF EXISTS users_orders_finished;
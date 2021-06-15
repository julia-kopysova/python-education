-- Задание 1
-- Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city
CREATE TABLE IF NOT EXISTS potential_customers(
    potential_customers_id serial PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
	surname VARCHAR(255) NOT NULL,
	second_name VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL
);

-- Заполните данными таблицу.
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
VALUES (1, 'email1-1@gmail.com', 'name 1', 'surname 1', 'second_name 1', 'city 1'),
       (2, 'email1-2@gmail.com', 'name 2', 'surname 2', 'second_name 2', 'city 2'),
       (3, 'email1-3@gmail.com', 'name 3', 'surname 3', 'second_name 3', 'city 3'),
       (4, 'email1-4@gmail.com', 'name 4', 'surname 4', 'second_name 4', 'city 4'),
       (5, 'email1-5@gmail.com', 'name 5', 'surname 5', 'second_name 5', 'city 5'),
       (6, 'email1-6@gmail.com', 'name 6', 'surname 6', 'second_name 6', 'city 6'),
       (7, 'email1-7@gmail.com', 'name 7', 'surname 7', 'second_name 7', 'city 7'),
       (8, 'email1-8@gmail.com', 'name 8', 'surname 8', 'second_name 8', 'city 8'),
       (9, 'email1-9@gmail.com', 'name 9', 'surname 9', 'second_name 9', 'city 9'),
       (10, 'email1-10@gmail.com', 'name 10', 'surname 10', 'second_name 10', 'city 11'),
       (11, 'email1-11@gmail.com', 'name 11', 'surname 11', 'second_name 11', 'city 17'),
       (12, 'email1-12@gmail.com', 'name 12', 'surname 12', 'second_name 12', 'city 17'),
       (13, 'email1-13@gmail.com', 'name 13', 'surname 13', 'second_name 13', 'city 17'),
       (14, 'email1-14@gmail.com', 'name 14', 'surname 14', 'second_name 14', 'city 12');
--Check
SELECT * FROM potential_customers;

-- Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
SELECT pc.name, pc.email
FROM potential_customers pc
WHERE city = 'city 17'
UNION
SELECT u.first_name, u.email
FROM users u
WHERE city = 'city 17';

-- Задание 2
-- Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)
SELECT u.first_name, u.email
FROM users u
ORDER BY u.city, u.first_name;

-- Задание 3
-- Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества
SELECT c.category_title, COUNT(p.product_id) as count
FROM categories c
LEFT JOIN products p on c.category_id = p.categories_category_id
GROUP BY c.category_id
ORDER BY count DESC ;

-- Задание 4
-- 1. Вывести продукты, которые ни разу не попадали в корзину.
SELECT p.product_id, p.product_title
FROM products p
LEFT JOIN cart_product cp on p.product_id = cp.products_product_id
WHERE cp.products_product_id IS NULL;

-- Check
SELECT *
FROM cart_product cp
WHERE cp.products_product_id = 34;

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
SELECT p.product_id, p.product_title
FROM products p
LEFT JOIN cart_product cp on p.product_id = cp.products_product_id
LEFT JOIN carts c on c.cart_id = cp.carts_cart_id
LEFT JOIN orders o on c.cart_id = o.carts_cart_id
WHERE o.carts_cart_id IS NULL;

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT p.product_title, pc.count
FROM products p
JOIN
(SELECT cp.products_product_id as product_id, COUNT(cp.products_product_id) as count
FROM cart_product cp
GROUP BY cp.products_product_id) pc
ON pc.product_id = p.product_id
ORDER BY count DESC
LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT p.product_title, pc.count
FROM products p
JOIN
(SELECT cp.products_product_id as product_id, COUNT(cp.products_product_id) as count
FROM cart_product cp
JOIN carts c on c.cart_id = cp.carts_cart_id
JOIN orders o on cp.carts_cart_id = o.carts_cart_id WHERE o.carts_cart_id IS NOT NULL
GROUP BY cp.products_product_id) pc
ON pc.product_id = p.product_id
ORDER BY count DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT u.first_name, u.last_name, SUM(o.total) as sum
FROM users u
LEFT JOIN carts c on u.user_id = c.users_user_id
LEFT JOIN orders o on c.cart_id = o.carts_cart_id
LEFT JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name IN ('Paid', 'Finished')
GROUP BY u.first_name, u.last_name
ORDER BY sum DESC
LIMIT 5;



-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT u.first_name, u.last_name, COUNT(o.order_id) as count
FROM users u
LEFT JOIN carts c on u.user_id = c.users_user_id
LEFT JOIN orders o on c.cart_id = o.carts_cart_id
LEFT JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name IN ('Paid', 'Finished')
GROUP BY o.carts_cart_id, u.first_name, u.last_name
ORDER BY count  DESC
LIMIT 5;

--Check
SELECT * FROM carts;
SELECT * FROM orders;
INSERT INTO carts(cart_id, users_user_id, subtotal, total, timestamp)
VALUES (2001, 1, 500.00, 500.00, current_timestamp),
       (2002, 1, 500.00, 500.00, current_timestamp);
INSERT INTO orders(order_id, carts_cart_id, order_statuses_order_status_id,
                   shipping_total, total, created_at, updated_at)
                   VALUES (1501, 2001, 1, 500.00, 500.00, current_timestamp, current_timestamp);


-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT u.first_name, u.last_name
FROM users u
JOIN carts c on u.user_id = c.users_user_id
LEFT JOIN orders o on c.cart_id = o.carts_cart_id WHERE o.carts_cart_id IS NULL
ORDER BY u.first_name, u.last_name
LIMIT 5;
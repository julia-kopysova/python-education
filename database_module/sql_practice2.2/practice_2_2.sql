-- 1. всех юзеров
SELECT * FROM users;

-- 2. все продукты
SELECT * FROM products;

-- 3. все статусы заказов
SELECT * FROM order_statuses;

-- Вывести заказы, которые успешно доставлены и оплачены
SELECT *
FROM orders o
JOIN order_statuses os ON o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name IN ('Paid', 'Finished');

-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00
SELECT *
FROM products
WHERE price > 80.00 and price <= 150.00;

-- 2. заказы совершенные после 01.10.2020 (поле created_at)
SELECT *
FROM orders
WHERE created_at::date > date '2020-10-01';

-- 3. заказы полученные за первое полугодие 2020 года
SELECT *
FROM orders
WHERE created_at::date between '2020-01-01' and '2020-06-30'
ORDER BY created_at;

-- 4. подукты следующих категорий Category 7, Category 11, Category 18
SELECT *
FROM products p
JOIN categories c on p.categories_category_id = c.category_id
WHERE c.category_title IN ('Category 7', 'Category 11', 'Category 18');

-- 5. незавершенные заказы по состоянию на 31.12.2020
SELECT *
FROM orders o
JOIN order_statuses os ON o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name NOT IN ('Finished', 'Canceled')
  AND o.updated_at::date > '2020-12-31';

-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.
SELECT c.cart_id, c.users_user_id, c.subtotal, c.total, c.timestamp
FROM carts c
LEFT JOIN orders o on o.carts_cart_id = c.cart_id
WHERE o.carts_cart_id IS NULL;

-- 1. среднюю сумму всех завершенных сделок
SELECT AVG(o.total) average
FROM orders o
JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name = 'Finished';

-- 2. вывести максимальную сумму сделки за 3 квартал 2020
SELECT MAX(o.total) max_sum
FROM orders o
JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id
WHERE os.status_name = 'Finished' AND
      created_at::date between '2020-07-01' and '2020-09-30';

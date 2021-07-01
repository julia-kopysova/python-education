SELECT *
FROM potential_customers;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (15, 'email1-15@gmail.com', 'Tom', 'Smith', 'del', 'New York');
ROLLBACK;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (15, 'email1-15@gmail.com', 'Tom', 'Smith', 'del', 'New York');
COMMIT;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (16, 'email1-16@gmail.com', 'Kell', 'Smith', 'van', 'New York');
SAVEPOINT insert_point;
DELETE FROM potential_customers WHERE potential_customers_id = 17;
ROLLBACK TO SAVEPOINT insert_point;
COMMIT;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (17, 'email1-17@gmail.com', 'Mikki', 'Smith', 'van', 'New York');
UPDATE potential_customers SET name = 'Eldar' WHERE name = 'Mikki';
SAVEPOINT update_point;
DELETE FROM potential_customers WHERE name = 'Mikki';
ROLLBACK TO SAVEPOINT update_point;
COMMIT;


SELECT * FROM products;

BEGIN;
INSERT INTO products(product_id, product_title, product_description, in_stock, price, slug, categories_category_id)
VALUES (4001, 'Apple', 'Simple apple', 15, 30.00, 'apple', 2);
ROLLBACK;

BEGIN;
UPDATE products SET product_title = 'Banana' WHERE product_id = 2;
SAVEPOINT  update_product;
DELETE FROM products WHERE product_id = 10008000;
ROLLBACK TO SAVEPOINT update_product;
COMMIT;

BEGIN;
INSERT INTO cart_product(carts_cart_id, products_product_id)
VALUES (318, 3),
       (469, 3),
       (200, 3);
COMMIT;

SELECT *
FROM products
WHERE product_id = 3;

SELECT *
FROM cart_product
WHERE products_product_id = 3;

BEGIN;
DELETE FROM cart_product WHERE products_product_id = 3;
SAVEPOINT delete_product_cart;
DELETE FROM products WHERE product_id = 3;
ROLLBACK TO SAVEPOINT delete_product_cart;
COMMIT;

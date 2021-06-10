CREATE TABLE IF NOT EXISTS users (
	user_id serial PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	middle_name VARCHAR(255) NOT NULL,
	is_staff int2 NOT NULL,
	country VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
    address TEXT
);
CREATE TABLE IF NOT EXISTS categories (
	category_id serial PRIMARY KEY,
	category_title VARCHAR(255) UNIQUE NOT NULL,
    category_description TEXT
);
CREATE TABLE IF NOT EXISTS products (
	product_id serial PRIMARY KEY,
	product_title VARCHAR(255) UNIQUE NOT NULL,
	product_description TEXT,
	in_stock INT NOT NULL,
	price FLOAT NOT NULL,
	slug VARCHAR(45) NOT NULL,
	categories_category_id INT NOT NULL,
	FOREIGN KEY (categories_category_id)
      	REFERENCES categories(category_id)

);

CREATE TABLE IF NOT EXISTS carts (
   	cart_id serial PRIMARY KEY,
   	users_user_id INT NOT NULL,
   	subtotal DECIMAL NOT NULL,
	total DECIMAL NOT NULL,
	timestamp TIMESTAMP(2),
	FOREIGN KEY (users_user_id)
      		REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS cart_product (
  carts_cart_id INT NOT NULL,
  products_product_id INT NOT NULL,
  PRIMARY KEY (carts_cart_id, products_product_id),
  FOREIGN KEY (carts_cart_id)
      REFERENCES carts (cart_id),
  FOREIGN KEY (products_product_id)
      REFERENCES products (product_id)
);

CREATE TABLE IF NOT EXISTS order_statuses (
   	order_status_id serial PRIMARY KEY,
   	status_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS orders(
   	order_id serial PRIMARY KEY,
	carts_cart_id INT NOT NULL,
   	order_statuses_order_status_id INT NOT NULL,
   	shipping_total DECIMAL NOT NULL,
	total DECIMAL NOT NULL,
	created_at TIMESTAMP(2),
	updated_at TIMESTAMP(2),
	FOREIGN KEY (carts_cart_id)
      		REFERENCES carts(cart_id),
	FOREIGN KEY (order_statuses_order_status_id)
      		REFERENCES order_statuses(order_status_id)
);

COPY users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/usr/src/users.csv'
DELIMITER ','
CSV;

COPY categories(category_id, category_title, category_description)
FROM '/usr/src/categories.csv'
DELIMITER ','
CSV;

COPY products(product_id, product_title, product_description, in_stock, price, slug, categories_category_id)
FROM '/usr/src/products.csv'
DELIMITER ','
CSV;

COPY carts(cart_id, users_user_id, subtotal, total, timestamp)
FROM '/usr/src/carts.csv'
DELIMITER ','
CSV;

COPY cart_product (carts_cart_id, products_product_id)
FROM '/usr/src/cart_products.csv'
DELIMITER ','
CSV;

COPY order_statuses (order_status_id, status_name)
FROM '/usr/src/order_statuses.csv'
DELIMITER ','
CSV;

COPY orders (order_id, carts_cart_id, order_statuses_order_status_id, shipping_total, total, created_at, updated_at)
FROM '/usr/src/orders.csv'
DELIMITER ','
CSV;


SELECT * FROM users;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM carts;
SELECT * FROM order_statuses;
SELECT * FROM orders;

ALTER TABLE users
ADD COLUMN phone_number INT;
SELECT * FROM users;

ALTER TABLE users
ALTER COLUMN phone_number TYPE VARCHAR;

UPDATE products
SET price = price * 2;
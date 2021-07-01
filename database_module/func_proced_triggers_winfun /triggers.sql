CREATE TABLE changes_price (
   id INT GENERATED ALWAYS AS IDENTITY,
   product_id INT NOT NULL,
   old_price double precision NOT NULL,
   new_price double precision NOT NULL,
   date_changes TIMESTAMP(6) NOT NULL
);

CREATE OR REPLACE FUNCTION log_product_price_changes()
  RETURNS TRIGGER
  LANGUAGE plpgsql
  AS
$$
BEGIN
	IF NEW.price <> OLD.price THEN
		 INSERT INTO changes_price(product_id, old_price, new_price, date_changes)
		 VALUES(OLD.product_id,OLD.price,NEW.price,now());
	END IF;
	RETURN NEW;
END;$$;

CREATE TRIGGER product_price_changes
AFTER UPDATE
ON products
FOR EACH ROW
EXECUTE PROCEDURE log_product_price_changes();

UPDATE products SET price = 99.99 WHERE product_id = 1;
CALL increase_price_by_category('Category 1', 10.0);
SELECT * FROM changes_price;
DROP TRIGGER IF EXISTS product_price_changes ON products;

CREATE OR REPLACE FUNCTION delete_cart_product()
  RETURNS trigger
  LANGUAGE plpgsql
  AS
$$
BEGIN
   DELETE FROM cart_product WHERE cart_product.carts_cart_id = OLD.cart_id;
   DELETE FROM orders WHERE carts_cart_id = OLD.cart_id;
   RETURN OLD;
END;$$;

CREATE TRIGGER delete_cart
   BEFORE DELETE ON carts
   FOR EACH ROW
   EXECUTE PROCEDURE delete_cart_product();

BEGIN;

DELETE FROM carts WHERE cart_id = 8;

SELECT * FROM orders WHERE order_id = 8;

SELECT o.order_id, p.product_title, o.total, cp.products_product_id
FROM orders o
JOIN carts c on o.carts_cart_id = c.cart_id
JOIN cart_product cp on c.cart_id = cp.carts_cart_id
JOIN products p on cp.products_product_id = p.product_id
WHERE cp.carts_cart_id = 8;

ROLLBACK;
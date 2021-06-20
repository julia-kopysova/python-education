CREATE OR REPLACE FUNCTION update_shipping_total(city_name varchar) RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM users
          WHERE city = city_name) THEN
      UPDATE orders SET shipping_total = 0
        WHERE carts_cart_id IN (SELECT o.carts_cart_id
        FROM users u
        JOIN carts c on u.user_id = c.users_user_id
        JOIN orders o on c.cart_id = o.carts_cart_id WHERE u.city = city_name);
    ELSE
        RAISE EXCEPTION '% not found', city_name;
    END IF;
END;
$$;

-- проверка
BEGIN;
SELECT update_shipping_total('city 1');
SELECT u.city, o.shipping_total
FROM users u
JOIN carts c on u.user_id = c.users_user_id
JOIN orders o on c.cart_id = o.carts_cart_id WHERE u.city = 'city 1';
SELECT update_shipping_total('city 19999');
ROLLBACK;

-- использование циклов
CREATE OR REPLACE FUNCTION get_product(pattern varchar)
RETURNS TABLE(
    product_id int,
	product_title varchar
)
LANGUAGE plpgsql
AS $$
DECLARE
    product record;
BEGIN
	FOR product IN ( SELECT product_id, product_title
	                FROM products
	                WHERE product_title ILIKE pattern)
    LOOP
	    product_title := product.product_title;
		product_id := product.product_id;
        RETURN NEXT;
	end loop;
end; $$;

SELECT get_product('1');
CREATE OR REPLACE PROCEDURE increase_price_by_category(need_category_name varchar,
                                                       percent float)
LANGUAGE plpgsql
AS $$
DECLARE
    need_category_id int;
BEGIN
    IF percent > 0 THEN
        IF EXISTS(SELECT 1 FROM categories WHERE category_title = need_category_name) THEN
            SELECT INTO need_category_id category_id
                    FROM categories
                    WHERE category_title = need_category_name;
            UPDATE products SET price = price + price*percent/100
                    WHERE categories_category_id = need_category_id;
        COMMIT;
        ELSE
            RAISE EXCEPTION '% was not found', need_category_name;
        END IF;
    ELSE
        RAISE EXCEPTION 'Percent less than 0';
    END IF;
END;
$$;

DROP PROCEDURE increase_price_by_category(category_name varchar, percent float);

CALL increase_price_by_category('Category 1', 10.0);
CALL increase_price_by_category('Category 111111111', 10.0);
CALL increase_price_by_category('Category 1', -10.0);


SELECT p.product_id, p.price FROM products p
JOIN categories c on c.category_id = p.categories_category_id
WHERE c.category_title = 'Category 1';

CREATE OR REPLACE PROCEDURE subtract_in_stock(update_product_id int,
                                              amount int)
LANGUAGE plpgsql
AS $$
DECLARE
    new_amount int;
BEGIN
    UPDATE products SET in_stock = in_stock - amount WHERE product_id = update_product_id
        RETURNING in_stock
        INTO new_amount;
    IF new_amount >= 0 THEN
        COMMIT;
    ELSE
        ROLLBACK;
        RAISE EXCEPTION 'Amount is more than products exist';
    END IF;
END;
$$;

CALL subtract_in_stock(2, 2);
CALL subtract_in_stock(2, 222);
SELECT * FROM products WHERE product_id = 2;
DROP PROCEDURE subtract_in_stock;

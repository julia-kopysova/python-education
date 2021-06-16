-- cost 0.00..4.76 with index
-- cost 0.00..31.76 with seq scan
EXPLAIN (ANALYSE) SELECT o.order_id
FROM orders o
WHERE o.total < 80.00;

CREATE INDEX IF NOT EXISTS idx_orders_total ON orders USING btree (total);
DROP INDEX idx_orders_total;

SET enable_seqscan TO off;
SET enable_seqscan TO on;

-- Check if use '>'
-- cost 0.00..31.78 with seq scan
-- cost 0.00..39.05 with index
EXPLAIN (ANALYSE) SELECT o.order_id
FROM orders o
WHERE o.total > 80.00;

-- from 38.39 to 33.05
CREATE INDEX IF NOT EXISTS idx_orders_updated_at ON orders USING btree(updated_at);
DROP INDEX idx_orders_updated_at;

EXPLAIN (ANALYSE) SELECT o.order_id, os.status_name
FROM orders o
JOIN order_statuses os on o.order_statuses_order_status_id = os.order_status_id
WHERE o.updated_at BETWEEN '2020-01-08 14:40:47' and '2021-01-29 14:50:47';


-- from 165.00 to 17.46
CREATE INDEX IF NOT EXISTS idx_products_price ON products USING btree(price);
DROP INDEX idx_products_price;

CREATE INDEX IF NOT EXISTS idx_products_not_in_stock ON products USING btree(in_stock) WHERE in_stock = 0;
DROP INDEX idx_products_not_in_stock;

EXPLAIN (ANALYSE) SELECT p.product_id, p.product_title, p.price, p.in_stock
FROM products p
WHERE p.in_stock = 0 and p.price <= 10.00;
SELECT
	p.product_title,
	p.price,
	c.category_title,
	AVG(p.price) OVER (
	   PARTITION BY c.category_title
	)
FROM products p
JOIN categories c on p.categories_category_id = c.category_id;
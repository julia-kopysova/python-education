-- сколько принесли прибыли бренчам зарегистривованные кастомеры
CREATE MATERIALIZED VIEW sum_by_branch AS
    SELECT
        b.branch_id, r.customer_id,
        SUM(r.period_renting * c.price) as sum
    FROM branch b
        JOIN car c on b.branch_id = c.branch_id
        JOIN renting r on c.car_id = r.car_id
        LEFT JOIN customer c2 on c2.customer_id = r.customer_id
    WHERE r.customer_id IS NOT NULL
    GROUP BY b.branch_id, r.customer_id
    ORDER BY sum DESC
WITH NO DATA;

REFRESH MATERIALIZED VIEW sum_by_branch;

SELECT * FROM sum_by_branch;
DROP MATERIALIZED VIEW IF EXISTS sum_by_branch;
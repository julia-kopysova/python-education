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

-- детальная информация про машину
CREATE OR REPLACE VIEW car_info AS
    SELECT
            c.car_number,
            c.price,
            m.model_name,
            m2.manufacture_name,
            ce.capacity,
            t.type_name,
            c2.quantity
        FROM car c
        LEFT JOIN branch b on b.branch_id = c.branch_id
        LEFT JOIN model m on m.model_id = c.model_id
        LEFT JOIN manufacture m2 on m2.manufacture_id = m.manufacture_id
        LEFT JOIN equipment e on e.equipment_id = m.equipment_id
        LEFT JOIN capacity_engine ce on e.capacity_engine_id = ce.capacity_engine_id
        LEFT JOIN transmission t on t.transmission_id = e.transmission_id
        LEFT JOIN cylinder c2 on c2.cylinder_id = e.cylinder_id;

SELECT * FROM car_info;
DROP VIEW IF EXISTS car_info;

-- информация про кастомеров
CREATE OR REPLACE VIEW customer_renting AS
    SELECT
        c.first_name,
        c.last_name,
        r.date_renting,
        r.period_renting,
        c2.car_number,
        b.branch_id
    FROM customer c
    JOIN renting r on c.customer_id = r.customer_id
    JOIN car c2 on c2.car_id = r.car_id
    JOIN branch b on b.branch_id = c2.branch_id;

SELECT * FROM customer_renting;
DROP VIEW IF EXISTS customer_renting;
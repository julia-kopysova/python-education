-- в какой бренче было больше всего не долгосрочных аренд за 2018
-- from 855.54 to 255.80
EXPLAIN (ANALYSE) SELECT b.branch_id, COUNT(r.period_renting) as sum
FROM branch b
LEFT JOIN car c on b.branch_id = c.branch_id
LEFT JOIN renting r on c.car_id = r.car_id
WHERE r.period_renting < 10 AND r.date_renting:: date BETWEEN '2018-01-01' AND '2019-01-01'
GROUP BY b.branch_id
ORDER BY sum DESC;

CREATE INDEX IF NOT EXISTS idx_renting_period_renting ON renting USING btree (period_renting);
CREATE INDEX IF NOT EXISTS idx_renting_date_renting ON renting USING btree(date_renting);

DROP INDEX idx_renting_date_renting;
DROP INDEX idx_renting_period_renting;

-- from cost 1086.64 to 987.02
EXPLAIN (ANALYSE)
SELECT c.car_number, b.branch_id, ce.capacity,  SUM(r.period_renting * c.price)  as sum
FROM car c
LEFT JOIN branch b on c.branch_id = b.branch_id
LEFT JOIN model m on m.model_id = c.model_id
JOIN renting r on c.car_id = r.car_id
LEFT JOIN equipment e on e.equipment_id = m.equipment_id
LEFT JOIN capacity_engine ce on ce.capacity_engine_id = e.capacity_engine_id
    WHERE capacity BETWEEN 3 AND 5 AND c.price <= 100.00
GROUP BY c.car_number, b.branch_id, ce.capacity
ORDER BY sum DESC;

CREATE INDEX IF NOT EXISTS idx_car_price ON car USING btree(price);
CREATE INDEX IF NOT EXISTS idx_capacity_engine_capacity ON capacity_engine USING btree(capacity);

DROP INDEX idx_car_price;
DROP INDEX idx_capacity_engine_capacity;

-- from cost 24.63 to 16.05
EXPLAIN (ANALYSE) SELECT c.car_number, m.model_name
FROM model m
LEFT JOIN car c on m.model_id = c.model_id
WHERE m.model_name = 'model 166' AND c.car_number = 19278;

CREATE INDEX IF NOT EXISTS idx_model_name ON model USING hash(model_name);
CREATE INDEX IF NOT EXISTS  idx_car_car_number ON car USING hash(car_number);

DROP INDEX idx_model_name;
DROP INDEX idx_car_car_number;
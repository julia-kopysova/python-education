CREATE OR REPLACE VIEW date_interval_renting AS
    SELECT c.car_id, r.date_renting, r.date_renting + make_interval(days => r.period_renting) AS date_end
    FROM car c
    JOIN renting r on c.car_id = r.car_id;

SELECT * FROM date_interval_renting;
DROP VIEW IF EXISTS date_interval_renting;

-- если машина занята, то невозможно её арендовать
CREATE OR REPLACE PROCEDURE insert_renting(n_date_renting timestamp,
                                           n_period_renting int,
                                           n_car_id int,
                                           n_customer_id int)
LANGUAGE plpgsql
AS $$
DECLARE
    n_date_end timestamp;
BEGIN
    SELECT INTO n_date_end MAX(date_end) FROM date_interval_renting
        WHERE car_id = n_car_id;
    INSERT INTO renting(renting_id, date_renting, period_renting, car_id, customer_id)
        VALUES (DEFAULT, n_date_renting, n_period_renting, n_car_id, n_customer_id);
    IF n_date_end IS NULL OR n_date_renting >= n_date_end THEN
        COMMIT;
    ELSE
        ROLLBACK;
        RAISE EXCEPTION 'Car is being rented now';
    END IF;
END;
$$;

-- 2020-04-25 02:36:19.129956
CALL insert_renting('2020-04-30 02:36:19.129956', 10, 3, 120);
DROP PROCEDURE IF EXISTS insert_renting(n_date_renting timestamp, n_period_renting int,
                                        n_car_id int, n_customer_id int);

CREATE OR REPLACE PROCEDURE update_branch_address(n_branch_id int,
                                                  n_address_id int)
LANGUAGE plpgsql
AS $$
DECLARE
    branch_by_address int;
BEGIN
    SELECT INTO branch_by_address branch_id
        FROM branch
        WHERE address_id = n_address_id
        LIMIT 1;
    UPDATE branch SET address_id = n_address_id
        WHERE branch_id = n_branch_id;
    IF branch_by_address IS NULL THEN
        COMMIT;
    ELSE
        ROLLBACK;
        RAISE EXCEPTION 'Branch % has been registered in this address', branch_by_address;
    END IF;
END;
$$;

DROP PROCEDURE IF EXISTS update_branch_address(n_branch_id int, n_address_id int);

CALL update_branch_address(1,1262);
CALL update_branch_address(1,1);
SELECT * FROM branch WHERE branch_id = 1;
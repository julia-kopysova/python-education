-- возвращает машину и сколько раз её арендовывали по введённому бренчу
CREATE OR REPLACE FUNCTION get_cars_by_branch(n_branch_id int)
RETURNS TABLE(
    current_car_id int,
	current_car_number int,
	current_amount_rented int,
	current_model_name varchar
)
LANGUAGE plpgsql
AS $$
DECLARE
    car_info record;
BEGIN
	FOR car_info IN ( SELECT r.car_id, c.car_number, COUNT(r.car_id) as amount_rented, m.model_name
                    FROM car c
                    JOIN renting r on c.car_id = r.car_id
                    LEFT OUTER JOIN model m on m.model_id = c.model_id
                    WHERE c.branch_id = n_branch_id
                    GROUP BY c.car_number, r.car_id, m.model_name
                    ORDER BY amount_rented DESC )
    LOOP
	    current_car_id := car_info.car_id;
		current_amount_rented := car_info.amount_rented;
	    current_car_number := car_info.car_number;
	    current_model_name := car_info.model_name;
        RETURN NEXT;
	end loop;
end; $$;

SELECT * FROM get_cars_by_branch(3);
DROP FUNCTION IF EXISTS get_cars_by_branch(n_branch_id int);

-- возвращает юзера и сколько он потратил денег
CREATE OR REPLACE FUNCTION get_top_n_customer(n_top int)
RETURNS TABLE(
    cur_first_name varchar,
	cur_last_name varchar,
	cur_sum double precision
)
LANGUAGE plpgsql
AS $$
DECLARE
    user_info record;
BEGIN
	FOR user_info IN (   SELECT c.first_name, c.last_name, SUM(c2.price * r.period_renting) as sum
                        FROM customer c
                        LEFT JOIN renting r on c.customer_id = r.customer_id
                        LEFT JOIN car c2 on r.car_id = c2.car_id
                        GROUP BY c.first_name, c.last_name
                        ORDER BY sum DESC
                        NULLS LAST
	                    LIMIT n_top)
    LOOP
	    cur_first_name := user_info.first_name;
		cur_last_name := user_info.last_name;
	    cur_sum := user_info.sum;
        RETURN NEXT;
	end loop;
end; $$;

SELECT * FROM get_top_n_customer(100);
DROP FUNCTION IF EXISTS get_top_n_customer(n_top int);

-- функция расчитывает цену
CREATE OR REPLACE FUNCTION calculate_price(n_car_number int, n_days int)
RETURNS double precision
LANGUAGE plpgsql
AS $$
DECLARE
    sum double precision;
BEGIN
    IF EXISTS(SELECT 1 FROM car WHERE car_number = n_car_number) THEN
        SELECT INTO sum price*n_days
        FROM car
        WHERE car_number = n_car_number;
        RETURN sum;
    ELSE
        RAISE EXCEPTION 'Car % was not found', n_car_number;
    END IF;
 end;
$$;

SELECT calculate_price(13005, 3);
DROP FUNCTION IF EXISTS calculate_price(n_car_number int, n_days int);
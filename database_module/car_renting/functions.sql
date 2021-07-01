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

-- поиск машин по производителю, которые не заняты
CREATE OR REPLACE FUNCTION get_car_by_manufacture(n_manufacture_name varchar)
   RETURNS TABLE(
       car_number int,
       branch_id int,
       model_name varchar,
       price double precision
                )
LANGUAGE plpgsql
AS $$
DECLARE
	rec_car record;
    date_end timestamp;
	cur_cars cursor(cur_manufacture_name varchar)
		 FOR SELECT c.car_id, c.car_number, b.branch_id, m.model_name, c.price
		 FROM model m
		 JOIN manufacture m2 on m2.manufacture_id = m.manufacture_id
		 JOIN car c on m.model_id = c.model_id
		 JOIN branch b on b.branch_id = c.branch_id
		 WHERE m2.manufacture_name = cur_manufacture_name
         ORDER BY c.price;
BEGIN
   OPEN cur_cars(n_manufacture_name);
   LOOP
      FETCH cur_cars INTO rec_car;
      EXIT WHEN NOT found;
      SELECT INTO date_end MAX(date_renting + make_interval(days => period_renting))
          FROM renting
          WHERE car_id = rec_car.car_id;

      IF date_end < now() THEN
             car_number := rec_car.car_number;
             branch_id := rec_car.branch_id;
             model_name := rec_car.model_name;
             price := rec_car.price;
             RETURN NEXT;
      END IF;
   END LOOP;
   CLOSE cur_cars;
end; $$;

DROP FUNCTION IF EXISTS get_car_by_manufacture(n_manufacture_name varchar);
SELECT * FROM get_car_by_manufacture('manufacture 2');
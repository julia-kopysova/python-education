-- city
CREATE SEQUENCE seq_city_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
SELECT nextval('seq_city_name');
DROP SEQUENCE seq_city_name;
CREATE OR REPLACE FUNCTION insert_city(amount int) RETURNS TABLE(
    city_name varchar
                                                                )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            city_name := 'city '||nextval('seq_city_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_city_name RESTART;
    end;
$$;

INSERT INTO city(city_name)
SELECT city_name FROM insert_city(50);

SELECT insert_city(50);
SELECT * FROM city;

ALTER SEQUENCE IF EXISTS seq_city_name RESTART;
SELECT nextval('seq_city_name');

-- street
CREATE SEQUENCE seq_street_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
CREATE OR REPLACE FUNCTION insert_street(amount int) RETURNS table(
    street_name varchar
                                                                  )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            street_name := 'street '||nextval('seq_street_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_street_name RESTART;
    end;
$$;

INSERT INTO street(street_name)
SELECT street_name FROM insert_street(50);

SELECT * FROM street;

-- house
CREATE SEQUENCE seq_house_number AS bigint INCREMENT 1 MAXVALUE 100 CYCLE;
CREATE OR REPLACE FUNCTION insert_house(amount int) RETURNS table(
    house_number int
                                                                 )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            house_number := nextval('seq_house_number');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_house_number RESTART;
    end;
$$;

INSERT INTO house(house_number)
SELECT house_number FROM insert_house(50);

SELECT * FROM house;

-- address
CREATE OR REPLACE FUNCTION insert_address(amount_full int, amount_null int) RETURNS table(
    city_id int,
    street_id int,
    house_id int,
    phone_number varchar
                                                                                        )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO city_id floor(random()*(50-1+1))+1;
            SELECT INTO street_id floor(random()*(50-1+1))+1;
            SELECT INTO house_id floor(random()*(100-1+1))+1;
            SELECT INTO phone_number '099'||floor(random()*(8909870-1+9999999))+1;
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO city_id floor(random()*(50-1+1))+1;
            street_id := null;
            house_id := null;
            phone_number := null;
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    end;
$$;

INSERT INTO address(city_id, street_id, house_id, phone_number)
SELECT city_id, street_id, house_id, phone_number FROM insert_address(1000, 500);

SELECT * FROM address;

SELECT c.city_name ||' '|| s.street_name ||', '||  h.house_number as address
FROM address a
LEFT JOIN city c on a.city_id = c.city_id
JOIN street s on a.street_id = s.street_id
JOIN house h on a.house_id = h.house_id;

-- branch
CREATE OR REPLACE FUNCTION insert_branch(amount int) RETURNS table(
    address_id int
                                                                  )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            SELECT INTO address_id floor(random()*(1500-1+1))+1;
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
    end;
$$;

INSERT INTO branch(address_id)
SELECT address_id FROM insert_branch(500);

SELECT * FROM branch;

-- capacity_engine
CREATE OR REPLACE FUNCTION insert_capacity_engine(amount int) RETURNS table(
    capacity double precision
                                                                           )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            SELECT INTO capacity ROUND((random()*5+1)::numeric,2);
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
    end;
$$;
SELECT ROUND((random()*5+1)::numeric,2);

INSERT INTO capacity_engine(capacity)
SELECT capacity FROM insert_capacity_engine(10);

SELECT * FROM capacity_engine;
DROP TABLE capacity_engine CASCADE;
TRUNCATE TABLE capacity_engine;


-- transmission
CREATE SEQUENCE seq_transmission_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
CREATE OR REPLACE FUNCTION insert_transmission(amount int) RETURNS table(
    type_name varchar
                                                                        )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            type_name := 'type '||nextval('seq_transmission_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
    end;
$$;

INSERT INTO transmission(type_name)
SELECT type_name FROM insert_transmission(50);

SELECT * FROM transmission;
DROP TABLE transmission CASCADE;

-- cylinder
CREATE SEQUENCE seq_cylinder AS bigint INCREMENT 1 MAXVALUE 8 CYCLE;
CREATE OR REPLACE FUNCTION insert_cylinder(amount int) RETURNS table(
    quantity int
                                                                    )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            quantity := nextval('seq_cylinder');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
    end;
$$;

INSERT INTO cylinder(quantity)
SELECT quantity FROM insert_cylinder(8);

SELECT * FROM cylinder;
DROP TABLE cylinder CASCADE ;

-- equipment
CREATE OR REPLACE FUNCTION insert_equipment(amount int) RETURNS table(
    cylinder_id int,
    transmission_id int,
    capacity_id int
                                                                     )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            SELECT INTO cylinder_id floor(random()*(8-1+1))+1;
            SELECT INTO transmission_id floor(random()*(50-1+1))+1;
            SELECT INTO capacity_id floor(random()*(10-1+1))+1;
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    end;
$$;

INSERT INTO equipment(cylinder_id, transmission_id, capacity_engine_id)
SELECT cylinder_id, transmission_id, capacity_id FROM insert_equipment(2000);

SELECT * FROM equipment;

-- manufacture
CREATE SEQUENCE seq_manufacture_name AS bigint INCREMENT 1 MAXVALUE 1000 CYCLE;
SELECT nextval('seq_manufacture_name');
DROP SEQUENCE seq_manufacture_name;
CREATE OR REPLACE FUNCTION insert_manufacture(amount int) RETURNS table(
    manufacture_name varchar
                                                                       )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            manufacture_name := 'manufacture '||nextval('seq_manufacture_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_manufacture_name RESTART;
    end;
$$;

INSERT INTO manufacture(manufacture_name)
SELECT manufacture_name FROM insert_manufacture(1000);

SELECT * FROM manufacture;
DROP TABLE manufacture CASCADE;

-- model
CREATE SEQUENCE seq_model_name AS bigint INCREMENT 1 MAXVALUE 9000 CYCLE;
CREATE OR REPLACE FUNCTION insert_model(amount_full int, amount_null int) RETURNS table(
    model_name varchar,
    manufacture_id int,
    equipment_id int
                                                                                       )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO equipment_id floor(random()*(1560-1+1))+1;
            SELECT INTO manufacture_id floor(random()*(1000-1+1))+1;
            model_name := 'model '||nextval('seq_model_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO manufacture_id floor(random()*(1000-1+1))+1;
            model_name := 'model '||nextval('seq_model_name');
            equipment_id := null;
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    ALTER SEQUENCE IF EXISTS seq_model_name RESTART;
    end;
$$;

INSERT INTO model(model_name, manufacture_id, equipment_id)
SELECT model_name, manufacture_id, equipment_id FROM insert_model(3000, 6000);

SELECT * FROM model;
SELECT COUNT(*) FROM manufacture;
DROP TABLE model CASCADE ;
SELECT COUNT(*) FROM equipment;

-- car
CREATE SEQUENCE seq_car_number AS bigint INCREMENT 1 MINVALUE 1000 MAXVALUE 99999;
DROP SEQUENCE seq_car_number;
CREATE OR REPLACE FUNCTION insert_car(amount int) RETURNS table(
    car_number int,
    price numeric(5,2),
    branch_id int,
    model_id int

                                                               )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            SELECT INTO branch_id floor(random()*(500-1+1))+1;
            SELECT INTO model_id floor(random()*(9000-1+1))+1;
            SELECT INTO price ROUND((random()*800+1)::numeric,2);
            car_number := nextval('seq_car_number');
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    end;
$$;

INSERT INTO car(car_number, price, branch_id, model_id)
SELECT car_number, price, branch_id, model_id FROM insert_car(12000);

SELECT * FROM car;
SELECT COUNT(*) FROM model; --9000
SELECT COUNT(*) FROM branch; --500
SELECT * FROM model;
SELECT * FROM car;
SELECT b.branch_id, COUNT(*)
FROM car c
JOIN branch b USING(branch_id)
GROUP BY b.branch_id
ORDER BY b.branch_id;

BEGIN;
DROP TABLE car CASCADE;
COMMIT;

-- renting
SELECT count(*) FROM customer;
CREATE OR REPLACE FUNCTION insert_renting(amount_full int, amount_null int) RETURNS table(
    date_renting timestamp,
    period_renting int,
    car_id int,
    customer_id int
                                                                                         )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO car_id floor(random()*(12000-1+1))+1;
            SELECT INTO customer_id floor(random()*(10000-1+1))+1;
            SELECT INTO period_renting floor(random()*(300-1+1))+1;
            SELECT INTO date_renting timestamp '2014-01-10 20:00:00' + random() * (timestamp '2021-01-20 20:00:00' -
                                                                 timestamp '2014-01-01 10:00:00');
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO car_id floor(random()*(12000-1+1))+1;
            SELECT INTO period_renting floor(random()*(300-1+1))+1;
            SELECT INTO date_renting timestamp '2014-01-10 20:00:00' + random() * (timestamp '2021-01-20 20:00:00' -
                                                                 timestamp '2014-01-01 10:00:00');
            customer_id := NULL;
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    end;
$$;

INSERT INTO renting(date_renting, period_renting, car_id, customer_id)
SELECT date_renting, period_renting, car_id, customer_id FROM insert_renting(7000,7000);

SELECT * FROM renting;

-- customer
CREATE SEQUENCE seq_customer_name AS bigint INCREMENT 1 MAXVALUE 10000 CYCLE;
CREATE SEQUENCE seq_customer_last_name AS bigint INCREMENT 1 MAXVALUE 10000 CYCLE;
CREATE OR REPLACE FUNCTION insert_customer(amount_full int, amount_null int) RETURNS table(
    first_name varchar,
    last_name varchar,
    address_id int
                                                                                          )
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO address_id floor(random()*(1500-1+1))+1;
            first_name := 'first name '||nextval('seq_customer_name');
            last_name := 'last name '||nextval('seq_customer_last_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            address_id := null;
            first_name := 'first name '||nextval('seq_customer_name');
            last_name := 'last name '||nextval('seq_customer_last_name');
            current_amount = current_amount + 1;
            RETURN NEXT;
        end loop;
    ALTER SEQUENCE IF EXISTS seq_customer_name RESTART;
    ALTER SEQUENCE IF EXISTS seq_customer_last_name RESTART;
    end;
$$;

INSERT INTO customer(first_name, last_name, address_id)
SELECT first_name, last_name, address_id FROM insert_customer(7000,7000);
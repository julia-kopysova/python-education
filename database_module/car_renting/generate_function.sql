-- city
CREATE SEQUENCE seq_city_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
SELECT nextval('seq_city_name');
DROP SEQUENCE seq_city_name;
CREATE OR REPLACE FUNCTION insert_city(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            INSERT INTO city(city_id, city_name) VALUES (DEFAULT, 'city '||nextval('seq_city_name'));
            current_amount = current_amount + 1;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_city_name RESTART;
    end;
$$;
SELECT insert_city(50);
SELECT * FROM city;
ALTER SEQUENCE IF EXISTS seq_city_name RESTART;
SELECT nextval('seq_city_name');

-- street
CREATE SEQUENCE seq_street_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
CREATE OR REPLACE FUNCTION insert_street(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            INSERT INTO street(street_id, street_name) VALUES (DEFAULT, 'street '||nextval('seq_street_name'));
            current_amount = current_amount + 1;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_street_name RESTART;
    end;
$$;
SELECT insert_street(50);
SELECT * FROM street;

-- house
CREATE SEQUENCE seq_house_number AS bigint INCREMENT 1 MAXVALUE 100 CYCLE;
CREATE OR REPLACE FUNCTION insert_house(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            INSERT INTO house(house_id, house_number) VALUES (DEFAULT, nextval('seq_house_number'));
            current_amount = current_amount + 1;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_house_number RESTART;
    end;
$$;
SELECT insert_house(100);
SELECT * FROM house;

-- address
CREATE OR REPLACE FUNCTION insert_address(amount_full int, amount_null int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_city_id int := 0;
        new_street_id int := 0;
        new_house_id int := 0;
        current_amount int := 0;
        new_phone_number int :=0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO new_city_id floor(random()*(50-1+1))+1;
            SELECT INTO new_street_id floor(random()*(50-1+1))+1;
            SELECT INTO new_house_id floor(random()*(100-1+1))+1;
            SELECT INTO new_phone_number floor(random()*(8909870-1+9999999))+1;
            INSERT INTO address(address_id, city_id, street_id, house_id, phone_number)
                VALUES (DEFAULT, new_city_id, new_street_id, new_house_id, '099'||new_phone_number);
            current_amount = current_amount + 1;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO new_city_id floor(random()*(50-1+1))+1;
            INSERT INTO address(address_id, city_id, street_id, house_id, phone_number)
                VALUES (DEFAULT, new_city_id, NULL, NULL, NULL);
            current_amount = current_amount + 1;
        end loop;
    end;
$$;

SELECT insert_address(1000, 500);
SELECT * FROM address;
SELECT c.city_name ||' '|| s.street_name ||', '||  h.house_number as address
FROM address a
LEFT JOIN city c on a.city_id = c.city_id
JOIN street s on a.street_id = s.street_id
JOIN house h on a.house_id = h.house_id;

-- branch
CREATE OR REPLACE FUNCTION insert_branch(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
        new_address int :=0;
    BEGIN
    loop
            exit when current_amount = amount;
            SELECT INTO new_address floor(random()*(1500-1+1))+1;
            INSERT INTO branch(branch_id, address_id) VALUES (DEFAULT, new_address);
            current_amount = current_amount + 1;
            end loop;
    end;
$$;
SELECT insert_branch(500);
SELECT * FROM branch;

-- capacity_engine
CREATE OR REPLACE FUNCTION insert_capacity_engine(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
        new_capacity double precision :=0;
    BEGIN
    loop
            exit when current_amount = amount;
            SELECT INTO new_capacity ROUND((random()*5+1)::numeric,2);
            INSERT INTO capacity_engine(capacity_engine_id, capacity) VALUES (DEFAULT, new_capacity);
            current_amount = current_amount + 1;
            end loop;
    end;
$$;
SELECT ROUND((random()*5+1)::numeric,2);
SELECT insert_capacity_engine(10);
SELECT * FROM capacity_engine;
DROP TABLE capacity_engine CASCADE;
TRUNCATE TABLE capacity_engine;


-- transmission
CREATE SEQUENCE seq_transmission_name AS bigint INCREMENT 1 MAXVALUE 50 CYCLE;
CREATE OR REPLACE FUNCTION insert_transmission(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            INSERT INTO transmission(transmission_id, type_name)
                VALUES (DEFAULT, 'type '||nextval('seq_transmission_name'));
            current_amount = current_amount + 1;
            end loop;
    end;
$$;
SELECT insert_transmission(50);
SELECT * FROM transmission;
DROP TABLE transmission CASCADE ;

-- cylinder
CREATE SEQUENCE seq_cylinder AS bigint INCREMENT 1 MAXVALUE 8 CYCLE;
CREATE OR REPLACE FUNCTION insert_cylinder(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
    loop
            exit when current_amount = amount;
            INSERT INTO cylinder(cylinder_id, quantity)
                VALUES (DEFAULT, nextval('seq_cylinder'));
            current_amount = current_amount + 1;
            end loop;
    end;
$$;
SELECT insert_cylinder(8);
SELECT * FROM cylinder;
DROP TABLE cylinder CASCADE ;

-- equipment
CREATE OR REPLACE FUNCTION insert_equipment(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_cylinder_id int := 0;
        new_transmission_id int := 0;
        new_capacity_id int := 0;
        current_amount int := 0;
        id int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            SELECT INTO new_cylinder_id floor(random()*(8-1+1))+1;
            SELECT INTO new_transmission_id floor(random()*(50-1+1))+1;
            SELECT INTO new_capacity_id floor(random()*(10-1+1))+1;
            SELECT INTO id equipment_id
                FROM equipment
                WHERE cylinder_id = new_cylinder_id AND
                      transmission_id = new_transmission_id AND
                      capacity_engine_id = new_capacity_id;
            IF id is null THEN
                INSERT INTO equipment(equipment_id, cylinder_id, transmission_id, capacity_engine_id)
                    VALUES (DEFAULT, new_cylinder_id, new_transmission_id, new_capacity_id);
            ELSE
                id = 0;
            END IF;
            current_amount = current_amount + 1;
        end loop;
    end;
$$;

SELECT insert_equipment(2000);
SELECT * FROM equipment;

-- manufacture
CREATE SEQUENCE seq_manufacture_name AS bigint INCREMENT 1 MAXVALUE 1000 CYCLE;
SELECT nextval('seq_manufacture_name');
DROP SEQUENCE seq_manufacture_name;
CREATE OR REPLACE FUNCTION insert_manufacture(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            INSERT INTO manufacture(manufacture_id, manufacture_name)
                VALUES (DEFAULT, 'manufacture '||nextval('seq_manufacture_name'));
            current_amount = current_amount + 1;
            end loop;
        ALTER SEQUENCE IF EXISTS seq_manufacture_name RESTART;
    end;
$$;
SELECT insert_manufacture(1000);
SELECT * FROM manufacture;
DROP TABLE manufacture CASCADE;

-- model
CREATE SEQUENCE seq_model_name AS bigint INCREMENT 1 MAXVALUE 9000 CYCLE;
CREATE OR REPLACE FUNCTION insert_model(amount_full int, amount_null int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_manufacture_id int := 0;
        new_equipment_id int := 0;
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO new_equipment_id floor(random()*(1560-1+1))+1;
            SELECT INTO new_manufacture_id floor(random()*(1000-1+1))+1;
            INSERT INTO model(model_id, model_name, manufacture_id, equipment_id)
                VALUES (DEFAULT, 'model '||nextval('seq_model_name'), new_manufacture_id, new_equipment_id);
            current_amount = current_amount + 1;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO new_manufacture_id floor(random()*(1000-1+1))+1;
            INSERT INTO model(model_id, model_name, manufacture_id, equipment_id)
                VALUES (DEFAULT, 'model '||nextval('seq_model_name'), new_manufacture_id, NULL);
            current_amount = current_amount + 1;
        end loop;
    ALTER SEQUENCE IF EXISTS seq_model_name RESTART;
    end;
$$;


SELECT insert_model(3000, 6000);
SELECT * FROM model;
SELECT COUNT(*) FROM manufacture;
DROP TABLE model CASCADE ;
SELECT COUNT(*) FROM equipment;

-- car
CREATE SEQUENCE seq_car_number AS bigint INCREMENT 1 MINVALUE 1000 MAXVALUE 99999;
DROP SEQUENCE seq_car_number;
CREATE OR REPLACE FUNCTION insert_car(amount int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_branch_id int := 0;
        new_model_id int := 0;
        new_price numeric(5,2) := 0;
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount;
            SELECT INTO new_branch_id floor(random()*(500-1+1))+1;
            SELECT INTO new_model_id floor(random()*(9000-1+1))+1;
            SELECT INTO new_price ROUND((random()*800+1)::numeric,2);
            INSERT INTO car(car_id, car_number, price, branch_id, model_id)
                VALUES (DEFAULT, nextval('seq_car_number'), new_price, new_branch_id, new_model_id);
            current_amount = current_amount + 1;
        end loop;
    end;
$$;

SELECT insert_car(12000);
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
CREATE OR REPLACE FUNCTION insert_renting(amount_full int, amount_null int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_car_id int := 0;
        new_customer_id int := 0;
        current_amount int := 0;
        new_date timestamp := '2014-01-10 20:00:00';
        new_period int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO new_car_id floor(random()*(12000-1+1))+1;
            SELECT INTO new_customer_id floor(random()*(10000-1+1))+1;
            SELECT INTO new_period floor(random()*(300-1+1))+1;
            SELECT INTO new_date timestamp '2014-01-10 20:00:00' + random() * (timestamp '2021-01-20 20:00:00' -
                                                                 timestamp '2014-01-01 10:00:00');
            INSERT INTO renting(renting_id, date_renting, period_renting, car_id, customer_id)
                VALUES (DEFAULT, new_date, new_period, new_car_id, new_customer_id);
            current_amount = current_amount + 1;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            SELECT INTO new_car_id floor(random()*(12000-1+1))+1;
            SELECT INTO new_period floor(random()*(300-1+1))+1;
            SELECT INTO new_date timestamp '2014-01-10 20:00:00' + random() * (timestamp '2021-01-20 20:00:00' -
                                                                 timestamp '2014-01-01 10:00:00');
            INSERT INTO renting(renting_id, date_renting, period_renting, car_id, customer_id)
                VALUES (DEFAULT, new_date, new_period, new_car_id, NULL);
            current_amount = current_amount + 1;
        end loop;
    end;
$$;

SELECT insert_renting(7000,7000);
SELECT insert_renting(7000,7000);
SELECT * FROM renting;

-- customer
CREATE SEQUENCE seq_customer_name AS bigint INCREMENT 1 MAXVALUE 10000 CYCLE;
CREATE SEQUENCE seq_customer_last_name AS bigint INCREMENT 1 MAXVALUE 10000 CYCLE;
CREATE OR REPLACE FUNCTION insert_customer(amount_full int, amount_null int) RETURNS void
LANGUAGE plpgsql
AS
$$
    DECLARE
        new_address_id int := 0;
        current_amount int := 0;
    BEGIN
        loop
            exit when current_amount = amount_full;
            SELECT INTO new_address_id floor(random()*(1500-1+1))+1;
            INSERT INTO customer(customer_id, first_name, last_name, address_id)
                VALUES (DEFAULT, 'first name '||nextval('seq_customer_name'),
                        'last name '||nextval('seq_customer_last_name'), new_address_id);
            current_amount = current_amount + 1;
        end loop;
        current_amount :=0;
        loop
            exit when current_amount = amount_null;
            INSERT INTO customer(customer_id, first_name, last_name, address_id)
                VALUES (DEFAULT, 'first name '||nextval('seq_customer_name'),
                        'last name '||nextval('seq_customer_last_name'), NULL);
            current_amount = current_amount + 1;
        end loop;
    ALTER SEQUENCE IF EXISTS seq_customer_name RESTART;
    ALTER SEQUENCE IF EXISTS seq_customer_last_name RESTART;
    end;
$$;
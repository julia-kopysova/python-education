SELECT *
FROM potential_customers;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (15, 'email1-15@gmail.com', 'Tom', 'Smith', 'del', 'New York');
ROLLBACK;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (15, 'email1-15@gmail.com', 'Tom', 'Smith', 'del', 'New York');
COMMIT;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (16, 'email1-16@gmail.com', 'Kell', 'Smith', 'van', 'New York');
SAVEPOINT insert_point;
DELETE FROM potential_customers WHERE potential_customers_id = 17;
ROLLBACK TO SAVEPOINT insert_point;
COMMIT;

BEGIN;
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
    VALUES (17, 'email1-17@gmail.com', 'Mikki', 'Smith', 'van', 'New York');
UPDATE potential_customers SET name = 'Eldar' WHERE name = 'Mikki';
SAVEPOINT update_point;
DELETE FROM potential_customers WHERE name = 'Mikki';
ROLLBACK TO SAVEPOINT update_point;
COMMIT;
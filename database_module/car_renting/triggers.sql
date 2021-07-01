CREATE TABLE updates_address_branch (
   id INT GENERATED ALWAYS AS IDENTITY,
   branch_id INT NOT NULL,
   old_address INT NOT NULL,
   new_address INT NOT NULL,
   date_changes TIMESTAMP(6) NOT NULL
);
DROP TABLE IF EXISTS  updates_address_branch;
DROP FUNCTION IF EXISTS log_update_address_branch();

CREATE OR REPLACE FUNCTION log_update_address_branch()
  RETURNS TRIGGER
  LANGUAGE plpgsql
  AS
$$
BEGIN
	IF NEW.address_id <> OLD.address_id THEN
		 INSERT INTO updates_address_branch(branch_id, old_address, new_address, date_changes)
		 VALUES(OLD.branch_id, OLD.address_id, NEW.address_id, now());
	END IF;
	RETURN NEW;
END;$$;

CREATE TRIGGER product_price_changes
AFTER UPDATE
ON branch
FOR EACH ROW
EXECUTE PROCEDURE log_update_address_branch();

CALL update_branch_address(1,3);
SELECT * FROM updates_address_branch;

CREATE OR REPLACE FUNCTION delete_customer_renting()
  RETURNS trigger
  LANGUAGE plpgsql
  AS
$$
BEGIN
   UPDATE renting SET customer_id = NULL WHERE customer_id = OLD.customer_id;
   RETURN OLD;
END;$$;

CREATE TRIGGER delete_customer
   BEFORE DELETE ON customer
   FOR EACH ROW
   EXECUTE PROCEDURE delete_customer_renting();

BEGIN;
SELECT r.customer_id, r.renting_id
FROM customer c
JOIN renting r on c.customer_id = r.customer_id;

SELECT customer_id
FROM renting
WHERE renting_id = 1;

DELETE FROM customer
WHERE customer_id = 5518;
ROLLBACK;
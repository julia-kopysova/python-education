CREATE TABLE IF NOT EXISTS city(
    city_id serial PRIMARY KEY,
    city_name varchar(20) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS street(
    street_id serial PRIMARY KEY,
    street_name varchar(50) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS house(
    house_id serial PRIMARY KEY,
    house_number int UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS address(
    address_id serial PRIMARY KEY,
    city_id int NOT NULL,
    street_id int,
    house_id int,
    phone_number varchar(13),
    FOREIGN KEY (city_id)
      	REFERENCES city(city_id),
    FOREIGN KEY (street_id)
      	REFERENCES street(street_id),
    FOREIGN KEY (house_id)
      	REFERENCES house(house_id)
);
CREATE TABLE IF NOT EXISTS customer(
   customer_id serial PRIMARY KEY,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255) NOT NULL,
   address_id int,
    FOREIGN KEY (address_id)
      	REFERENCES address(address_id)
);
CREATE TABLE IF NOT EXISTS branch(
    branch_id serial PRIMARY KEY,
    address_id int NOT NULL,
    FOREIGN KEY (address_id)
      	REFERENCES address(address_id)
);
CREATE TABLE IF NOT EXISTS capacity_engine(
    capacity_engine_id serial PRIMARY KEY,
    capacity float NOT NULL
);
CREATE TABLE IF NOT EXISTS transmission(
    transmission_id serial PRIMARY KEY,
    type_name varchar(20) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS cylinder(
    cylinder_id serial PRIMARY KEY,
    quantity int UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS equipment(
    equipment_id serial PRIMARY KEY,
    cylinder_id int NOT NULL ,
    transmission_id int NOT NULL ,
    capacity_engine_id int NOT NULL ,
    FOREIGN KEY (cylinder_id)
      	REFERENCES cylinder(cylinder_id),
    FOREIGN KEY (transmission_id)
      	REFERENCES transmission(transmission_id),
    FOREIGN KEY (capacity_engine_id)
      	REFERENCES capacity_engine(capacity_engine_id)
);

CREATE TABLE IF NOT EXISTS manufacture(
    manufacture_id serial PRIMARY KEY,
    manufacture_name varchar(50) NOT NULL
);
DROP TABLE manufacture CASCADE;
CREATE TABLE IF NOT EXISTS model(
    model_id serial PRIMARY KEY,
    model_name varchar(50) NOT NULL,
    manufacture_id int NOT NULL,
    equipment_id int,
    FOREIGN KEY (manufacture_id)
        REFERENCES manufacture(manufacture_id),
    FOREIGN KEY (equipment_id)
        REFERENCES equipment(equipment_id)
);
CREATE TABLE IF NOT EXISTS car(
    car_id serial PRIMARY KEY,
    car_number int UNIQUE NOT NULL,
    price numeric(5,2) NOT NULL,
    branch_id int NOT NULL,
    model_id int NOT NULL,
    FOREIGN KEY (branch_id)
        REFERENCES branch(branch_id),
    FOREIGN KEY (model_id)
        REFERENCES model(model_id)
);
CREATE TABLE IF NOT EXISTS renting(
    renting_id serial PRIMARY KEY,
    date_renting timestamp NOT NULL,
    period_renting int NOT NULL,
    car_id int NOT NULL,
    customer_id int,
    FOREIGN KEY (car_id)
        REFERENCES car(car_id),
    FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
);
-- CREATE DATABASE contacts_api;
DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  phone_number VARCHAR,
  address VARCHAR
);
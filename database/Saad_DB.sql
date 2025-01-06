CREATE DATABASE smart_contract_db;

USE smart_contract_db;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(100),
    receiver VARCHAR(100),
    amount DECIMAL(10, 2)
);


USE smart_contract_db;
SHOW TABLES;
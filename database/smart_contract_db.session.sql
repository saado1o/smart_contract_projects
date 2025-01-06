CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS buyer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS manufacturers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO relationships (source_id, target_id, relationship_type, source_type, target_type) 
VALUES (%s, %s, %s, %s, %s);

CREATE TABLE IF NOT EXISTS relationships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_id INT NOT NULL,
    target_id INT NOT NULL,
    relationship_type VARCHAR(255) NOT NULL,
    source_type VARCHAR(255) NOT NULL,
    target_type VARCHAR(255) NOT NULL,
    FOREIGN KEY (source_id) REFERENCES suppliers(id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES suppliers(id) ON DELETE CASCADE
);


ALTER USER 'smart_contract_project'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'your_mysql_password';

-- Create the `suppliers` table
CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
) DEFAULT CHARSET=utf8mb4;

-- Create the `buyers` table
CREATE TABLE IF NOT EXISTS buyers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
) DEFAULT CHARSET=utf8mb4;

-- Create the `manufacturers` table
CREATE TABLE IF NOT EXISTS manufacturers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
) DEFAULT CHARSET=utf8mb4;

-- Create the `relationships` table
CREATE TABLE IF NOT EXISTS relationships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_id INT NOT NULL,
    target_id INT NOT NULL,
    relationship_type VARCHAR(255) NOT NULL,
    source_type ENUM('suppliers', 'buyers', 'manufacturers') NOT NULL,
    target_type ENUM('suppliers', 'buyers', 'manufacturers') NOT NULL,
    FOREIGN KEY (source_id) REFERENCES suppliers(id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES suppliers(id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

-- Adjust foreign key references for relationships (optional, depending on requirements)
-- Uncomment and modify if `source_id` or `target_id` should reference other tables.
-- FOREIGN KEY (source_id) REFERENCES buyers(id) ON DELETE CASCADE,
-- FOREIGN KEY (target_id) REFERENCES manufacturers(id) ON DELETE CASCADE;

-- Insert sample data into `relationships`
-- Adjust the `%s` placeholders with actual data in your Python script.
-- Remove this line if it's meant to be handled dynamically in Python.

-- Uncomment the below lines if the user 'smart_contract_project' needs to be configured
-- ALTER USER 'smart_contract_project'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'your_mysql_password';

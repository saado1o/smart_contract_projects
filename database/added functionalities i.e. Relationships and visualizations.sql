CREATE TABLE members (
    id INT PRIMARY KEY AUTO_INCREMENT,
    member_type VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE relationships (
    id INT PRIMARY KEY AUTO_INCREMENT,
    source_member_id INT NOT NULL,
    target_member_id INT NOT NULL,
    relationship_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_member_id) REFERENCES members(id),
    FOREIGN KEY (target_member_id) REFERENCES members(id)
);


INSERT INTO members (member_type, name, location) VALUES ('supplier', 'Supplier A', 'Location A');
INSERT INTO members (member_type, name, location) VALUES ('manufacturer', 'Manufacturer B', 'Location B');
INSERT INTO members (member_type, name, location) VALUES ('buyer', 'Buyer C', 'Location C');


INSERT INTO relationships (source_member_id, target_member_id, relationship_type) VALUES (1, 2, 'supplies');
INSERT INTO relationships (source_member_id, target_member_id, relationship_type) VALUES (2, 3, 'manufactures');
INSERT INTO relationships (source_member_id, target_member_id, relationship_type) VALUES (3, 1, 'buys_from');


SELECT m1.name AS source_name, m1.member_type AS source_type, r.relationship_type, m2.name AS target_name, m2.member_type AS target_type
FROM relationships r
JOIN members m1 ON r.source_member_id = m1.id
JOIN members m2 ON r.target_member_id = m2.id;

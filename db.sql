CREATE DATABASE IF NOT EXISTS client_management;

USE client_management;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,        
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,       
    company VARCHAR(100) NOT NULL             
);
INSERT INTO clients (id,name, email, company)
VALUES 
    (201,'John Doe', 'john@example.com', 'Tech titans'),
    (202,'Jane Smith', 'jane@example.com', 'Tech titans'),
    (203,'Alice Brown', 'alice@example.com', 'Tech titans');

show databases;
CREATE DATABASE IF NOT EXISTS naadbramha_db;
USE naadbramha_db;
show tables;
desc menu;
desc billing ;
desc sales;
desc users;
-- Menu Table
drop table menu;
CREATE TABLE menu (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

select *from menu;

-- Staff Table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Leave') NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
);

-- Sales Table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_method ENUM('Cash', 'UPI', 'Card') NOT NULL
);

-- Inventory Table
CREATE TABLE inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Billing Table
CREATE TABLE billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT,
    item_id INT,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory(item_id) ON DELETE CASCADE
);
INSERT INTO menu (item_name, price) VALUES
('Idli Chutney/Sambar (1 PC)', 10),
('Idli Chutney/Sambar (2 PC)', 20),
('Idli Chutney/Sambar (3 PC)', 30),
('Thatte Ghee Masala Idli (1 PC)', 50),
('Button Ghee Masala Idli (14 PC)', 60),
('Tea', 10),
('Coffee', 15),
('Lemon Tea', 10),
('Mineral Water', 20);
delete from menu where item_id=1;


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from users;

delete  from users where id =1;


CREATE TABLE billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    datetime DATETIME NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL
);
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT,
    item_name VARCHAR(255),
    price DECIMAL(10,2),
    quantity INT,
    total FLOAT,
    FOREIGN KEY (bill_id) REFERENCES billing(bill_id) ON DELETE CASCADE
);
desc menu;
use naadbramha_db;



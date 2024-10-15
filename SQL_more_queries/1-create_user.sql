-- Task 1: Create user_0d_1 with all privileges on the MySQL server
-- This script creates the user 'user_0d_1' with full privileges and sets the password.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

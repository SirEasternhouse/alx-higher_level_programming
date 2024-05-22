-- Creation of database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Cration of user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting SELECT privilege on database to user
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';

-- Applying changes
FLUSH PRIVILEGES;

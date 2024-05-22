-- Creation of database if it does not exist
-- Cration of user if it does not exist
-- Granting SELECT privilege on database to user
-- Applying changes
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;

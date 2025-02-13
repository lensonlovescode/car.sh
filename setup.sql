-- Prepares a database and respective users and tables for the project

CREATE DATABASE IF NOT EXISTS carsh;

CREATE USER 'carsh_dev'@'localhost' IDENTIFIED BY 'carsh@1hDbTVi4';

GRANT ALL PRIVILEGES ON carsh_dev.* TO 'carsh_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'carsh_dev'@'localhost';

FLUSH PRIVILEGES;

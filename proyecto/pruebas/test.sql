-- Active: 1747619745969@@127.0.0.1@3306@publicacion_articulos

SHOW TABLES;
DESCRIBE role;
DESCRIBE usr;
DESCRIBE articulo;
SELECT * FROM user WHERE email='author@example.com';

SELECT * FROM role;

ALTER TABLE articulo ADD COLUMN imagen VARCHAR(256);
DROP DATABASE IF EXISTS publicacion_articulos;

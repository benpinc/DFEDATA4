CREATE DATABASE Exercises
USE Exercises
CREATE TABLE table1
(id int not null primary key autoincrement,
firstname varchar(255) not null,
surname varchar(255) not null,
birthdate date
)
SELECT * from table1

SELECT * from table1 
WHERE id = 1

SELECT firstname, surname
FROM table1
ORDER BY surname, firstname
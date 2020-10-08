CREATE DATABASE mahi;
use mahi;

CREATE TABLE students (
    id int,
    Name varchar(25),
    email varchar(25),
    city varchar(25)
    
);

ALTER TABLE students
ADD email varchar(20),city varchar(20);

select * from students;



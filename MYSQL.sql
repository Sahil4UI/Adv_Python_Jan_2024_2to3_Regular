-- how to delete a database ?  
drop database emp;

-- how to create database?
create database bmpl; 

-- how to use database?
USe bmpl;

-- SQL is not a case sensitive language alter
--  YYYY-MM-DD. - date format 
create table employee (id int primary key, name text , dept text,doj date,salary int); 
-- primary key - column name which will never store any duplicate value 

-- how to insert data in sql
insert into employee values 
(101,"Sahil","IT","2023-07-05",90000),
(102,"Lokesh","HR","2022-12-01",75000),
(103,"Ravi","ADMIN","2013-03-01",50000),
(104,"Shipra","ACC","2026-07-12",19000),
(105,"Pooja","SEC","2023-10-15",5000);

-- how to view table 
select * from employee;

insert into employee values 
(106,"Mohit","IT","2024-04-25",24000),
(107,"Mohan","IT","2024-04-25",24000);
-- select statement
select * from employee where id = 101;
select * from employee where id between 101 and 103;
select * from employee where id in (101,104,105);
select * from employee where id >=102 ;
-- % - anything
select * from employee where name like "S%";
select * from employee where name like "%a";
select * from employee where name like "%i%";
-- when we are position specific  , then use _
select * from employee where name like "__i%";

-- select * from employee where doj=current_date();
 
select * from employee where year(doj)=2024;

select * from employee order by salary desc limit 2;

update employee set salary = salary+salary*0.2 ;

select * from employee;

select count(*) from employee;

delete from employee where id=101;
-- how to add/remove/modify columns in SQL 
alter table employee add project int; 

alter table employee modify project text; 
-- how to find type
describe employee; 

alter table employee drop column project; 

-- how many tables are there in our database;
show tables;
show databases;

drop table employee;
drop database bmpl;


-- Task 1
-- Create a table
-- Create a table of your choice inside the sample SQLite database, 
-- rename it, and add a new column. Insert a couple rows inside your table. 
-- Also, perform UPDATE and DELETE statements on inserted rows.

-- As a solution to this task, create a file named: task1.sql, 
-- with all the SQL statements you have used to accomplish this task

create table _my_first_table (
	id int,
	name varchar(255),
	city varchar(255),
	country varchar(255)
);

alter table "_my_first_table" rename to _my_first_table_with_updated_name;
alter table _my_first_table ADD column age int;

insert into _my_first_table values(1, 'Test name', 'Kyiv', 'Ukraine', 25);
insert into _my_first_table values(2, 'Test name 2', 'Lviv', 'Ukraine', 28);
insert into _my_first_table values(3, 'Test name 3', 'Odesa', 'Ukraine', 31);

update _my_first_table
set name = 'New name' 
where id = 1;

delete from _my_first_table
where id = 3;

select * from _my_first_table;
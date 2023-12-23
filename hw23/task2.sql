-- Task 2
-- Select queries
-- Use the sample PostreSQL database hr.db
-- As a solution to HW, create a file named: task2.sql with all SQL queries:

-- write a query to display the names (first_name, last_name) using
--  alias name "First Name", "Last Name" from the table of employees;
-- write a query to get the unique department ID from the employee table
-- write a query to get all employee details from the employee table ordered
--  by first name, descending
-- write a query to get the names (first_name, last_name), salary, PF of all 
-- the employees (PF is calculated as 12% of salary)
-- write a query to get the maximum and minimum salary from the employees table
-- write a query to get a monthly salary (round 2 decimal places) of each and every employee

select first_name as "First Name", last_name as "Last Name"  from "_employees";

select distinct department_id from "_employees";

select * from "_employees"
order by first_name desc;

select first_name, last_name, salary, salary * 0.12 as pf from "_employees";
select sum(salary * 0.12) from "_employees";

select min(salary) from "_employees" ;
select max(salary) from "_employees";

select first_name as "First Name", 
last_name as "Last Name",
salary as "Salary", 
round(cast(salary as numeric) / 12, 2) as "Monthly Salary" from "_employees";
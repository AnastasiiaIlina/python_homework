-- Joins
-- Use the sample SQLite database hr.db (same database you used in 
-- the previous lesson for homework tasks)
-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- 1. write a query in SQL to display the first name, last name, department number, 
-- and department name for each employee

select _employees.first_name, _employees.last_name, _department.department_id , _department.department_name 
from _employees
inner join _department on _employees.department_id = _department.department_id  

-- 2. write a query in SQL to display the first and last name, department, city, 
-- and state province for each employee

select _employees.first_name, _employees.last_name, _department.department_name, _locations.city, _locations.state_province 
from _employees
inner join _department on _employees.department_id = _department.department_id 
inner join _locations on _department.location_id = _locations.location_id 

-- 3. write a query in SQL to display the first name, last name, department number, 
-- and department name, for all employees for departments 80 or 40

select _employees.first_name, _employees.last_name, _departments.department_id, _departments.depart_name 
from "_employees" 
inner join "_departments" on _employees.department_id = _departments.department_id
where _departments.department_id in (40, 80)

-- 4. write a query in SQL to display all departments including those where does not have any employee

select _employees.first_name, _employees.last_name, _departments.department_id, _departments.depart_name 
from "_employees" 
right join "_departments" on _employees.department_id = _departments.department_id

-- 5. write a query in SQL to display the first name of all employees including the first name 
-- of their manager

select  employees.first_name, managers.first_name
from "_employees" employees
left join "_employees" managers on managers.employee_id = employees.manager_id

-- 6. write a query in SQL to display the job title, full name (first and last name) of the employee, 
-- and the difference between the maximum salary for the job and the salary of the employee

select  
	_jobs.job_title, _jobs.max_salary, _employees.salary,
	concat_ws(' ', _employees.first_name, _employees.last_name) as full_name,
	(_jobs.max_salary - _employees.salary) as salary_diff
from "_jobs"
inner join "_employees" on _employees.job_id = _jobs.job_id 

-- 7. write a query in SQL to display the job title and the average salary of employees

select  _jobs.job_title, AVG(_employees.salary) as avg_salary
from "_jobs"
inner join "_employees" on _employees.job_id = _jobs.job_id 
group by _jobs.job_title

-- 8. write a query in SQL to display the full name (first and last name), and salary of those employees 
-- who work in any department located in London

select  
	concat_ws(' ', _employees.first_name, _employees.last_name) as full_name, 
	_employees.salary, 
	_departments.depart_name,
	_locations.city
from "_employees"
inner join "_departments" on _departments.department_id = _employees.department_id
inner join "_locations" on _locations.location_id = _departments.location_id 
where  _locations.city = 'London'

-- 9. write a query in SQL to display the department name and the number of employees in each department

select  
	_departments.depart_name,
	count(_employees.employee_id) as employees_amount
from "_employees"
inner join "_departments" on _departments.department_id = _employees.department_id
group by _departments.depart_name
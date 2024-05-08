/*Consider the 'Employees' table. Write an SQL query to find the names of employees who 
joined the company after '2020-01-01' and are currently working in the 'Finance'
 department. The result should include only the 'emp_name' column.*/





SELECT 
Department.department,
Employees.emp_name,
Employees.hire_date
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id
where Employees.hire_date > '2020-01-01' and Department.department = 'Finance'
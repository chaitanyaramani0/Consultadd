/*Write an SQL query to retrieve the names of all employees along with the names of 
their corresponding departments. Include only employees who belong to the 'Sales' 
department. The result should include two columns: 'emp_name' and 'dept_name'.*/



SELECT Employees.emp_name, Department.department
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id 
where Department.department = 'Sales';

SELECT Employees.emp_name, Department.department
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id 
where Department.department = 'Sales';

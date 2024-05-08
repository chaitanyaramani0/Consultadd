SELECT 
Department.department,
Employees.emp_name,
Employees.hire_date
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id
where Employees.hire_date > '2020-01-01' and Department.department = 'Finance'
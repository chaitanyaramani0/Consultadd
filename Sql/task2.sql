SELECT 
Department.department,
timestampdiff(YEAR,Employees.hire_date,current_date()) as Totaltenure
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id;
/*Given the 'Employees' table, write an SQL query to calculate the average tenure (in years)
 of employees in each department. The tenure is calculated as the difference between the 
 current date and the 'hire_date', rounded to the nearest year. The result should include
  two columns: 'dept_name' and 'AverageTenure'.*/

SELECT 
Department.department,
timestampdiff(YEAR,Employees.hire_date,current_date()) as Totaltenure
from Employees
Inner Join Department
on Employees.department_id = Department.dept_id;
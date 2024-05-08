/*Consider the 'Employees' table. Write an SQL query to find the names of employees 
who have been with the company for more than 3 years and have a salary greater than
 $50,000. The result should include only the 'emp_name' column.*/

select emp_name from Employees 
where YEAR(hire_date) > 2021 and salary > 50000
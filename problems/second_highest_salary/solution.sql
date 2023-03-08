# Write your MySQL query statement below

select max(salary) as SecondHighestSalary

from Employee

where salary < (select salary from Employee ORDER BY salary DESC LIMIT 1)
# Write your MySQL query statement below

SELECT employee_id, IF(employee_id % 2 != 0 AND NOT name LIKE "M%", salary, 0) AS bonus FROM Employees
ORDER BY employee_id
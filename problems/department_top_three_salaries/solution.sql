# Write your MySQL query statement below

WITH c AS (
    SELECT id, departmentId, salary, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary desc) AS N
    FROM Employee
), 
 m AS (
    SELECT departmentId, MIN(salary) as salary FROM c WHERE c.N <= 3 GROUP BY departmentId
)

SELECT d.name as Department, e.name as Employee, e.salary as Salary FROM 
Employee e INNER JOIN Department d ON (d.id = e.departmentId)
INNER JOIN m ON (e.departmentId = m.departmentId AND e.salary >= m.salary)
 
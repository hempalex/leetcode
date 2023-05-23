# Write your MySQL query statement below

SELECT m.name FROM Employee m INNER JOIN Employee e ON (e.managerId = m.id)
GROUP BY m.id HAVING COUNT(e.id) >= 5
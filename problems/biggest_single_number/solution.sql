# Write your MySQL query statement below
WITH Single AS (
    SELECT MAX(num) AS num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1
)

SELECT MAX(num) as num FROM Single
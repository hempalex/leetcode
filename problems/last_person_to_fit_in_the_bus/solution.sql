# Write your MySQL query statement below

WITH weight AS (
    SELECT *, SUM(weight) OVER(order by turn) AS cumulative_weight FROM queue
)

SELECT person_name FROM weight 
WHERE cumulative_weight <= 1000
ORDER BY cumulative_weight DESC
LIMIT 1
WITH days AS (
    SELECT visited_on, sum(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT b.visited_on, SUM(a.amount) AS amount, ROUND(avg(a.amount), 2) AS average_amount
FROM days a 
INNER JOIN days b ON (b.visited_on BETWEEN a.visited_on AND a.visited_on + INTERVAL 6 DAY)
GROUP BY b.visited_on
HAVING COUNT(a.visited_on) = 7
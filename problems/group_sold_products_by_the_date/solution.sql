# Write your MySQL query statement below

SELECT sell_date, count(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product SEPARATOR ',') AS products 
FROM Activities
GROUP BY sell_date
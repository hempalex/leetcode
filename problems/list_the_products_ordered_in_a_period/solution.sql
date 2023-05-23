# Write your MySQL query statement below

SELECT p.product_name, SUM(o.unit) as unit
FROM 
Orders o INNER JOIN Products p ON (o.product_id = p.product_id AND YEAR(o.order_date) = 2020 AND MONTH(o.order_date) = 2)  

GROUP BY p.product_id
HAVING unit >= 100
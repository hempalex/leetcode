# Write your MySQL query statement below

WITH First AS (
    SELECT customer_id, MIN(order_date) AS order_date, MIN(customer_pref_delivery_date) AS customer_pref_delivery_date  FROM Delivery GROUP BY customer_id 
)

SELECT ROUND(100 * SUM(IF(order_date = customer_pref_delivery_date, 1, 0))/COUNT(customer_id), 2) AS immediate_percentage FROM First

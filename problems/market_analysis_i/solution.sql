# Write your MySQL query statement below

WITH Orders2019 AS (
  SELECT buyer_id AS user_id, COUNT(order_id) as orders
  FROM Orders 
  WHERE YEAR(order_date) = 2019
  GROUP BY buyer_id
)

SELECT u.user_id AS buyer_id, u.join_date, IFNULL(o.orders, 0) AS orders_in_2019 
FROM users u LEFT JOIN Orders2019 o ON (u.user_id = o.user_id)
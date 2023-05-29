# Write your MySQL query statement below

WITH last_change AS (
    SELECT product_id, MAX(change_date) as change_date 
    FROM Products 
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
),

products_all AS (
    SELECT DISTINCT product_id FROM Products
)

SELECT a.product_id, IFNULL(p.new_price, 10) as price FROM 
    products_all a 
    LEFT JOIN last_change l ON (a.product_id = l.product_id)
    LEFT JOIN Products p ON (l.product_id = p.product_id and l.change_date = p.change_date)
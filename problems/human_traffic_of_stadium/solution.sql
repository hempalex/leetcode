# Write your MySQL query statement below

WITH t AS (
    SELECT *, id - (row_number() OVER (ORDER BY id)) AS diff 
    FROM Stadium 
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM t
WHERE diff IN (
    SELECT diff from t GROUP BY diff HAVING count(diff) >=3
)
ORDER BY id
# Write your MySQL query statement below

WITH UsersTotal AS (
    SELECT COUNT(*) AS total FROM Users
)

SELECT r.contest_id, ROUND(100 * COUNT(r.user_id)/t.total, 2) AS percentage 
FROM
Register r, UsersTotal t

GROUP BY contest_id
ORDER BY percentage DESC, contest_id


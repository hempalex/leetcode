# Write your MySQL query statement below

WITH all_requests AS (
    SELECT requester_id AS id FROM RequestAccepted
UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) 
SELECT id, count(id) as num
FROM all_requests
GROUP BY id
ORDER BY num DESC
LIMIT 1

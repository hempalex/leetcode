# Write your MySQL query statement below

WITH 
First AS (
    SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id
),
Second AS (
    SELECT a.player_id, MIN(a.event_date) as event_date FROM Activity a INNER JOIN First f ON (f.player_id = a.player_id) WHERE DATEDIFF(a.event_date, f.event_date) = 1
    GROUP BY a.player_id
)

SELECT ROUND(SUM(IF(s.player_id IS NULL, 0, 1))/COUNT(f.player_id), 2) AS fraction FROM First f LEFT JOIN Second s ON (s.player_id = f.player_id) 


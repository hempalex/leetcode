
SELECT t.request_at AS Day, ROUND(SUM(IF(t.status != 'completed', 1, 0))/COUNT(t.id), 2) AS `Cancellation Rate` FROM Trips t INNER JOIN Users c ON (c.users_id = t.client_id and c.banned != 'Yes') INNER JOIN Users d ON (d.users_id = t.driver_id and d.banned != 'Yes') 
WHERE t.request_at BETWEEN '2013-10-01' and '2013-10-03'
GROUP BY request_at
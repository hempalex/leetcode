# Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance i
WHERE 1
AND i.tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(pid) > 1
)
AND (i.lat, i.lon) NOT IN (
    SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(pid) > 1 
)

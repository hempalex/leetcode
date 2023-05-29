# Write your MySQL query statement below

SELECT DISTINCT n1.num AS ConsecutiveNums FROM 
    Logs n1 
    INNER JOIN Logs n2 ON (n1.id = n2.id - 1 AND n1.num = n2.num )
    INNER JOIN Logs n3 ON (n2.id = n3.id - 1 AND n2.num = n3.num )

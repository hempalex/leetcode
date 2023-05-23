# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE p1 FROM Person p1 LEFT JOIN Person p2 ON (p1.email = p2.email AND p1.id > p2.id)
WHERE p2.id IS NOT NULL


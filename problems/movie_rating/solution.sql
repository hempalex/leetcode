# Write your MySQL query statement below
WITH 
UserRatings AS (
    SELECT u.name AS results FROM MovieRating r INNER JOIN Users u ON (r.user_id = u.user_id)
    GROUP BY r.user_id
    ORDER BY COUNT(r.movie_id) DESC, u.name
    LIMIT 1
),
MovieRatings AS (
    SELECT m.title AS results FROM MovieRating r INNER JOIN Movies m ON (r.movie_id = m.movie_id)
    WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
    GROUP BY r.movie_id
    ORDER BY AVG(r.rating) DESC, m.title
    LIMIT 1
)

SELECT * FROM UserRatings
UNION ALL
SELECT * FROM MovieRatings


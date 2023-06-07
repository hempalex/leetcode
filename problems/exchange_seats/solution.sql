WITH Seat_max AS (
  SELECT MAX(id) AS id FROM Seat
)

SELECT IF(s.id % 2 = 1, 
            IF(s.id != Seat_max.id, s.id + 1, s.id),
            s.id - 1
      ) AS id, 
      student 
FROM Seat s, Seat_max
ORDER BY id

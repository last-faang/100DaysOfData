SELECT
    s1.id,
    COALESCE(CASE WHEN s1.id % 2 = 0 THEN s3.student ELSE s2.student END, s1.student) AS student
FROM Seat AS s1
LEFT JOIN Seat AS s2
    ON s1.id = s2.id - 1
LEFT JOIN Seat AS s3
    ON s1.id = s3.id + 1;

SELECT
    *,
    CASE 
        WHEN (x + y < z OR x + z < y OR y + x < z) THEN 'No'
    ELSE 'Yes' END AS triangle
FROM Triangle;

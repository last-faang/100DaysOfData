SELECT person_name
FROM (
    SELECT
        *,
        CASE WHEN SUM(weight) OVER (ORDER BY turn) <= 1000 THEN 1 END AS is_in
    FROM Queue
) AS temp
WHERE is_in = 1
ORDER BY turn DESC 
LIMIT 1;

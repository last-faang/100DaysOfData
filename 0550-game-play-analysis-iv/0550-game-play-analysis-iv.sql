SELECT
    ROUND(COUNT(DISTINCT player_id)::numeric / COUNT(*), 2) AS fraction
FROM (
    SELECT
        a2.player_id,
        ROW_NUMBER() OVER (PARTITION BY a1.player_id ORDER BY a1.event_date) AS rn
    FROM Activity AS a1
    LEFT JOIN Activity AS a2
        ON a1.player_id = a2.player_id
    AND a1.event_date + INTERVAL '1 day' = a2.event_date
)
WHERE rn = 1;

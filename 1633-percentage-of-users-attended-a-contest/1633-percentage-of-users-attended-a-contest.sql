SELECT
    contest_id,
    ROUND(100.0 * COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY
    percentage DESC,
    contest_id;

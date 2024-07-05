SELECT
    Signups.user_id,
    ROUND(SUM(CASE 
                  WHEN Confirmations.user_id IS NULL OR Confirmations.action = 'timeout' THEN 0
              ELSE 1
              END)::numeric / COUNT(Signups.user_id), 2) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
    ON Signups.user_id = Confirmations.user_id
GROUP BY Signups.user_id;

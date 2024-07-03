SELECT
    Prices.product_id,
    COALESCE(ROUND(SUM(UnitsSold.units * Prices.price)::numeric / SUM(UnitsSold.units), 2), 0) AS average_price
FROM Prices
LEFT JOIN UnitsSold
    ON Prices.product_id = UnitsSold.product_id
   AND Prices.start_date <= UnitsSold.purchase_date
   AND Prices.end_date >= UnitsSold.purchase_date
GROUP BY Prices.product_id;

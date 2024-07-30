SELECT
    product_id,
    CASE
      WHEN store1 IS NOT NULL THEN store1
    'store1' AS store,
    END AS price
FROM Products
UNION ALL
SELECT
    product_id,
    CASE
      WHEN store2 IS NOT NULL THEN store2
    'store2' AS store,
    END AS price
FROM Products;
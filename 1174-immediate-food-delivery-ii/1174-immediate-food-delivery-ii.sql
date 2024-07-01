WITH first_order_date_list AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT
    ROUND((SUM(CASE WHEN first_order_date_list.first_order_date = Delivery.customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*)), 2) AS immediate_percentage
FROM first_order_date_list
INNER JOIN Delivery 
    ON first_order_date_list.first_order_date = Delivery.order_date
WHERE first_order_date_list.customer_id = Delivery.customer_id;

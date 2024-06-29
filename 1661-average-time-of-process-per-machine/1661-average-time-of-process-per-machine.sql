WITH processing_time_list AS (
  SELECT
      machine_id,
      process_id,
      MAX(timestamp) - MIN(timestamp) AS processing_time
  FROM Activity
  GROUP BY machine_id, process_id
)

SELECT
    machine_id,
    AVG(processing_time) AS processing_time
FROM processing_time_list
GROUP BY machine_id;

SELECT DISTINCT Employee.salary AS SecondHighestSalary
FROM (
  SELECT 2 AS rank
) AS dummy_rank
LEFT JOIN (
  SELECT
      id,
      salary,
      DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
  FROM Employee
) AS Employee
    ON dummy_rank.rank = Employee.rank;

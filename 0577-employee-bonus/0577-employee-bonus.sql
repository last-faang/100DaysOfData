SELECT
    Employee.name,
    Bonus.bonus
FROM Employee
LEFT JOIN Bonus
    ON Employee.empId = Bonus.empId
WHERE COALESCE(Bonus.bonus, 0) < 1000;

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
   
    SELECT 
        IFNULL(
            (SELECT
            DISTINCT salary
            FROM
                Employee
            ORDER BY
                salary DESC
            LIMIT 1
            OFFSET N),
            NULL)  
    as getNthHighestSalary
    
  );
END
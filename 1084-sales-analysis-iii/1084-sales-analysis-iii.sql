SELECT ft.product_id,p.product_name from (
    SELECT
    product_id,sale_date
FROM
    SALES
GROUP BY
    product_id
HAVING
    MIN(sale_date) >='2019-01-01' and 
    MAX(sale_date) <= '2019-03-31' 
) 

as ft JOIN  Product as  p

WHERE
    ft.product_id=p.product_id




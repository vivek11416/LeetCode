SELECT
    score,dense_rank()
OVER( order by score desc)
AS 'rank'
FROM 
(
    SELECT 
    score
FROM
    scores
ORDER BY
    score desc
) as temp



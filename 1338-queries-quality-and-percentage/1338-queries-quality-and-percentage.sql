# Write your MySQL query statement below
select query_name, 
ROUND(AVG(rating/position),2) quality, 
ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100,2) poor_query_percentage
from Queries Group By query_name;
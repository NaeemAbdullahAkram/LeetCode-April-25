# Write your MySQL query statement below
with cte as (select *,
rank() over (partition by customer_id order by order_date asc) as "ranknum"
from delivery)
select round(count(case when order_date = customer_pref_delivery_date then 1 end)*100 / count(*),2) as "immediate_percentage"
from cte
where ranknum = 1;

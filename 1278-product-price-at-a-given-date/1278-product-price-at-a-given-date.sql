# Write your MySQL query statement below
select T1.product_id, coalesce(new_price, 10) price
from (select distinct product_id from Products) T1 left join
(select P1.* from Products P1 left join
(select product_id, max(change_date) change_date 
from Products where change_date <= '2019-08-16' group by product_id) P2
on P1.product_id = P2.product_id and P1.change_date = P2.change_date
where P2.change_date is not null) T2
on T1.product_id = T2.product_id 
select p.product_id ,
ifnull(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price 
# Based on Average selling price = Total Price of Product / Number of products sold
from Prices p
left join Unitssold u
on p.product_id=u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id
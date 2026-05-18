select 
customer_id,
date(transaction_timestamp) as transaction_date,
count(*) as total_transactions,
sum(amount) as total_amount,
case when count(*)>5 then 1
else 0 end as high_velocity_flag


from {{ref('stg_transactions')}}
group by 
customer_id,
transaction_date
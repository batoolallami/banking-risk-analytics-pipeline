select 
t.transaction_id,
t.customer_id,
c.customer_name,
c.email,
c.country_code as customer_country,
c.kyc_status,

t.merchant_id,
m.merchant_name,
m.merchant_category,
m.country_code as merchant_country,

t.transaction_timestamp,
t.amount,
t.currency,
t.status,
t.payment_method,

r.risk_rating,
r.sanctioned_flag

from {{ ref('stg_transactions') }} t
left join {{ ref('stg_customers')}} c
on t.customer_id=c.customer_id

left join {{ref('stg_merchants')}} m
on t.merchant_id=m.merchant_id

left join {{ ref('stg_country_risk')}} r
on c.country_code=r.country_code
select
customer_id,
customer_name,
email,
country_code,
date_of_birth,
signup_date,
kyc_status
from {{ source('banking_raw','customers_raw')}}
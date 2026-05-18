select
merchant_id,
merchant_name,
merchant_category,
country_code
from {{ source('banking_raw','merchants_raw')}}
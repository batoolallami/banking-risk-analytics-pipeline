select
transaction_id,
customer_id,
merchant_id,
transaction_timestamp,
amount,
currency,
status,
payment_method

from {{source('banking_raw','transactions_raw')}}
select
country_code,
risk_rating,
sanctioned_flag
from {{ source('banking_raw','country_risk_raw')}}
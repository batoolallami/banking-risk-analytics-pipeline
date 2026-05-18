{{config(
    materialized ='incremental',
    unique_key='transaction_id'
) }}

select 
*,
case 
when amount>10000 then 1
else 0
end as high_amount_flag,

case
when sanctioned_flag= true then 1
else 0
end as sanctioned_country_flag,

case
when lower(kyc_status)!='verified' then 1
else 0
end as incomplete_kyc_flag,

case
when lower(risk_rating)='high' then 1
else 0
end as high_risk_country_flag


from {{ ref ('int_enriched_transaction')}}

{% if is_incremental() %}
where transaction_timestamp > (
    select max(transaction_timestamp) from {{ this }}
)
{% endif %}
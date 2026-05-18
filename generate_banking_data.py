import random
from datetime import date,timedelta
import pandas as pd
from faker import Faker

fake=Faker()
countries = ["GB","US",'DE','ES','AE','NG','IN','BR','CN']
KYC_STATUSES=['verified','pending','rejected']
TRANSACTION_STATUSES =["approved",'declined','pending']
PAYMENT_METHODS = ['card','bank_transfer','mobile_wallet']
MERCHAND_CATEGORIES=['retail','travel','gambling','crypto','food','electronics']

def generate_merchants(num_merchants=50):
    merchants=[]
    for merchant_id in range(1,num_merchants+1):
        merchants.append({
            'merchant_id':merchant_id,
            'merchant_name':fake.company(),
            'merchant_category':random.choice(MERCHAND_CATEGORIES),
            'country_code':random.choice(countries),
        })
    return pd.DataFrame(merchants)

def generate_country_risk():
    country_risk=[]
    for country_code in countries:
        risk_rating=random.choice(['low','medium','high'])
        country_risk.append({
            'country_code':country_code,
            'risk_rating':risk_rating,
            'sanctioned_flag':risk_rating=='high'
        })
    return pd.DataFrame(country_risk)


#def generate_transactions(num_transaction=1000,num_customers=100):
 #   transactions = []
 #   for transaction_id in range(1,num_transaction+1):
 #       transaction_time=fake.date_time_between(start_date='-30d',end_date='now')
 #       transactions.append({
 #           'transaction_id':transaction_id,
 #           'customer_id':random.randint(1,num_customers),
 #           'merchant_id':random.randint(1,50),
 #           'transaction_timestamp':transaction_time,
 #           'amount':round(random.uniform(5,20000),2),
 #           'currency':'USD',
 #           'status':random.choice(TRANSACTION_STATUSES),
 #           'payment_method':random.choice(PAYMENT_METHODS)
 #       })
 #   return pd.DataFrame(transactions)



#def generate_customers(num_customers=100):
#    customers=[]
 #   for customer_id in range(1,num_customers+1):
  #      signup_date=fake.date_between(start_date="-3y",end_date="today")
  #      customers.append({
   #         'customer_id':customer_id,
 #           'customer_name':fake.name,
 #           'email':fake.email(),
 #           'country_code':random.choice(countries),
 #           'date_of_birth':fake.date_of_birth(minimum_age=18,maximum_age=80),
  #          'signup_date':signup_date,
   #         'kyc_status':random.choice(KYC_STATUSES),
  #      })
  #  return pd.DataFrame(customers)

def main():
   # customer_df=generate_customers(100)
   # customer_df.to_csv('customers.csv',index=False)
   #transaction_df=generate_transactions(1000,100)
   #transaction_df.to_csv('transactions.csv',index=False)
   merchant_df=generate_merchants(50)
   merchant_df.to_csv('merchants.csv',index=False)
   country_risk_df=generate_country_risk()
   country_risk_df.to_csv('country_risk.csv',index=False)
   print("created customers.csv")

if __name__=="__main__":
    main()

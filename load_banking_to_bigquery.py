import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID=os.getenv('PROJECT_ID')
BUCKET_NAME=os.getenv('BUCKET_NAME')

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
DATASET_ID="banking_raw"
FILES={
    'customers.csv':'customers_raw',
    'transactions.csv':'transactions_raw',
    'merchants.csv':'merchants_raw',
    'country_risk.csv':'country_risk_raw'
}

def load_table(file_name,table_name):
    client=bigquery.Client(project=PROJECT_ID)
    uri=f"gs://{BUCKET_NAME}/raw/banking/{file_name}"
    table_id=f"{PROJECT_ID}.{DATASET_ID}.{table_name}"
    job_config=bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition='WRITE_TRUNCATE',
    )
    load_job=client.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config, )
    load_job.result()
    print(f"Loaded {table_name}")

def main():
    for file_name,table_name in FILES.items():
        load_table(file_name,table_name)

if __name__=="__main__":
    main()    



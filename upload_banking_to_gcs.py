import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID=os.getenv('PROJECT_ID')
BUCKET_NAME=os.getenv('BUCKET_NAME')

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
FILES=[
    'customers.csv',
    'merchants.csv',
    'transactions.csv',
    'country_risk.csv'
]

def upload_file_to_gcs (bucket,local_file,gcs_path):
    blob=bucket.blob(gcs_path)
    blob.upload_from_filename(local_file)
    print(f"uploaded {local_file} to gs://{BUCKET_NAME}/{gcs_path}")

def main():
    storage_client=storage.Client(project=PROJECT_ID)
    bucket=storage_client.bucket(BUCKET_NAME)

    for file in FILES:
        gcs_path=f"raw/banking/{file}"
        upload_file_to_gcs(bucket,file,gcs_path)

if __name__=="__main__":
    main()


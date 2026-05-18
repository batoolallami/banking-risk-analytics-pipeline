# banking-risk-analytics-pipeline
Build an end-to-end banking data pipeline that ingests synthetic banking data, stores raw files in GCS, loads raw tables into BigQuery, and uses dbt to create analytics-ready fraud.
---

# Project Overview
This project demonstrates how raw banking transaction data can be transformed into analytics-ready fraud detection models using a layered data warehouse architecture.

The pipeline includes:
- Raw transaction ingestion
- Bigquery warehouse loading
- dbt transformations
- Fraud analytics models
- Data quality testing
- Incremental processing
- lineage documentation

---

# Architecture

Raw CSV Data
-> Google Cloud Storage
-> BigQuery Raw Layer
-> dbt Staging Models
-> Increnmetal Enrichment Models
-> Fraud Mart Models

---

# Technologies Used

- Python
- Pandas
- Google Cloud Storage (GCS)
- BigQuery
- dbt
- SQL
- GitHub

---

# Data Models

## Raw Layer
- customers_raw
- transactions_raw
- merchants_raw
- country_risk_raw

## Staging Layer
- stg_customers
- stg_transactions
- stg_merchants
- stg_country_risk

## Intermediate Layer
- int_enriched_transactions

## Mart Layer
- fct_flagged_transactions
- fct_transaction_velocity
---

# Fraud Detection Logic

The project includes fraud detection logic such as:
- High transaction amount detection
- High risk country detection
- Sanctioned country monitoring
- Incomplete KYC detection
- Transaction velocity analysis
- Rolling 3-day behavioral monitoring

---

# dbt Features Implemented

- Source definitions
- Tests
- Lineage documentation
- Incremental models
- Relationships testing
- Accepted values validation

---

# Example dbt Lineage

[dbt lineage](screenshoots/dbt_lineage.png)

---

# Future Improvements

- Airflow orchestration
- Docker containerization
- CI/CD pipelines
- Real-time streaming ingestion
- Machine learning fraud scoring

---

# Author

Batool Allami

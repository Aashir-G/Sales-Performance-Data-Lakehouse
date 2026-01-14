```md
# 📊 Sales Performance Data Lakehouse

An end-to-end analytics pipeline that transforms raw business data into executive-level dashboards using a modern **Data Lakehouse architecture**.

Pipeline:
```

Excel / CSV → Python → Databricks (Delta Lake) → Power BI

```

This project shows how messy operational data is engineered into scalable, analytics-ready tables and consumed by BI tools.

---

## 🏗️ Architecture

```

Raw Excel / CSV
↓
Python (Cleaning + Feature Engineering)
↓
Databricks Lakehouse
├─ Bronze Layer  → Raw ingestion
├─ Silver Layer  → Cleaned & typed data
└─ Gold Layer    → Aggregated KPIs for BI
↓
Power BI Dashboard (Executive Overview)

```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|-------|
| Python (Pandas) | Data cleaning and preprocessing |
| Databricks | Distributed compute + Lakehouse platform |
| PySpark | Transformations & aggregations |
| Delta Lake | Reliable table storage (ACID) |
| Power BI | Data visualization & dashboards |
| Excel | Raw data source |
| GitHub | Version control |

---

## 📁 Project Structure

```

Sales-Performance-Data-Lakehouse/
│
├── data/
│   ├── raw/                 # Generated raw Excel/CSV (git ignored)
│   ├── processed/           # Cleaned CSV output (git ignored)
│   └── sample/              # Small sample dataset for demo
│
├── notebooks/
│   └── lakehouse_pipeline.py   # Bronze → Silver → Gold pipeline
│
├── src/
│   ├── generate_raw_excel.py   # Fake dataset generator
│   ├── clean_excel_to_csv.py   # Cleaning + feature engineering
│   └── config.py
│
├── screenshots/
│   ├── dashboard.png
│   └── databricks_tables.png
│
├── requirements.txt
└── README.md

````

---

## 🔄 Data Layers

### 🥉 Bronze Layer – Raw Ingestion
Stores unmodified data for lineage and recovery.

```python
df_bronze = spark.table("workspace.default.silver_sales")
df_bronze.write.format("delta").saveAsTable("bronze_sales")
````

---

### 🥈 Silver Layer – Curated Data

* Type casting
* Null handling
* Data quality filters
* Standardized schema

```python
df_silver.write.format("delta").saveAsTable("silver_sales_curated")
```

---

### 🥇 Gold Layer – Analytics Tables

| Table             | Description                   |
| ----------------- | ----------------------------- |
| gold_kpis         | Daily KPIs by channel         |
| gold_product_perf | Product-level performance     |
| gold_region_perf  | Region-level revenue & profit |

Only these tables are used by Power BI.

---

## 📊 KPIs Implemented

* Net Revenue
* Profit (estimated with COGS)
* ROAS (Return on Ad Spend)
* AOV (Average Order Value)
* Return Rate
* Orders
* Unique Customers

---

## 📈 Power BI Dashboard

Page: **Executive Overview**

Contains:

* KPI Cards:

  * Net Revenue
  * Profit
  * ROAS
  * Orders

* Visuals:

  * Revenue Trend (Line Chart)
  * Revenue by Channel (Column Chart)
  * Top Products (Bar Chart)
  * Revenue by Region (Bar Chart)

* Slicers:

  * Date range
  * Channel
  * Region

---

## 🖼️ Dashboard Preview

```md
![alt text](image-1.png)
```

---

## 🗃️ Databricks Tables Preview

```md
![alt text](image.png)
```

---

## 🚀 Run Locally (Python)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Generate raw dataset
python -m src.generate_raw_excel

# Clean Excel → CSV
python -m src.clean_excel_to_csv
```

---

## ☁️ Run in Databricks

1. Upload cleaned CSV using:

   * `Create or modify table from file upload`
2. Run the notebook:

```
notebooks/lakehouse_pipeline.py
```

3. Verify tables:

```python
spark.sql("SHOW TABLES").show()
```

You should see:

```
bronze_sales
silver_sales_curated
gold_kpis
gold_product_perf
gold_region_perf
```

---

## 🔌 Power BI Connection

Power BI → Get Data → **Azure Databricks**

Use:

* Server hostname
* HTTP Path
* Personal Access Token

Load:

* gold_kpis
* gold_product_perf
* gold_region_perf

---

## 📌 Notes

* Only Gold tables are exposed to BI tools
* Bronze & Silver layers stay internal to Databricks
* Delta Lake ensures schema consistency and reliability
* Architecture matches real enterprise analytics pipelines

---

## 🔥 Project Outcome

This project implements a full **Lakehouse analytics workflow** with:

* Raw data ingestion
* Structured transformation layers
* Production-style KPI tables
* Live BI dashboard integration


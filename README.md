# 🚀 Sales Performance Data Lakehouse

An end-to-end analytics platform that transforms raw business data into executive-ready dashboards using a modern Lakehouse architecture. Built to mirror how real companies design data pipelines and BI systems.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks\&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-0A2F5A?logo=databricks\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi\&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?logo=microsoftexcel\&logoColor=white)

---

## ✨ Overview

This project simulates a real enterprise analytics workflow:

**Excel / CSV → Python → Databricks (Bronze / Silver / Gold) → Power BI**

It demonstrates how messy operational data is engineered into reliable, analytics-ready tables and visualized in a professional BI dashboard.

---

## ⚡ What Makes It Cool

* 🏗️ **Lakehouse architecture** (Bronze → Silver → Gold)
* 📊 **Executive-level KPIs** (Revenue, Profit, ROAS, Orders, AOV)
* 🔄 **End-to-end pipeline** from Excel to Power BI
* 🧱 **Delta Lake reliability** (schema enforcement + ACID tables)
* 🎯 **Real business use case** (sales, marketing, performance analytics)

---

## 🧠 Architecture

```
Raw Excel / CSV
      ↓
Python (Cleaning & Feature Engineering)
      ↓
Databricks Lakehouse
  ├─ Bronze  → Raw ingestion
  ├─ Silver  → Cleaned & validated data
  └─ Gold    → Business KPIs
      ↓
Power BI Dashboard (Executive Overview)
```

---

## 🛠️ Tech Stack

* Python (Pandas) – Data cleaning
* Databricks – Distributed analytics
* PySpark – Transformations & aggregations
* Delta Lake – Reliable table storage
* Power BI – Dashboarding
* Excel – Raw data source
* GitHub – Version control

---

## 📁 Project Structure

```
Sales-Performance-Data-Lakehouse/
├── data/
│   ├── raw/              # Generated raw data (git ignored)
│   ├── processed/        # Cleaned CSV (git ignored)
│   └── sample/           # Small demo dataset
│
├── notebooks/
│   └── lakehouse_pipeline.py   # Bronze → Silver → Gold pipeline
│
├── src/
│   ├── generate_raw_excel.py   # Dataset generator
│   ├── clean_excel_to_csv.py   # Cleaning + feature engineering
│   └── config.py
│
├── screenshots/
│   ├── dashboard.png
│   └── databricks_tables.png
│
├── requirements.txt
└── README.md
```

---

## 🔄 Data Layers

### 🥉 Bronze

Raw ingested data, preserved for lineage and recovery.

### 🥈 Silver

Curated dataset:

* Correct data types
* Null handling
* Validation & filtering

### 🥇 Gold

Analytics-ready tables used by Power BI:

| Table             | Description           |
| ----------------- | --------------------- |
| gold_kpis         | Daily KPIs by channel |
| gold_product_perf | Product performance   |
| gold_region_perf  | Regional performance  |

Only the **Gold** layer is exposed to BI tools.

---

## 📈 KPIs Implemented

* Net Revenue
* Profit (COGS-adjusted)
* ROAS (Return on Ad Spend)
* Orders
* AOV (Average Order Value)
* Return Rate
* Unique Customers

---

## 📊 Power BI Dashboard

**Page: Executive Overview**

Includes:

* KPI Cards

  * Net Revenue
  * Profit
  * ROAS
  * Orders

* Visuals

  * Revenue Trend (Line)
  * Revenue by Channel (Column)
  * Top Products (Bar)
  * Revenue by Region (Bar)

* Filters

  * Date range
  * Channel
  * Region

---

## 🖼️ Dashboard Preview


![Dashboard Preview](image-1.png)

---

## 🗃️ Databricks Tables Preview


![Databricks Tables](image.png)

---

## 🚀 Run Locally (Python Side)

1. Create virtual environment
2. Install dependencies
3. Generate raw dataset
4. Clean Excel → CSV

This produces the dataset that feeds Databricks.

---

## ☁️ Run in Databricks

1. Upload cleaned CSV using **Create or modify table**
2. Run `lakehouse_pipeline.py`
3. Verify tables:

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

Connect using:

* Server hostname
* HTTP Path
* Personal Access Token

Load:

* gold_kpis
* gold_product_perf
* gold_region_perf

---

## 📌 Notes

* Only Gold tables are exposed to BI
* Bronze & Silver remain internal
* Delta Lake ensures reliability
* Architecture matches real production analytics pipelines

---

## 🔥 Final Result

A complete modern analytics stack:

**Excel → Python → Databricks → Delta Lake → Power BI**



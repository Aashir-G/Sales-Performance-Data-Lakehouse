# Sales Performance Data Lakehouse 📊

An end-to-end analytics project that simulates an enterprise-grade **Lakehouse architecture** using Databricks + Power BI.
It ingests raw sales data, transforms it through Bronze → Silver → Gold layers, and delivers clean KPI-driven dashboards for business decision making.

![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi\&logoColor=black)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?logo=apache-spark\&logoColor=white)
![Lakehouse](https://img.shields.io/badge/Lakehouse-Architecture-4B8BBE)

---

## Features ✨

### 🏗️ Medallion Architecture

Implements a professional Lakehouse pipeline:

* **Bronze Layer** – Raw ingested data
* **Silver Layer** – Cleaned and structured data
* **Gold Layer** – Aggregated KPIs and analytics tables

```
UI Upload
→ Silver Table
→ Bronze Table
→ Silver Table (refined)
→ Gold Tables (analytics ready)
```

Gold tables:

* `gold_kpis`
* `gold_product_perf`
* `gold_region_perf`

---

### 📈 Revenue Analytics

* Year-over-year revenue trends
* Channel-wise revenue distribution
* Business-ready KPIs for leadership reporting

---

### 🧮 Business Metrics

Calculated metrics include:

* Total Revenue
* Average Order Value (AOV)
* Order Count
* Revenue by Channel
* Revenue by Region
* Product Performance

---

### 📊 Power BI Dashboard

Interactive dashboard features:

* Revenue trend visualization
* Channel performance bar charts
* Date range filtering (Between slicer)
* Enterprise-style layout
* Clean executive reporting design

---

### ⚙️ Enterprise-Style Data Pipeline

* PySpark transformations
* Delta tables
* SQL Warehouse / Cluster integration
* Power BI Direct connection via Databricks

This mirrors how real companies structure their analytics stacks.

---

## Architecture Overview 🏛️

```
CSV Upload
   ↓
Databricks FileStore (DBFS)
   ↓
Bronze Table (Raw)
   ↓
Silver Table (Cleaned)
   ↓
Gold Tables (Aggregations)
   ↓
Power BI Dashboard
```

---

## File Structure 📁

```
Sales-Performance-Data-Lakehouse/
├── data/
│   └── processed/
│       └── silver_sales.csv
├── databricks/
│   └── lakehouse_pipeline.py   # Full PySpark pipeline
├── powerbi/
│   └── sales_dashboard.pbix    # Power BI report
├── README.md
```

---

## Technologies Used 🛠️

* **Databricks** – Distributed processing & Lakehouse storage
* **PySpark** – Data transformations and aggregations
* **Delta Lake** – Transactional tables
* **Power BI** – Visualization & analytics
* **SQL Warehouse** – BI connectivity
* **DBFS** – File ingestion

---

## Setup & Execution 🚀

### 1. Upload Data

Upload the CSV file:

```
/FileStore/tables/silver_sales.csv
```

---

### 2. Run the Pipeline in Databricks

Create a new Python notebook and paste the pipeline code.

Attach a cluster and run:

```python
spark.sql("SHOW TABLES").show()
```

You should see:

```
bronze_sales
silver_sales
gold_kpis
gold_product_perf
gold_region_perf
```

Preview:

```python
display(spark.table("gold_kpis"))
display(spark.table("gold_product_perf"))
display(spark.table("gold_region_perf"))
```

---

### 3. Connect Power BI

In Power BI:

1. Get Data → Azure → Azure Databricks
2. Enter:

   * Server Hostname
   * HTTP Path
   * Authentication: Personal Access Token
3. Select:

   * `gold_kpis`
   * `gold_product_perf`
   * `gold_region_perf`

---

## Sample Insights 📊

| KPI                  | Description                    |
| -------------------- | ------------------------------ |
| Revenue Trend        | Tracks revenue over time       |
| Channel Revenue      | Breakdown by marketing channel |
| Product Performance  | Top-selling items              |
| Regional Performance | Strongest geographic markets   |

---

## Why This Project Matters 🎯

This project demonstrates:

* Real enterprise analytics architecture
* Data engineering + BI integration
* Production-style pipelines
* Recruiter-ready portfolio quality

Easy explanation in interviews:

> “I built a full Databricks Lakehouse that processes raw sales data into business KPIs and visualized everything in Power BI using a professional analytics pipeline.”

---

## Future Improvements 💭

* [ ] Real-time streaming ingestion
* [ ] Incremental Delta updates
* [ ] Data quality checks
* [ ] CI/CD deployment
* [ ] Cost optimization layer
* [ ] ML forecasting on revenue

---

## License 📄

MIT License

---

## Support 💬

Have ideas or feedback?

* Open an issue
* Submit a PR
* Or build on top of it

---

**Built to simulate real enterprise analytics systems.**
Lakehouse thinking. BI execution. Career-level portfolio project 🚀

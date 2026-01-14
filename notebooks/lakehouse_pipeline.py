from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# VS Code likes having SparkSession defined; Databricks already provides it.
spark = SparkSession.builder.appName("Sales Performance Pipeline").getOrCreate()

# =========================
# CONFIG
# =========================
# This is the table you created via "Create or modify table" from your CSV upload
RAW_TABLE = "workspace.default.silver_sales"

# Output tables (use different names to avoid collisions)
BRONZE_TABLE = "bronze_sales"
SILVER_TABLE = "silver_sales_curated"
GOLD_KPIS_TABLE = "gold_kpis"
GOLD_PRODUCT_TABLE = "gold_product_perf"
GOLD_REGION_TABLE = "gold_region_perf"

# =========================
# (OPTIONAL) CLEAN SLATE
# Run once if you want to restart fresh
# =========================
spark.sql(f"DROP TABLE IF EXISTS {BRONZE_TABLE}")
spark.sql(f"DROP TABLE IF EXISTS {SILVER_TABLE}")
spark.sql(f"DROP TABLE IF EXISTS {GOLD_KPIS_TABLE}")
spark.sql(f"DROP TABLE IF EXISTS {GOLD_PRODUCT_TABLE}")
spark.sql(f"DROP TABLE IF EXISTS {GOLD_REGION_TABLE}")

# =========================
# BRONZE LAYER
# =========================
df_bronze = spark.table(RAW_TABLE)

df_bronze.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(BRONZE_TABLE)

# =========================
# SILVER LAYER (typed + cleaned)
# =========================
df = spark.table(BRONZE_TABLE)

df_silver = (
    df
    # standardize column types
    .withColumn("order_date", F.to_date(F.col("order_date")))
    .withColumn("units", F.col("units").cast("int"))
    .withColumn("unit_price", F.col("unit_price").cast("double"))
    .withColumn("shipping_cost", F.col("shipping_cost").cast("double"))
    .withColumn("ad_spend", F.col("ad_spend").cast("double"))
    .withColumn("discount_pct", F.col("discount_pct").cast("double"))
    .withColumn("gross_revenue", F.col("gross_revenue").cast("double"))
    .withColumn("net_revenue", F.col("net_revenue").cast("double"))
    .withColumn("returns", F.col("returns").cast("int"))
    # light data quality filters
    .filter(F.col("order_date").isNotNull())
    .filter(F.col("units").isNotNull() & (F.col("units") > 0))
    .filter(F.col("unit_price").isNotNull() & (F.col("unit_price") > 0))
    .filter((F.col("discount_pct").isNull()) | ((F.col("discount_pct") >= 0) & (F.col("discount_pct") <= 0.9)))
    .fillna({"region": "Unknown", "channel": "Unknown", "product": "Unknown"})
)

df_silver.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(SILVER_TABLE)

# =========================
# GOLD LAYER (KPIs + aggregates)
# =========================
df_silver = spark.table(SILVER_TABLE)

df_gold = (
    df_silver
    .withColumn("cogs_est", F.col("gross_revenue") * F.lit(0.45))
    .withColumn("profit_est", F.col("net_revenue") - F.col("ad_spend") - F.col("cogs_est"))
)

# Daily/Channel KPI table
gold_kpis = (
    df_gold.groupBy("order_date", "channel")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.sum("ad_spend").alias("ad_spend"),
        F.countDistinct("order_id").alias("orders"),
        F.countDistinct("customer_id").alias("unique_customers"),
        F.sum("returns").alias("returns")
    )
    .withColumn("roas", F.when(F.col("ad_spend") > 0, F.col("net_revenue") / F.col("ad_spend")))
    .withColumn("aov", F.when(F.col("orders") > 0, F.col("net_revenue") / F.col("orders")))
    .withColumn("return_rate", F.when(F.col("orders") > 0, F.col("returns") / F.col("orders")))
)

gold_kpis.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(GOLD_KPIS_TABLE)

# Product performance table
gold_product = (
    df_gold.groupBy("product")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.countDistinct("order_id").alias("orders"),
        F.sum("units").alias("units_sold")
    )
    .orderBy(F.desc("net_revenue"))
)

gold_product.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(GOLD_PRODUCT_TABLE)

# Region performance table
gold_region = (
    df_gold.groupBy("region")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.countDistinct("order_id").alias("orders")
    )
    .orderBy(F.desc("net_revenue"))
)

gold_region.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(GOLD_REGION_TABLE)

# =========================
# QUICK CHECKS
# =========================
spark.sql("SHOW TABLES").show(truncate=False)

spark.table(GOLD_KPIS_TABLE).limit(20)
spark.table(GOLD_PRODUCT_TABLE).limit(20)
spark.table(GOLD_REGION_TABLE).limit(20)

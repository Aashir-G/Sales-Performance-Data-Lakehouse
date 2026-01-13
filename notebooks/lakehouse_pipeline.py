from pyspark.sql import functions as F

# =========================
# BRONZE LAYER
# =========================
# Read from the table you created via the UI
df_bronze = spark.table("workspace.default.silver_sales")

df_bronze.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_sales")


# =========================
# SILVER LAYER
# =========================
df = spark.table("bronze_sales")

df_silver = (
    df.withColumn("order_date", F.to_date("order_date"))
      .withColumn("units", F.col("units").cast("int"))
      .withColumn("unit_price", F.col("unit_price").cast("double"))
      .withColumn("shipping_cost", F.col("shipping_cost").cast("double"))
      .withColumn("ad_spend", F.col("ad_spend").cast("double"))
      .withColumn("discount_pct", F.col("discount_pct").cast("double"))
      .withColumn("gross_revenue", F.col("gross_revenue").cast("double"))
      .withColumn("net_revenue", F.col("net_revenue").cast("double"))
)

df_silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_sales")


# =========================
# GOLD LAYER
# =========================
df_gold = (
    df_silver
    .withColumn("cogs_est", F.col("gross_revenue") * F.lit(0.45))
    .withColumn("profit_est", F.col("net_revenue") - F.col("ad_spend") - F.col("cogs_est"))
)

# KPI table
gold_kpis = (
    df_gold.groupBy("order_date", "channel")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.sum("ad_spend").alias("ad_spend"),
        F.countDistinct("order_id").alias("orders"),
    )
    .withColumn(
        "roas",
        F.when(F.col("ad_spend") > 0, F.col("net_revenue") / F.col("ad_spend"))
    )
)

gold_kpis.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_kpis")


# Product performance
gold_product = (
    df_gold.groupBy("product")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.countDistinct("order_id").alias("orders"),
    )
    .orderBy(F.desc("net_revenue"))
)

gold_product.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_product_perf")


# Region performance
gold_region = (
    df_gold.groupBy("region")
    .agg(
        F.sum("net_revenue").alias("net_revenue"),
        F.sum("profit_est").alias("profit_est"),
        F.countDistinct("order_id").alias("orders"),
    )
    .orderBy(F.desc("net_revenue"))
)

gold_region.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_region_perf")

# Databricks notebook source
# MAGIC %run ./Include/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/")
display(files)

# COMMAND ----------



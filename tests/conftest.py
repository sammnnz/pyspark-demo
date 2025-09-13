import os

from pyspark.sql import SparkSession
from pytest import fixture


@fixture(scope="module")
def spark_data():
    spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Demo')\
        .getOrCreate()
    product_df = spark.read.csv(
        os.path.join("sample_data", "product.csv"), header=True
        )
    category_df = spark.read.csv(
        os.path.join("sample_data", "category.csv"), header=True
        )
    product_category_df = spark.read.csv(
        os.path.join("sample_data", "product_category.csv"), header=True
        )
    yield product_df, category_df, product_category_df
    spark.stop()

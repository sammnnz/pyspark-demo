from pyspark_utils import get_all_rows_joins_unsafe
from pytest import mark
from pyspark.sql import DataFrame


@mark.parametrize(("mode", "columns"), [
    ('left', ())
])
def test_get_all_rows_joins_unsafe(spark_data, mode, columns):
    df1, df2, jdf = spark_data
    # TODO: impl test
    assert True

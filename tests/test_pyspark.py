from pyspark.sql import Row
from pyspark.sql.functions import col
from pyspark_utils import get_all_rows_joins_unsafe
from pytest import mark
from typing import List


@mark.parametrize(("df1_pk", "df2_pk", "join_df1_pk", "join_df2_pk", "mode"), [
    ('id', 'id', "product_id", "category_id", "left"),
    ('id', 'id', "product_id", "category_id", "right"),
])
def test_get_all_rows_joins_unsafe(spark_data, 
                                   df1_pk, 
                                   df2_pk, 
                                   join_df1_pk, 
                                   join_df2_pk, 
                                   mode):
    df1, df2, jdf = spark_data
    jdf_data: List[Row] = jdf.collect()
    result_df = get_all_rows_joins_unsafe(df1, df2, jdf, 
                                          df1_pk=df1_pk, 
                                          df2_pk=df2_pk,
                                          join_df1_pk=join_df1_pk,
                                          join_df2_pk=join_df2_pk,
                                          columns=None,
                                          mode=mode)
    result_df.show()
    id_1 = result_df.columns.index(df1_pk)
    id_2 = result_df.columns.index(df2_pk, id_1+1)
    for item in result_df.where(col(join_df1_pk).isNotNull()).collect():
        _ = Row(**{join_df1_pk: item[id_1], join_df2_pk: item[id_2]})
        assert _ == jdf_data.pop(0)

    assert len(jdf_data) == 0
    # TODO: make check for nulls

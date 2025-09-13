from pyspark.sql import DataFrame
from typing import List, Literal, Tuple, Union

__all__ = ["get_all_rows_joins_unsafe"]


def get_all_rows_joins_unsafe(
        df1: DataFrame, df2: DataFrame, join_df: DataFrame, *, 
        df1_pk: str = 'id', 
        df2_pk: str = 'id', 
        join_df1_pk: str, 
        join_df2_pk: str, 
        columns: Union[Tuple[str, ...], List[str], None] = None, 
        mode: Literal['left', 'right'] = 'left'
) -> DataFrame:
    """
    Get all rows according to the given joins between dataframes.

    Return:
        DataFrame

    Note:
        The '_unsafe' suffix means that input arguments are not validated and an exception may be thrown.

        The `mode` argument specifies the dataframe relative to which the rows will be retrieved.
    """
    df = join_df\
        .join(df1, getattr(df1, df1_pk) == getattr(join_df, join_df1_pk), "full")\
        .join(df2, getattr(df2, df2_pk) == getattr(join_df, join_df2_pk), mode)\
        .drop(join_df1_pk, join_df2_pk)
    
    return df.select(*columns) if columns else df

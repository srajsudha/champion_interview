from pyspark.sql import DataFrame
from pyspark.sql.functions import sum

def sum_all_values(df: DataFrame) -> int:
    total_sum = df.select(sum(df.columns[0])).collect()[0][0]
    return total_sum
from myfunctions import sum_all_values
def test_myfunction():
    data = [(3,), (7,), (10,)]
    df = spark.createDataFrame(data, ["value"])
    result = sum_all_values(df)
    assert result == 20
    
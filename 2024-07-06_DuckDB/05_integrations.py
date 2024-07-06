# DuckDB <-> Array do Numpy
import numpy as np
conn.sql("SELECT range(5, 17, 3)").fetchnumpy()
npdata = np.arange(35).reshape(5, -1)
conn.sql("FROM npdata")  # Pela variável local

# DuckDB <-> Pandas
import pandas as pd
conn.sql("SELECT * EXCLUDE column2 FROM npdata").df()
tbl = pd.DataFrame([{"a": a, "b": a ** 2} for a in range(5)])
conn.sql("FROM tbl")

# E se a variável não for local?
conn.register("dataset", tbl)  # Também há unregister
conn.sql("FROM dataset")

# DuckDB <-> Polars (exige pyarrow instalado)
import polars as pl  # COLUMNS aceita filtro por regex!
result = conn.sql("""
SELECT COLUMNS('.*[134]') FROM npdata
""").pl()
col3mod = result.select(pl.col("column3") * pl.col("column1"))
conn.sql("FROM col3mod")

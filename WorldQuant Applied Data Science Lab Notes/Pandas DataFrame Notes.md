# Notes on Pandas DataFrames

* Import:
  * `import pandas as pd`

* DataFrame type:
  * `pandas.core.frame.DataFrame`

* Read a CSV file into a DataFrame:
  * `df = pd.read_csv("filename.csv")`

* To show what columns exist and what their types are:
  * `df.info()`

* To show head/tail:
  * `df.head()`
  * `df.head(10)`
  * `df.tail()`

* To show dimensions (rows, columns):
  * `df.shape()`

* To create a DataFrame with only certain columns selected from another DataFrame:
  * `df_with_certain_columns = df[["DEBT", "HOUSES"]]`

* Masking: To select only the rows from a DataFrame that match a condition:
  * `mask = df["TURNFEAR"] == 1`
  * `df = df[mask]`



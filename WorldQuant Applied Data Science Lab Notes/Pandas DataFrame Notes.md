# Notes on Pandas DataFrames

* Import:
  * `import pandas as pd`

* DataFrame type:
  * `pandas.core.frame.DataFrame`

* Read a CSV file into a DataFrame:
  * `df = pd.read_csv("filename.csv")`
  * Note: Also works with `.csv.gz` files:
    * `df = pd.read_csv("data/SCFP2019.csv.gz")`
  
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

* Drop all rows with NaN values:
  * `df = df.dropna()`
  * `df.dropna(inplace=True)`
  * Can also drop columns with NaN values: `df.dropna(axis="columns")`

* Apply a function:
  * `top_ten_trim_var = df.apply(trimmed_var, limits=(0.1, 0.1)).sort_values().tail(5)`

* Get the values of the index column as a list:
  * `top_ten_trim_var.index.to_list()`
  * Output: `['DEBT', 'NETWORTH', 'HOUSES', 'NFIN', 'ASSET']`

* Get a copy of a DataFrame with only certain columns included:
  * `high_var_cols = ['DEBT', 'NETWORTH', 'HOUSES', 'NFIN', 'ASSET']`
  * `X = df[high_var_cols]`

* Convert all values in a DataFrame to type `int`
  * `df.astype(int)`

* Find the mean and standard deviation for all columns in a DataFrame
  * `df.aggregate(["mean", "std"])`

* Count the number of rows where column "BUS" has the value 1:
  * `count = len([x for x in df["HBUS"] if x == 1])`
  * Or, more efficiently and idiomatically with Pandas: `count = (df["HBUS"] == 1).sum()`





* TODO: DataFrame versus Series versus Numpy Arrays versus Python list versus Python dictionary
  * Comparison chart of how to do operations with each one
  * TODO: See https://pandas.pydata.org/pandas-docs/version/0.21/10min.html
  * TODO: See https://pandas.pydata.org/pandas-docs/version/0.21/dsintro.html#dsintro
  * TODO: DataFrame iloc() function: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html





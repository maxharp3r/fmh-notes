# pandas

* clean
    * address missing
    * remove outliers
    * continuous => bins?
* featurize
    * normalize continuous
    * categorical => one hot
* split (train/test, x/y)
* model
* eval

```python
# read
df = pd.read_csv("path/to/file", sep=",", index_col="foo")

# info
df.info() # will also show columns with nulls
df["col"].describe()  # for continuous
df["col"].hist()
df["col"].value_counts(dropna=False)  # for categorical

# indexes
df.set_index("col", inplace=True)
df.reset_index(inplace=True)

# selecting rows
df.loc[0:2]  # by index; 3 results
df.iloc[0:2]  # by row number; 2 results (exclusive on right bound)

# selecting/dropping columns
df.loc[:, df.dtypes == np.float64]  # np.int64, "float", "object"
df.loc[:, df.columns != "foo"]
df.loc[:, ~df.columns.isin(["foo", "bar"])]
df.drop(columns=["foo"], inplace=True)

# finding/filling NA
df[df.isnull().any(axis=1)]
df["col"].fillna("missing", inplace=True)

# Find outliers above the 99th percentile
percentile_99 = df["col"].quantile(0.99)
outliers = df[df["col"] > percentile_99]

# binning
df["age_cat"] = pd.cut(df["age"], bins=[0, 20, 100], labels=["0-20", "20+"], right=False) # vals outside of range become NaN
df["age_cat"] = df["age_cat"].cat.add_categories("missing").fillna("missing")

# normalize / standardize min-max
(df["cat"] - df["cat"].mean()) / df["cat"].std()
(df["cat"] - df["cat"].min()) / (df["cat"].max() - df["cat"].min())

# apply (series)
df["col"].apply(lambda s: s[0])

# groupby for analytics
df.groupby("col")["foo"].value_counts()  # categorical
df.groupby("col")["foo"].describe()  # numerical

```

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

## Validated DataFrame

```python
class ValidatedDataFrame(pd.DataFrame):
    """A DataFrame that validates against a Pydantic schema.

    Useful so that we can pass around validated, typed dataframes, allowing us to leverage
    python typing to check inputs/outputs rather than passing around vanilla dataframes.

    example usage:
    class ExampleSchema(BaseModel):
        name: str
        department: str
        age: Optional[int] = None

    class ExampleDataFrame(ValidatedDataFrame):
        schema = ExampleSchema

    data = {'name': ['Alice'], 'department': ['Engineering']}
    my_df = ExampleDataFrame(pd.DataFrame(data))
    """

    schema: Type[BaseModel]

    def __init__(self, df: pd.DataFrame):
        """Wrap a dataframe.

        # , underscores_to_spaces: bool = False

        Args:
            data (pd.DataFrame): the dataframe, will be validated during __init__
        """
        super().__init__(df)
        self.validate(df)

    def validate(self, data: pd.DataFrame):
        """Validate the first row of the DataFrame against the Pydantic schema."""
        if data.empty:
            raise ValueError("DataFrame is empty.")

        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")

        row_dict = data.iloc[0].to_dict()

        try:
            self.schema(**row_dict)
        except ValidationError as e:
            errors = e.errors()
            error_messages = []

            for error in errors:
                field_name = error["loc"][-1]
                message = f"Field '{field_name}' error: {error['msg']}"
                error_messages.append(message)

            raise ValueError(f"DataFrame schema validation error: {', '.join(error_messages)}")
```

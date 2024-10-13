# sklearn

## preprocessing

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.compose import ColumnTransformer

# one-hot
onehot = OneHotEncoder(sparse_output=False, drop="first")
category_encoded = onehot.fit_transform(df[['foo']])
col_names = [f"foo_{cat}" for cat in onehot.categories_[0]]
df_onehot = pd.DataFrame(category_encoded, columns=col_names, index=df.index)

# min-max scale (normalization)
min_max = MinMaxScaler()
min_max.fit(train_df[[col]])
df["col"] = min_max.transform(train_df[["col"]])
```

## model training

```python
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_X, train_y)
lr.predict(train_X)
```

## metrics

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_true, y_pred)
```

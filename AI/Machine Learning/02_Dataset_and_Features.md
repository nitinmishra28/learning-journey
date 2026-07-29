# 02 - Dataset Exploration using Pandas

## 🎯 Goal

Before training any Machine Learning model, we must first understand our dataset.

Questions we should answer:

- How many rows and columns are there?
- What are the column names?
- What is the datatype of each column?
- Are there missing values?
- Are there duplicate rows?
- What kind of data do we have?

This process is called **Dataset Exploration**.

---

# Why Dataset Exploration?

Imagine your company gives you an Excel file.

Before building a forecasting model, you should know:

- Is the dataset complete?
- Are dates stored correctly?
- Is Sales Quantity numeric?
- Are there missing values?
- Which columns are useful?

Without understanding the dataset, we cannot build a reliable ML model.

---

# Step 1 - Import Pandas

Pandas is a Python library used for data manipulation and analysis.

```python
import pandas as pd
```

Why?

Because Python itself cannot easily analyze tables like Excel files.

Pandas provides a DataFrame, which makes working with tabular data much easier.

---

# Step 2 - Load the Dataset

Example

```python
df = pd.read_excel("../data/raw/sales_data.xlsx")
```

or

```python
df = pd.read_csv("sales.csv")
```

### Why do we load the dataset?

The model cannot directly read Excel or CSV files.

We first load the data into a **DataFrame**, where we can inspect, clean, and prepare it.

---

# Step 3 - View the First Few Rows

```python
df.head()
```

Output

| Posting Date | Product | Sales Quantity |
|--------------|----------|---------------:|
|2025-01-01|Urea|120|
|2025-01-02|DAP|145|
|2025-01-03|Urea|132|

### Why use `head()`?

Datasets may contain thousands of rows.

Instead of printing everything, `head()` shows the first **5 rows** by default.

You can also specify the number of rows:

```python
df.head(10)
```

---

# Step 4 - View the Last Few Rows

```python
df.tail()
```

### Why use `tail()`?

Useful for checking:

- Whether the file loaded completely.
- Whether the last rows contain unexpected values.

Example

```python
df.tail(3)
```

---

# Step 5 - Check Dataset Shape

```python
df.shape
```

Example Output

```python
(20321, 22)
```

Meaning

- 20,321 rows
- 22 columns

### Why is this important?

It tells us how large the dataset is.

This helps estimate memory usage and training time.

---

# Step 6 - View Column Names

```python
df.columns
```

Example

```python
Index([
'Posting Date',
'CustomerName',
'ItemCode',
'Sales Quantity'
])
```

### Why?

Before selecting features, we need to know what columns are available.

---

# Step 7 - Check Data Types

```python
df.dtypes
```

Example

```python
Posting Date      datetime64
ItemCode          object
Sales Quantity    int64
Amount            float64
```

### Why?

The model expects the correct datatype.

Example

If Sales Quantity is stored as text,

```
"120"
```

instead of

```
120
```

the model cannot learn properly.

---

# Common Data Types

| Datatype | Meaning |
|----------|---------|
| int64 | Integer numbers |
| float64 | Decimal numbers |
| object | Text |
| datetime64 | Date & Time |
| bool | True / False |

---

# Step 8 - Dataset Information

```python
df.info()
```

Example

```text
RangeIndex: 20321 entries

22 columns

Non-Null Count

Dtypes
```

### Why?

`info()` gives a quick overview of the dataset.

It tells us:

- Number of rows
- Number of columns
- Missing values
- Datatypes
- Memory usage

---

# Step 9 - Statistical Summary

```python
df.describe()
```

Example

| | Sales |
|---|------:|
|count|20321|
|mean|158.4|
|std|42.1|
|min|2|
|max|650|

### Why?

Useful for understanding numerical columns.

We can quickly detect:

- Unusually high values
- Negative values
- Large variations

---

# Step 10 - Missing Values

```python
df.isnull().sum()
```

Example

```python
Posting Date       0
State              0
Sales Quantity    18
Amount            42
```

### Why?

Machine Learning models generally cannot handle missing values directly.

We must identify and clean them before training.

---

# Step 11 - Duplicate Rows

```python
df.duplicated().sum()
```

Example

```python
12
```

Meaning

The dataset contains **12 duplicate rows**.

### Why?

Duplicates can bias the model and should usually be removed.

---

# Step 12 - Unique Values

```python
df["State"].unique()
```

Example

```python
['MP', 'UP', 'Delhi']
```

Count unique values

```python
df["State"].nunique()
```

### Why?

Helps understand categorical columns.

Example:

How many different states exist?

---

# Step 13 - Value Counts

```python
df["State"].value_counts()
```

Example

```python
MP       5200
UP       4300
Delhi    3100
```

### Why?

Useful for checking class distribution and understanding the data.

---

# Step 14 - Selecting Columns

Single Column

```python
df["Sales Quantity"]
```

Multiple Columns

```python
df[["Posting Date", "Sales Quantity"]]
```

### Why?

Later, we will select only useful columns (Features).

---

# Step 15 - Filtering Data

Example

```python
df[df["Year"] == 2025]
```

Another Example

```python
df[df["Sales Quantity"] > 500]
```

### Why?

Filtering helps inspect specific subsets of the data.

---

# Step 16 - Sorting Data

```python
df.sort_values("Sales Quantity")
```

Descending Order

```python
df.sort_values("Sales Quantity", ascending=False)
```

### Why?

Useful for finding:

- Highest sales
- Lowest sales
- Outliers

---

# Real Workflow

```
Excel File
      ↓
Read using Pandas
      ↓
Understand Dataset
      ↓
Find Problems
      ↓
Clean Data
      ↓
Feature Engineering
      ↓
Train Machine Learning Model
```

---

# Golden Rules

✅ Never train a model without understanding the dataset.

✅ Always check:

- Shape
- Columns
- Datatypes
- Missing Values
- Duplicates

These five checks should be your habit in every ML project.

---

# Interview Questions

### Why do we use Pandas?

To load, inspect, clean, and manipulate tabular data before training a Machine Learning model.

---

### What does `df.shape` return?

A tuple:

```
(rows, columns)
```

---

### Difference between `head()` and `tail()`?

- `head()` shows the first rows.
- `tail()` shows the last rows.

---

### Why is `df.info()` useful?

It provides a quick summary of:

- Rows
- Columns
- Datatypes
- Missing values
- Memory usage

---

### Why should we check missing values?

Most ML algorithms cannot work directly with missing data.

---

# 📝 Key Takeaways

- Every ML project starts with dataset exploration.
- Pandas is used to read and inspect datasets.
- `head()` and `tail()` help preview the data.
- `shape` tells us the dataset size.
- `columns` lists all available columns.
- `dtypes` shows the datatype of each column.
- `info()` provides an overall summary.
- `describe()` summarizes numerical data.
- Missing values and duplicates should be identified before model training.
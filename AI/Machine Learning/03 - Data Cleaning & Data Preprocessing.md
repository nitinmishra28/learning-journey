# 03 - Data Cleaning & Data Preprocessing

## 🎯 Goal

Real-world datasets are never perfect.

Before training a Machine Learning model, we must clean and prepare the data.

This process is called **Data Cleaning** or **Data Preprocessing**.

---

# Why Do We Need Data Cleaning?

Suppose the company gives us this dataset.

| Product | Price | Sales Quantity |
|----------|------:|---------------:|
| Urea | 500 | 120 |
| DAP | NULL | 145 |
| Urea | 500 | 120 |
| NPK | -100 | 180 |

Problems:

- Missing values
- Duplicate rows
- Invalid values
- Wrong datatypes

If we train a model on this data,

❌ Predictions will be poor.

---

# Real ML Workflow

```
Raw Dataset
      ↓
Explore Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Model Training
```

Never skip Data Cleaning.

---

# Step 1 - Check Missing Values

Missing values are empty cells in a dataset.

Example

| Product | Price |
|----------|------:|
| Urea | 500 |
| DAP | NULL |

### Code

```python
df.isnull().sum()
```

Example Output

```text
Price              12
Sales Quantity      3
```

### Why?

Most Machine Learning algorithms cannot work with missing values.

We must identify them before training.

---

# Step 2 - Calculate Missing Percentage

Sometimes the count alone is not enough.

### Code

```python
(df.isnull().sum() / len(df)) * 100
```

Example Output

```text
Price              2.1%
Amount             8.3%
```

### Why?

If a column has

- 1% missing → Fill it
- 90% missing → Consider dropping it

---

# Step 3 - Remove Duplicate Rows

Duplicate rows repeat the same information.

Example

| Product | Sales |
|----------|------:|
| Urea | 120 |
| Urea | 120 |

### Check duplicates

```python
df.duplicated().sum()
```

### Remove duplicates

```python
df = df.drop_duplicates()
```

### Why?

Duplicates give extra importance to repeated records and can bias the model.

---

# Step 4 - Check Data Types

### Code

```python
df.dtypes
```

Example

```text
Sales Quantity      object
Price               float64
Posting Date        object
```

### Why?

Machine Learning models require correct datatypes.

For example,

Sales Quantity should be numeric, not text.

---

# Step 5 - Convert Data Types

Example

```python
df["Posting Date"] = pd.to_datetime(df["Posting Date"])
```

Convert to integer

```python
df["Sales Quantity"] = df["Sales Quantity"].astype(int)
```

### Why?

Correct datatypes make calculations and feature engineering possible.

---

# Step 6 - Rename Columns

Sometimes column names contain spaces or special characters.

Example

```
Sales Quantity
```

Rename it

```python
df.rename(columns={
    "Sales Quantity": "Sales_Quantity"
}, inplace=True)
```

### Why?

Short and consistent names make coding easier.

---

# Step 7 - Remove Unnecessary Columns

Example

| Column |
|---------|
| Customer Name |
| Invoice Number |
| Sales Quantity |

Customer Name usually doesn't help predict future sales.

### Code

```python
df.drop(
    columns=["Customer Name", "Invoice Number"],
    inplace=True
)
```

### Why?

Unnecessary columns increase noise and slow down training.

---

# Step 8 - Check Unique Values

```python
df["State"].unique()
```

Count them

```python
df["State"].nunique()
```

### Why?

Helps understand categorical columns.

Example

```
MP
UP
Delhi
```

---

# Step 9 - Standardize Text

Sometimes the same value appears in different formats.

Example

```
Delhi

delhi

DELHI
```

Convert everything to lowercase.

```python
df["State"] = df["State"].str.lower()
```

Or uppercase.

```python
df["State"] = df["State"].str.upper()
```

### Why?

The model should treat all these as the same category.

---

# Step 10 - Strip Extra Spaces

Example

```
" Delhi "

```

Code

```python
df["State"] = df["State"].str.strip()
```

### Why?

Leading and trailing spaces create duplicate categories.

---

# Step 11 - Handle Invalid Values

Example

| Price |
|------:|
|500|
|-100|

Negative price is invalid.

Check

```python
df[df["Price"] < 0]
```

### Why?

Business rules help identify impossible values.

---

# Step 12 - Save the Clean Dataset

```python
df.to_csv(
    "../data/processed/clean_sales.csv",
    index=False
)
```

### Why?

Instead of cleaning every time,

we save the cleaned dataset for future use.

---

# Cleaning Checklist

Before training a model, always check:

✅ Missing values

✅ Duplicate rows

✅ Datatypes

✅ Invalid values

✅ Column names

✅ Extra spaces

✅ Text formatting

---

# Real Retail Forecasting Workflow

```
Raw Excel File
       ↓
Read using Pandas
       ↓
Check Shape
       ↓
Check Missing Values
       ↓
Remove Duplicates
       ↓
Fix Datatypes
       ↓
Remove Unnecessary Columns
       ↓
Save Clean Dataset
```

---

# Interview Questions

### Why is Data Cleaning important?

Because Machine Learning models expect clean and consistent data.

Poor-quality data leads to poor predictions.

---

### Why remove duplicate rows?

Duplicates can bias the model and reduce data quality.

---

### Why convert datatypes?

To ensure numerical operations and model training work correctly.

---

### Why remove unnecessary columns?

They add noise and do not help the model learn meaningful patterns.

---

### Why standardize text?

To avoid treating values like

```
Delhi

DELHI

delhi
```

as different categories.

---

# Best Practices

- Explore data before cleaning.
- Never modify the original raw dataset.
- Save the cleaned dataset separately.
- Validate every cleaning step.
- Document all transformations.

---

# 📝 Key Takeaways

- Data Cleaning is one of the most important phases of any ML project.
- Always check for missing values, duplicates, and incorrect datatypes.
- Remove unnecessary columns before model training.
- Standardize text values and clean formatting issues.
- Save the cleaned dataset separately for reproducibility.
- Clean data leads to better Machine Learning models.
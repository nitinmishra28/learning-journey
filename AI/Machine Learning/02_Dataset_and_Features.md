# 02 - Dataset, Samples, Features & Target

## 🎯 Goal

Understand the basic terminology of Machine Learning datasets.

After this chapter you should be able to identify:

- Dataset
- Sample
- Observation
- Record
- Feature
- Target
- Label
- X and y

---

# 1. What is a Dataset?

A dataset is a collection of observations (rows) used to train a Machine Learning model.

Example

| Month | State | Item | Sales |
|--------|-------|------|------:|
| Jan | MP | Urea | 100 |
| Jan | UP | Urea | 120 |
| Feb | MP | Urea | 150 |
| Feb | UP | DAP | 180 |

The complete table is called a **Dataset**.

---

# 2. What is a Sample?

Each row inside a dataset is called a:

- Sample
- Observation
- Record

All three terms mean the same thing.

Example

| Month | State | Item | Sales |
|--------|-------|------|------:|
| Jan | MP | Urea | 100 |

This single row is **one sample**.

---

# 3. Dataset Structure

```
Dataset
│
├── Sample 1
├── Sample 2
├── Sample 3
└── Sample N
```

---

# 4. What is a Feature?

Features are the input variables given to the model.

Example

| Month | State | Item | Sales |
|--------|-------|------|------:|
| Jan | MP | Urea | 100 |

Features are:

- Month
- State
- Item

These help the model learn patterns.

---

# 5. What is a Target?

The target is the value we want the model to predict.

Example

| Month | State | Item | Sales |
|--------|-------|------|------:|
| Jan | MP | Urea | 100 |

Target

```
Sales = 100
```

For our Retail Forecasting project,

```
Target = Sales Quantity
```

---

# 6. Feature vs Target

| Feature | Target |
|----------|---------|
| Input | Output |
| Used for learning | Predicted by the model |
| Multiple columns | Usually one column |

Example

```
Features

Month
State
Brand
ItemCode
Territory

↓

Model

↓

Target

Sales Quantity
```

---

# 7. Raw Data vs Features

Raw Data comes directly from the business.

Example

| Posting Date | Customer Name | Invoice No | Sales Quantity |
|--------------|---------------|------------|----------------|

Raw data contains

- Useful columns
- IDs
- Duplicate information
- Noise
- Missing values

---

Features are useful information extracted from raw data.

Example

Raw Data

```
Posting Date = 15-Jul-2026
```

Features

```
Month = July

Quarter = Q3

Year = 2026
```

Another Example

Raw Data

```
Sales Quantity
```

Feature Engineering

```
Lag 1 Month Sales

Rolling Average

Lag 12 Month Sales
```

These features are created by us.

---

# 8. Columns ≠ Features

Not every column becomes a feature.

Example

| Column | Used as Feature? |
|---------|------------------|
| Customer Name | ❌ |
| Invoice Number | ❌ |
| Posting Date | ✅ |
| ItemCode | ✅ |
| Territory | ✅ |
| Sales Quantity | 🎯 Target |

Always select only meaningful columns.

---

# 9. Dataset Shape

The size of a dataset is represented as

```
(rows, columns)
```

Example

```
(20321,22)
```

Means

- 20,321 rows
- 22 columns

Python

```python
df.shape
```

---

# 10. Shape does NOT mean Features

Example

```
Dataset Shape

(20321,22)
```

Does **NOT** mean 22 Features.

Because some columns may be

- IDs
- Duplicate columns
- Target
- Metadata

Example

| Column | Feature? |
|---------|-----------|
| CustomerCode | ❌ |
| CustomerName | ❌ |
| Sales Quantity | 🎯 Target |
| Month | ✅ |
| ItemCode | ✅ |

---

# 11. X and y

Machine Learning uses a standard notation.

```
X

↓

Input Features

↓

Model

↓

Output

↓

y
```

Python Example

```python
X = df[["Month", "State", "ItemCode"]]

y = df["Sales Quantity"]
```

Where

```
X = Features

y = Target
```

---

# 12. Labels

Regression terminology

```
Target = Label
```

Both terms refer to the value we want to predict.

Example

```
Sales Quantity

↓

Target

↓

Label
```

---

# 13. Retail Forecasting Example

Dataset

| Month | Territory | Item | Brand | Sales Qty |
|--------|-----------|------|--------|----------:|
| Jul | MP | Pesticide A | Bayer | 220 |

Features

- Month
- Territory
- Item
- Brand

Target

```
Sales Quantity
```

---

# 14. Machine Learning View of a Dataset

```
Dataset

↓

Samples (Rows)

↓

Features (Inputs)

↓

Model

↓

Target Prediction
```

---

# 15. Important Terminology

| ML Term | Database Equivalent |
|----------|---------------------|
| Dataset | Table |
| Sample | Row |
| Feature | Column (Input) |
| Target | Output Column |
| Observation | Row |
| Record | Row |

---

# ⭐ Golden Rules

### Rule 1

A dataset is a collection of samples.

---

### Rule 2

Each row is called a sample (or observation or record).

---

### Rule 3

Features are the inputs given to the model.

---

### Rule 4

The target is what we want to predict.

---

### Rule 5

Not every column should be used as a feature.

---

### Rule 6

```
X = Features

y = Target
```

This is the universal Machine Learning convention.

---

# 📝 Key Takeaways

- A dataset is a collection of samples.
- Every row is one sample.
- Features are input variables.
- Target is the output variable.
- Raw data must be transformed into useful features.
- Dataset shape tells only rows and columns.
- Not every column becomes a feature.
- X represents features.
- y represents the target.
- Good feature selection is more important than having many columns.
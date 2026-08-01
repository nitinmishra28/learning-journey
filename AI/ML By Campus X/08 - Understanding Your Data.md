# Day 08 - Understanding Your Data (Part 1)

> **Course:** CampusX - 100 Days of Machine Learning

---

# 🎯 Learning Objectives

After completing this lecture, you will be able to:

- Understand why data understanding is important.
- Learn what to check before building a Machine Learning model.
- Understand the structure of a dataset.
- Identify features and target variables.
- Get familiar with common Pandas functions for understanding data.

---

# 📚 Prerequisites

Before starting this lecture, you should know:

- Machine Learning Development Life Cycle
- Basic Python
- Basic Pandas

---

# Introduction

Many beginners make the same mistake.

```
Dataset

↓

Train Model

↓

Prediction
```

This is **not** the correct workflow.

Before training any Machine Learning model, you should first understand the dataset.

A Machine Learning engineer spends a significant amount of time understanding the data before writing any model.

---

# What Does "Understanding Your Data" Mean?

Understanding your data means exploring the dataset to answer questions like:

- What information is available?
- How many features are present?
- Which column is the target?
- What type of data does each column contain?
- Are there missing values?
- Is the dataset suitable for Machine Learning?

This step helps us avoid mistakes later in the pipeline.

---

# Why Is It Important?

Imagine someone gives you an Excel file with 500 columns.

Would you directly train a model?

No.

First, you would try to understand:

- What each column represents.
- Which columns are useful.
- Which columns contain errors.
- Which column should be predicted.

Without understanding the dataset, model building becomes guesswork.

---

# Step 1: Load the Dataset

The first step is loading the dataset into memory.

Example

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

After loading,

always inspect the dataset.

---

# Step 2: View the Dataset

The most commonly used function is

```python
df.head()
```

Output

```
First 5 rows of the dataset
```

To see the last rows

```python
df.tail()
```

---

# Why Use head()?

- Verify that the file loaded correctly.
- Check column names.
- Understand the structure.
- Spot obvious errors.

---

# Step 3: Check Dataset Shape

Shape tells us

- Number of rows
- Number of columns

```python
df.shape
```

Example Output

```
(1000, 12)
```

Meaning

- 1000 records
- 12 columns

---

# Why Is Shape Important?

It gives a quick idea of the dataset size.

Examples

```
(500, 5)
```

Small dataset.

---

```
(1000000, 45)
```

Large dataset.

---

# Step 4: Check Sample Records

Instead of reading the entire dataset,

observe a few records.

Example

| Age | Salary | Purchased |
|------|---------|-----------|
| 25 | 30000 | Yes |
| 32 | 50000 | No |
| 40 | 70000 | Yes |

From just a few rows,

you can identify:

- Numerical columns
- Categorical columns
- Possible target variable

---

# Step 5: Understand the Columns

Use

```python
df.columns
```

Example Output

```
Index([
'Age',
'Salary',
'Gender',
'Purchased'
])
```

Now you know what information is available.

---

# Features vs Target

Example Dataset

| Age | Salary | Purchased |
|------|---------|-----------|

Features

```
Age

Salary
```

Target

```
Purchased
```

Features are used as input.

Target is what we want to predict.

---

# Step 6: Check Data Types

Use

```python
df.info()
```

Example Output

```
Age          int64

Salary       float64

Gender       object

Purchased    object
```

---

# Why Check Data Types?

Because Machine Learning algorithms expect data in specific formats.

Example

```
Age

↓

Integer
```

Good.

---

```
Salary

↓

Float
```

Good.

---

```
Purchased

↓

Object
```

May need encoding later.

---

# Common Data Types

| Data Type | Example |
|------------|----------|
| int64 | 25 |
| float64 | 25.6 |
| object | Male |
| bool | True |
| datetime | 2025-07-20 |

---

# Retail Sales Forecasting Example

Suppose we have

| Date | Store | Product | Sales |
|------|--------|----------|------|

Checking

```python
df.info()
```

helps us verify:

- Date is datetime
- Sales is numeric
- Product is categorical

This information helps during preprocessing.

---

# Interview Questions

### Why should we understand the dataset before model training?

Because understanding the dataset helps identify features, target variables, data types, and potential issues before building the model.

---

### What does `df.shape` return?

It returns the number of rows and columns.

---

### What is the purpose of `df.head()`?

It displays the first five rows to quickly inspect the dataset.

---

### Why is `df.info()` important?

It provides column names, data types, and missing value information.

---

# Common Mistakes

❌ Start training immediately after loading data.

✅ Inspect the dataset first.

---

❌ Ignore data types.

✅ Verify every column's data type.

---

❌ Assume the target variable.

✅ Confirm it before training.

---

# Key Takeaways

- Understanding the dataset is the first practical step after loading it.
- Always inspect rows, columns, shape, and data types.
- Identify features and target before preprocessing.
- Pandas provides powerful functions for quick dataset exploration.

---

# What's Next?

In **Part 2**, we will learn:

- Missing Values
- Duplicate Records
- Statistical Summary
- Value Counts
- Unique Values
- Descriptive Statistics
- Data Quality Checks


# Day 08 - Understanding Your Data (Part 2)

> **Topics Covered**
>
> - Missing Values
> - Duplicate Records
> - Statistical Summary
> - Unique Values
> - Value Counts
> - Memory Usage
> - Data Quality Checks

---

# Step 7: Check Missing Values

## Definition

Missing values are data points where information is not available.

Example

| Name | Age | Salary |
|------|-----|--------|
| Rahul | 25 | 30000 |
| Amit | NULL | 45000 |
| Neha | 28 | NULL |

Missing values are one of the most common problems in Machine Learning datasets.

---

# Why Should We Check Missing Values?

Many ML algorithms cannot handle missing values directly.

If ignored, they may:

- Produce incorrect predictions
- Cause training errors
- Reduce model accuracy

---

# Python Example

```python
df.isnull().sum()
```

Example Output

```
Age          5

Salary      12

Gender       0
```

Meaning

- Age has 5 missing values.
- Salary has 12 missing values.

---

# Retail Example

| Product | Sales |
|----------|------:|
| Milk | 120 |
| Bread | NULL |
| Eggs | 95 |

Before training a forecasting model,

we must decide how to handle the missing sales value.

---

# Step 8: Check Duplicate Records

Duplicate rows increase dataset size unnecessarily and may bias the model.

Example

| Customer | Product |
|----------|----------|
| A | Milk |
| A | Milk |

The second row may be an accidental duplicate.

---

# Python Example

```python
df.duplicated().sum()
```

To remove duplicates

```python
df.drop_duplicates()
```

---

# Why Remove Duplicates?

Duplicates can

- Increase training time
- Bias statistics
- Distort model learning

---

# Step 9: Statistical Summary

One of the most useful Pandas functions is

```python
df.describe()
```

It generates summary statistics for numerical columns.

Example Output

| Statistic | Age |
|-----------|----:|
| Count | 1000 |
| Mean | 35.8 |
| Std | 8.2 |
| Min | 18 |
| 25% | 28 |
| 50% | 35 |
| 75% | 42 |
| Max | 65 |

---

# Understanding Each Metric

## Count

Number of non-missing values.

---

## Mean

Average value.

Formula

```
Sum of Values

──────────────

Number of Values
```

---

## Standard Deviation (Std)

Measures how spread out the data is.

- Small Std → Values are close together.
- Large Std → Values are widely spread.

---

## Minimum

Smallest value in the column.

---

## Maximum

Largest value in the column.

---

## Quartiles

### 25%

25% of observations lie below this value.

---

### 50%

Median (middle value).

---

### 75%

75% of observations lie below this value.

---

# Why is describe() Important?

It helps identify:

- Outliers
- Data distribution
- Missing values (through count)
- Suspicious values

---

# Retail Example

Suppose

```
Average Sales = 220

Maximum Sales = 18000
```

Immediately,

you may suspect an outlier or a special event.

---

# Step 10: Unique Values

To know how many distinct values exist in a column,

use

```python
df["Gender"].nunique()
```

Example Output

```
2
```

Meaning

Only two unique values exist.

---

# Why is nunique() Useful?

It helps identify:

- Categorical features
- Identifier columns
- Low-cardinality columns

---

# Step 11: Value Counts

Sometimes,

knowing unique values is not enough.

We also need their frequencies.

Example

```python
df["Gender"].value_counts()
```

Output

```
Male      650

Female    350
```

---

# Why is value_counts() Important?

It helps identify:

- Class imbalance
- Dominant categories
- Rare categories

---

# Retail Example

Product Category

```
Milk      1200

Bread      850

Eggs       600

Butter      20
```

Butter appears very rarely.

This insight may influence preprocessing or business decisions.

---

# Step 12: Memory Usage

Large datasets consume memory.

To inspect memory usage

```python
df.memory_usage()
```

or

```python
df.info()
```

Example

```
Memory Usage

45.8 MB
```

Knowing memory usage is useful when working with large datasets.

---

# Complete Data Inspection Checklist

Whenever you receive a new dataset,

check the following:

✅ Shape

✅ Head

✅ Tail

✅ Columns

✅ Data Types

✅ Missing Values

✅ Duplicates

✅ Statistical Summary

✅ Unique Values

✅ Value Counts

---

# Python Summary

```python
df.head()

df.tail()

df.shape

df.columns

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df.nunique()

df["Gender"].value_counts()
```

These commands are enough to perform an initial inspection of most datasets.

---

# Interview Questions

### Why do we check missing values?

To identify incomplete data before model training.

---

### What does describe() return?

Summary statistics for numerical columns.

---

### What is the purpose of value_counts()?

It returns the frequency of each unique value in a column.

---

### Difference between unique() and nunique()?

- `unique()` returns the actual unique values.
- `nunique()` returns only the count of unique values.

---

### Why remove duplicate records?

Duplicates may bias the model and distort statistics.

---

# Common Mistakes

❌ Ignoring missing values.

✅ Always inspect them before preprocessing.

---

❌ Using describe() on all columns and assuming it summarizes categorical data.

✅ By default, `describe()` focuses on numerical columns (unless configured otherwise).

---

❌ Assuming balanced classes.

✅ Verify class distribution using `value_counts()`.

---

# Key Takeaways

- Missing values must be identified before training.
- Duplicate records should be checked and handled appropriately.
- `describe()` provides a quick statistical overview.
- `nunique()` and `value_counts()` help understand categorical features.
- Initial data inspection saves significant debugging time later.

---

# What's Next?

In **Part 3**, we will cover:

- Univariate Analysis (Introduction)
- Bivariate Analysis (Introduction)
- Correlation
- Data Distribution
- Common Data Quality Issues
- End-to-End Dataset Inspection Workflow
- Interview Cheat Sheet
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
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

# Day 08 - Understanding Your Data (Part 3)

> **Topics Covered**
>
> - Understanding Data Distribution
> - Correlation (Introduction)
> - Understanding Target Variable
> - End-to-End Dataset Inspection Workflow
> - Retail Sales Forecasting Example
> - Interview Questions
> - Common Mistakes
> - Revision Cheat Sheet

---

# Step 13: Understand Data Distribution

## Definition

After checking the dataset,

we should understand how the values are distributed.

Questions to ask:

- Are most values small?
- Are most values large?
- Are values evenly distributed?
- Are there extreme values?

Understanding the distribution helps in choosing preprocessing techniques and ML algorithms.

---

# Example

Suppose Salary values are

```
25000
27000
28000
30000
32000
35000
400000
```

Notice

Most salaries are between **25k–35k**, but one value is **400k**.

This could be:

- A CEO's salary
- A data entry mistake
- An outlier

---

# Why Does Distribution Matter?

Many Machine Learning algorithms assume that data follows certain patterns.

If the data is highly skewed,

we may need transformations later during preprocessing.

---

# Step 14: Understand the Target Variable

Before training a model,

we must understand the target column.

Questions to ask:

- Is it numerical?
- Is it categorical?
- Is it balanced?
- Does it contain missing values?

---

# Example 1

Target

```
Sales
```

Output

```
150

200

250
```

This is a **Regression** problem.

---

# Example 2

Target

```
Purchased
```

Output

```
Yes

No
```

This is a **Classification** problem.

---

# Retail Sales Forecasting Example

Dataset

| Date | Store | Product | Sales |
|------|--------|----------|------:|

Target

```
Sales
```

Since Sales is numeric,

the problem is

**Regression**.

---

# Step 15: Correlation (Introduction)

## Definition

Correlation measures how strongly two numerical variables are related.

It helps answer questions like:

- Does temperature affect sales?
- Does discount increase demand?
- Does advertising increase revenue?

---

# Example

Suppose

```
Temperature ↑

Ice Cream Sales ↑
```

Both increase together.

Positive Correlation.

---

Suppose

```
Price ↑

Demand ↓
```

One increases,

the other decreases.

Negative Correlation.

---

# Correlation Values

| Correlation | Meaning |
|-------------|---------|
| +1 | Perfect Positive |
| 0 | No Relationship |
| -1 | Perfect Negative |

---

# Python Example

```python
df.corr(numeric_only=True)
```

This generates a correlation matrix for numerical columns.

---

# Why Is Correlation Useful?

Correlation helps us

- Understand feature relationships.
- Detect redundant features.
- Improve feature selection.
- Reduce multicollinearity (later topic).

---

# Step 16: Initial Business Insights

Understanding data is not only for Machine Learning.

It also provides business insights.

Example

Suppose you discover:

- Weekend sales are higher.
- Milk sells more during winter.
- Promotions increase demand.

Even before building a model,

these insights can help business teams make better decisions.

---

# End-to-End Dataset Inspection Workflow

Whenever you receive a new dataset,

follow this sequence.

```
Load Dataset

↓

View First Rows

↓

Check Shape

↓

Check Columns

↓

Check Data Types

↓

Check Missing Values

↓

Check Duplicates

↓

Generate Summary Statistics

↓

Check Unique Values

↓

Check Target Variable

↓

Understand Distribution

↓

Study Correlation

↓

Ready for Data Preprocessing
```

---

# Retail Sales Forecasting Workflow

Suppose your dataset contains

- Date
- Product
- Store
- Temperature
- Promotion
- Holiday
- Sales

Your workflow becomes

```
Load Dataset

↓

Understand Columns

↓

Identify Target

↓

Check Missing Values

↓

Remove Duplicates

↓

Study Sales Distribution

↓

Study Correlation

↓

Feature Engineering

↓

Model Building
```

This is the same approach followed in real-world ML projects.

---

# Complete Pandas Checklist

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df.head()

df.tail()

df.shape

df.columns

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df.nunique()

df["Sales"].value_counts()

df.corr(numeric_only=True)
```

These commands provide a strong initial understanding of most datasets.

---

# Interview Questions

### What is the purpose of Understanding Your Data?

To understand the structure, quality, and characteristics of the dataset before preprocessing and model training.

---

### Why should we inspect the target variable?

Because it determines the Machine Learning problem type and influences model selection.

---

### What is Correlation?

Correlation measures the strength and direction of the relationship between two numerical variables.

---

### What does a correlation of +1 indicate?

A perfect positive relationship.

---

### What does a correlation of 0 indicate?

No linear relationship.

---

### Why is understanding data important before preprocessing?

Because preprocessing decisions depend on the dataset's characteristics.

---

# Common Mistakes

❌ Jumping directly to Feature Engineering.

✅ First understand the dataset completely.

---

❌ Assuming every numerical column is useful.

✅ Check correlation and business relevance.

---

❌ Ignoring the target variable.

✅ Understand the target before selecting algorithms.

---

# Revision Cheat Sheet

```
Understanding Your Data

│

├── Load Dataset
│
├── View Sample Rows
│
├── Check Shape
│
├── Check Columns
│
├── Check Data Types
│
├── Missing Values
│
├── Duplicate Records
│
├── Statistical Summary
│
├── Unique Values
│
├── Target Variable
│
├── Data Distribution
│
├── Correlation
│
└── Ready for Preprocessing
```

---

# Key Takeaways

- Never train a model without understanding the dataset.
- Inspect rows, columns, data types, and missing values.
- Study the target variable before choosing an algorithm.
- Correlation helps understand relationships between numerical features.
- Dataset understanding is the foundation of every successful Machine Learning project.

---

# Final Summary

Understanding Your Data is the first practical step after collecting a dataset.

A Machine Learning engineer spends significant time exploring data before model building.

By understanding the dataset's structure, quality, and relationships, we reduce errors, improve feature engineering, and build more reliable Machine Learning models.

Mastering this step will make every future stage—data preprocessing, feature engineering, model selection, and evaluation—much easier.

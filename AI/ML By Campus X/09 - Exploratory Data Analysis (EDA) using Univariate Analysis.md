# Day 09 - Exploratory Data Analysis (EDA) using Univariate Analysis (Part 1)

> **Course:** CampusX - 100 Days of Machine Learning

---

# 🎯 Learning Objectives

After completing this lecture, you will be able to:

- Understand what Exploratory Data Analysis (EDA) is.
- Understand Univariate Analysis.
- Differentiate between Categorical and Numerical Data.
- Perform Univariate Analysis on Categorical Features.
- Use Pandas and Seaborn for basic data exploration.
- Interpret charts used for categorical variables.

---

# 📚 Prerequisites

Before starting this lecture, you should know:

- Pandas Basics
- Understanding Your Data
- Basic Python

---

# Introduction

After understanding our dataset, the next step is to **explore it in detail**.

Simply knowing

- number of rows,
- columns,
- data types

is **not enough**.

We also want to know:

- Which values occur most frequently?
- Which categories dominate the dataset?
- Are some categories very rare?
- Is the data balanced?

To answer these questions, we perform **Exploratory Data Analysis (EDA).**

---

# What is EDA?

**Exploratory Data Analysis (EDA)** is the process of exploring, summarizing, and visualizing data to understand its characteristics before building a Machine Learning model.

EDA helps us discover:

- Hidden patterns
- Trends
- Missing values
- Outliers
- Data distribution
- Relationships between variables

EDA is usually performed after loading and understanding the dataset.

---

# Why is EDA Important?

Imagine you directly train a model without exploring the data.

Problems like:

- Missing values
- Imbalanced classes
- Outliers
- Incorrect distributions

may remain hidden.

As a result,

your model may perform poorly.

EDA helps us identify these problems before model training.

---

# Types of EDA

EDA can be divided into three categories.

```
EDA

│

├── Univariate Analysis

├── Bivariate Analysis

└── Multivariate Analysis
```

---

# What is Univariate Analysis?

The word

```
Uni

↓

One
```

means

**Univariate Analysis studies only one variable at a time.**

We do not compare one column with another.

Instead,

we completely understand a single feature.

---

# Example

Suppose we have

| Age | Salary | Purchased |
|------|---------|-----------|

If we only study

```
Age
```

then this is

**Univariate Analysis**.

If we compare

```
Age

↓

Salary
```

then it becomes

**Bivariate Analysis**.

---

# Goal of Univariate Analysis

The objective is to answer questions like:

- What values are present?
- Which value occurs most often?
- How are values distributed?
- Are there missing values?
- Are there unusual values?
- Is the feature balanced?

---

# Types of Features

Before performing Univariate Analysis,

we must identify the type of feature.

Features are mainly divided into:

```
Dataset

│

├── Numerical

└── Categorical
```

In this part,

we will focus on **Categorical Features**.

---

# What is a Categorical Feature?

A categorical feature contains **labels or categories** instead of continuous numerical values.

Examples

```
Gender

Male

Female
```

---

```
City

Delhi

Mumbai

Bhopal

Pune
```

---

```
Department

HR

Sales

Finance
```

These values represent **categories**, not quantities.

---

# Retail Example

Suppose we have a retail dataset.

| Store Type |
|------------|
| Supermarket |
| Hypermarket |
| Supermarket |
| Express Store |

Store Type is a **Categorical Feature**.

---

# How Do We Analyze Categorical Features?

The most common methods are:

- Frequency Table
- Value Counts
- Bar Chart
- Count Plot
- Pie Chart (less preferred)

---

# Frequency Table

A frequency table tells us **how many times each category appears**.

Example

| Gender |
|---------|
| Male |
| Female |
| Male |
| Male |
| Female |

Frequency Table

| Category | Count |
|----------|------:|
| Male | 3 |
| Female | 2 |

---

# Using value_counts()

Pandas provides a simple function.

```python
df["Gender"].value_counts()
```

Output

```
Male      650

Female    350
```

---

# Why value_counts() is Important?

It helps answer:

- Which category is most common?
- Which category is rare?
- Is the dataset balanced?

---

# Normalize Frequencies

Instead of counts,

sometimes percentages are more useful.

```python
df["Gender"].value_counts(normalize=True)
```

Example Output

```
Male      0.65

Female    0.35
```

Meaning

- Male → 65%
- Female → 35%

---

# Count Plot

One of the most commonly used visualization techniques for categorical data is the **Count Plot**.

Example

```python
import seaborn as sns

sns.countplot(data=df, x="Gender")
```

---

# What Does Count Plot Show?

Each bar represents

```
Frequency of a Category
```

Taller bar

↓

More observations

Smaller bar

↓

Fewer observations

---

# Example

```
Male

██████████████

Female

███████
```

Immediately,

we can see

Male appears more frequently.

---

# Why Count Plot is Useful?

Instead of reading numbers,

we can understand the dataset visually.

This becomes especially useful when there are many categories.

---

# Bar Plot vs Count Plot

Many beginners confuse these.

## Count Plot

Counts observations automatically.

Example

```python
sns.countplot(data=df, x="Gender")
```

---

## Bar Plot

Requires numerical values.

Example

```python
sns.barplot(data=df,
            x="Department",
            y="Salary")
```

Interview Tip:

Use **Count Plot** for frequencies.

Use **Bar Plot** when you already have numerical values to compare.

---

# Pie Chart

Pie charts also show category proportions.

Example

```python
df["Gender"].value_counts().plot(kind="pie")
```

---

# Should We Always Use Pie Charts?

No.

Pie charts become difficult to read when:

- Categories are many.
- Differences are small.

In most Machine Learning projects,

Count Plot or Bar Plot is preferred.

---

# Retail Example

Product Categories

```
Milk

Bread

Eggs

Butter

Cheese
```

Using

```python
sns.countplot(data=df,
              x="Product")
```

helps identify

- Most sold product
- Least sold product

before model training.

---

# Interview Questions

### What is EDA?

EDA is the process of exploring and understanding data before model building.

---

### What is Univariate Analysis?

Studying one variable at a time.

---

### Why is Univariate Analysis important?

It helps understand the distribution and characteristics of individual features.

---

### Which plot is commonly used for categorical variables?

Count Plot.

---

### What does value_counts() do?

Returns the frequency of each category.

---

### Difference between Count Plot and Bar Plot?

Count Plot automatically counts categories.

Bar Plot requires numerical values.

---

# Common Mistakes

❌ Comparing two variables during Univariate Analysis.

✅ Study only one variable at a time.

---

❌ Using Histogram for categorical data.

✅ Use Count Plot or Bar Chart.

---

❌ Using Pie Charts with many categories.

✅ Prefer Count Plot for better readability.

---

# Key Takeaways

- EDA helps understand data before model building.
- Univariate Analysis studies one feature at a time.
- Categorical features are analyzed using frequencies and visualizations.
- `value_counts()` is the most commonly used Pandas function.
- Count Plot is the preferred visualization for categorical features.

---

# What's Next?

In **Part 2**, we will study **Numerical Features** using:

- Histogram
- KDE Plot
- Distribution
- Mean
- Median
- Mode
- Skewness
- Python Examples
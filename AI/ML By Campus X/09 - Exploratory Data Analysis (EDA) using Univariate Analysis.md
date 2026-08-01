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



# Day 09 - Exploratory Data Analysis (EDA) using Univariate Analysis (Part 2)

> **Topics Covered**
>
> - Numerical Features
> - Descriptive Statistics
> - Histogram
> - KDE Plot
> - Distribution
> - Mean
> - Median
> - Mode
> - Skewness
> - Distribution Shape
> - Python Examples

---

# Numerical Features

## Definition

A Numerical Feature contains quantitative values that can be measured.

Examples

```
Age

Salary

Marks

Height

Weight

Sales

Temperature
```

Unlike categorical features,

numerical features allow mathematical operations such as

- Addition
- Average
- Minimum
- Maximum

---

# Types of Numerical Features

Numerical features are mainly divided into

```
Numerical Data

│

├── Discrete

└── Continuous
```

---

## Discrete Data

Contains countable values.

Examples

```
Number of Students

Number of Cars

Number of Orders

Number of Products Sold
```

Possible values

```
1

2

3

4
```

Decimals usually don't make sense.

---

## Continuous Data

Contains measurable values.

Examples

```
Height

Weight

Temperature

Salary

Sales
```

Possible values

```
45.2

175.6

22.8

1000.75
```

---

# How Do We Analyze Numerical Features?

The most common methods are

- Summary Statistics
- Histogram
- KDE Plot
- Box Plot
- Distribution Analysis

In this part we will focus on

- Summary Statistics
- Histogram
- KDE Plot

---

# Descriptive Statistics

Descriptive Statistics summarize numerical data.

The easiest way is

```python
df.describe()
```

Example Output

| Statistic | Sales |
|-----------|------:|
| Count | 1000 |
| Mean | 245 |
| Std | 32 |
| Min | 120 |
| 25% | 220 |
| 50% | 240 |
| 75% | 265 |
| Max | 380 |

---

# Mean

## Definition

Mean is the average value.

Formula

```
Sum of Values

──────────────

Number of Values
```

Example

```
10

20

30

40

50
```

Mean

```
30
```

Python

```python
df["Sales"].mean()
```

---

# Median

## Definition

Median is the middle value after sorting the data.

Example

```
10

20

30

40

50
```

Median

```
30
```

Python

```python
df["Sales"].median()
```

---

# Mode

## Definition

Mode is the most frequently occurring value.

Example

```
10

20

20

20

40
```

Mode

```
20
```

Python

```python
df["Sales"].mode()
```

---

# Mean vs Median vs Mode

| Measure | Meaning |
|----------|---------|
| Mean | Average |
| Median | Middle Value |
| Mode | Most Frequent Value |

---

# When Should We Use Median?

Suppose salaries are

```
25000

27000

29000

30000

5000000
```

Mean becomes very large because of one extreme salary.

Median still represents the center correctly.

This is why Median is preferred when outliers are present.

---

# Histogram

## Definition

Histogram is the most commonly used plot for numerical features.

It divides data into intervals called **bins**.

Then,

it counts how many observations fall into each interval.

---

# Python Example

```python
import seaborn as sns

sns.histplot(df["Sales"])
```

---

# Why Histogram?

Histogram helps answer

- Is the data normally distributed?
- Is the data skewed?
- Are there gaps?
- Are there multiple peaks?

---

# Example

```
Frequency

│

│      ███

│   ███████

│ ███████████

│██████████████

└────────────────

        Sales
```

The tallest bars indicate where most observations lie.

---

# Number of Bins

Bins divide the data into intervals.

Example

Sales

```
100-150

150-200

200-250

250-300
```

Each interval becomes one bar.

More bins

↓

More detailed histogram.

Fewer bins

↓

Simpler histogram.

---

# KDE Plot

## Definition

KDE stands for

Kernel Density Estimation.

It is a smooth version of a Histogram.

Instead of bars,

it shows a smooth probability curve.

---

# Python Example

```python
sns.kdeplot(df["Sales"])
```

---

# Histogram + KDE

A common practice is

```python
sns.histplot(
    df["Sales"],
    kde=True
)
```

This displays

- Histogram
- KDE Curve

together.

---

# Why Use KDE?

KDE makes it easier to understand

- Distribution Shape
- Peaks
- Spread

without the effect of histogram bins.

---

# Distribution

Distribution tells us

how values are spread.

Questions

- Are values concentrated?
- Are they spread out?
- Is the distribution symmetric?

Understanding distribution is one of the most important goals of EDA.

---

# Symmetric Distribution

Example

```
        █

      ███

    ███████

      ███

        █
```

Left side

≈

Right side

Mean

≈

Median

---

# Skewed Distribution

Sometimes data is not symmetric.

Instead,

one side becomes longer.

This is called

**Skewness**.

---

# Positive Skew

```
███████

████

██

█

──────────────►
```

Long tail on the right.

Usually

```
Mean > Median
```

---

# Negative Skew

```
◄──────────────

█

██

████

███████
```

Long tail on the left.

Usually

```
Mean < Median
```

---

# Why Is Skewness Important?

Many Machine Learning algorithms work better when data is approximately symmetric.

Highly skewed data may require transformation during preprocessing.

---

# Retail Example

Suppose

Most stores sell

```
200–250 units
```

A few stores sell

```
5000 units
```

The sales distribution becomes positively skewed.

---

# Python Example

```python
df["Sales"].skew()
```

Output

```
1.87
```

Positive value

↓

Positive Skew.

---

# Interview Questions

### What is Histogram?

A graphical representation of numerical data using bins.

---

### What is KDE Plot?

A smooth estimate of the data distribution.

---

### Difference between Histogram and KDE?

Histogram uses bars.

KDE uses a smooth curve.

---

### Difference between Mean and Median?

Mean is the average.

Median is the middle value.

---

### Why is Median preferred when outliers exist?

Because Median is less affected by extreme values.

---

### What is Positive Skew?

Distribution with a long right tail.

---

### What is Negative Skew?

Distribution with a long left tail.

---

# Common Mistakes

❌ Using Count Plot for numerical features.

✅ Use Histogram.

---

❌ Assuming Mean always represents the center.

✅ Median is often better when outliers exist.

---

❌ Confusing Histogram with Bar Plot.

Histogram is used for numerical data.

Bar Plot is generally used for categorical summaries.

---

# Key Takeaways

- Numerical features are analyzed differently from categorical features.
- Mean, Median, and Mode summarize the center of the data.
- Histograms help visualize frequency distributions.
- KDE plots provide a smoother view of the distribution.
- Skewness describes the asymmetry of the data.
- Understanding the distribution helps in preprocessing and model selection.

---

# What's Next?

In **Part 3**, we will study

- Box Plot
- Outliers
- Five Number Summary
- IQR
- Percentiles
- Complete Univariate Workflow
- Retail Sales Forecasting Example
- Interview Cheat Sheet


# Day 09 - Exploratory Data Analysis (EDA) using Univariate Analysis (Part 3)

> **Topics Covered**
>
> - Box Plot
> - Outliers
> - Five Number Summary
> - Percentiles
> - IQR (Interquartile Range)
> - Complete Univariate Workflow
> - Retail Sales Forecasting Example
> - Interview Questions
> - Revision Cheat Sheet

---

# Box Plot

## Definition

A **Box Plot** is a graphical representation used to understand the distribution of numerical data and identify outliers.

Unlike a Histogram,

a Box Plot focuses on

- Spread of data
- Center of data
- Outliers

---

# Why Do We Use Box Plot?

A Box Plot helps answer:

- Are there any outliers?
- How spread is the data?
- Where is the median located?
- Is the distribution symmetric?

---

# Python Example

```python
import seaborn as sns

sns.boxplot(x=df["Sales"])
```

---

# Components of a Box Plot

A Box Plot is built using the **Five Number Summary**.

```
Minimum

↓

Q1 (25%)

↓

Median (50%)

↓

Q3 (75%)

↓

Maximum
```

---

# Five Number Summary

The five-number summary gives a quick overview of a numerical feature.

| Statistic | Meaning |
|-----------|---------|
| Minimum | Smallest value |
| Q1 | 25th Percentile |
| Median | 50th Percentile |
| Q3 | 75th Percentile |
| Maximum | Largest value |

---

# Percentiles

A percentile divides the dataset into 100 equal parts.

Examples

### 25th Percentile (Q1)

25% of observations lie below this value.

---

### 50th Percentile

This is the Median.

50% of observations lie below it.

---

### 75th Percentile (Q3)

75% of observations lie below this value.

---

# Example

Sorted Data

```
10

20

30

40

50

60

70

80
```

Approximate Percentiles

```
Q1 → 25

Median → 45

Q3 → 65
```

---

# Interquartile Range (IQR)

## Definition

IQR measures the spread of the middle 50% of the data.

Formula

```
IQR = Q3 - Q1
```

Example

```
Q1 = 20

Q3 = 40
```

```
IQR = 40 - 20 = 20
```

---

# Why is IQR Important?

IQR helps detect **outliers**.

Unlike the Mean,

IQR is not heavily affected by extreme values.

---

# Outliers

## Definition

Outliers are observations that are significantly different from the rest of the data.

Example

```
200

205

210

215

220

5000
```

The value **5000** is an outlier.

---

# Why Do Outliers Matter?

Outliers can

- Distort the Mean
- Affect model training
- Reduce prediction accuracy
- Influence statistical analysis

However, not every outlier is an error.

Sometimes it represents a real business event.

---

# Detecting Outliers Using IQR

A value is considered an outlier if

```
Value < Q1 − 1.5 × IQR
```

or

```
Value > Q3 + 1.5 × IQR
```

---

# Python Example

```python
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
]
```

---

# Retail Sales Forecasting Example

Suppose daily sales are

```
210

220

215

225

218

5000
```

Possible reasons for the outlier:

- Festival season
- Flash sale
- Data entry mistake
- Bulk corporate order

As an ML engineer,

never remove outliers blindly.

Always understand the business reason first.

---

# Box Plot Interpretation

Suppose a Box Plot shows

- Long upper whisker
- Several points above the whisker

This usually indicates

- Positive Skew
- Presence of Outliers

---

# Complete Univariate Analysis Workflow

Whenever you receive a numerical feature,

follow this order.

```
Select Feature

↓

Check Data Type

↓

Summary Statistics

↓

Mean

↓

Median

↓

Mode

↓

Histogram

↓

KDE Plot

↓

Box Plot

↓

Check Outliers

↓

Understand Distribution

↓

Ready for Feature Engineering
```

---

# Retail Example Workflow

Feature

```
Sales
```

Steps

```
Check Missing Values

↓

Describe()

↓

Mean

↓

Median

↓

Histogram

↓

Box Plot

↓

Outlier Detection

↓

Decision

↓

Model Training
```

---

# Which Plot Should I Use?

| Feature Type | Preferred Plot |
|--------------|----------------|
| Categorical | Count Plot |
| Numerical Distribution | Histogram |
| Numerical Density | KDE Plot |
| Outliers | Box Plot |

---

# Interview Questions

### What is Univariate Analysis?

Studying one feature at a time.

---

### Which plot is best for detecting outliers?

Box Plot.

---

### What is IQR?

The difference between Q3 and Q1.

---

### Formula of IQR?

```
IQR = Q3 - Q1
```

---

### Why is IQR preferred over Mean for outlier detection?

Because IQR is less affected by extreme values.

---

### What is the Five Number Summary?

- Minimum
- Q1
- Median
- Q3
- Maximum

---

### Can every outlier be removed?

No.

Some outliers represent real-world events and contain valuable information.

---

### Which plot shows the distribution of numerical data?

Histogram.

---

### Which plot shows both distribution and outliers?

Box Plot.

---

# Common Mistakes

❌ Removing every outlier automatically.

✅ First understand whether it is a business event or a data error.

---

❌ Using Box Plot for categorical data.

✅ Use Box Plot only for numerical features.

---

❌ Assuming Mean is always reliable.

✅ Outliers can significantly affect the Mean.

---

❌ Ignoring skewness while interpreting a Box Plot.

✅ Skewness often explains why outliers appear.

---

# Revision Cheat Sheet

```
EDA

│

└── Univariate Analysis

        │

        ├── Categorical

        │      ├── value_counts()

        │      ├── Count Plot

        │      └── Pie Chart

        │

        └── Numerical

               ├── Mean

               ├── Median

               ├── Mode

               ├── Histogram

               ├── KDE Plot

               ├── Box Plot

               ├── Percentiles

               ├── IQR

               └── Outlier Detection
```

---

# Key Takeaways

- Univariate Analysis studies one feature at a time.
- Categorical features are analyzed using frequency tables and Count Plots.
- Numerical features are analyzed using summary statistics and visualizations.
- Histograms help understand distributions.
- KDE plots provide a smoother view of the distribution.
- Box Plots help identify outliers.
- IQR is a robust method for outlier detection.
- Always interpret outliers using business context before removing them.

---

# Final Summary

Univariate Analysis is the first step of Exploratory Data Analysis (EDA). It helps us understand the characteristics of individual features before applying preprocessing or Machine Learning algorithms.

By analyzing categorical and numerical features separately, identifying distributions, detecting outliers, and understanding statistical summaries, we build a strong foundation for feature engineering and model development.
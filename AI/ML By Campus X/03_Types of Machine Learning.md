# Day 3 - Types of Machine Learning

## 🎯 Learning Objective

After completing this lecture, you should be able to:

* Understand the three major types of Machine Learning.
* Differentiate between Supervised, Unsupervised and Reinforcement Learning.
* Understand the types of Supervised Learning.
* Understand the types of Unsupervised Learning.
* Identify which ML technique should be used for a given problem.
* Answer common interview questions confidently.

---

# What is Machine Learning?

Machine Learning is the process of learning patterns from historical data so that a machine can make predictions or decisions without being explicitly programmed.

Depending on the type of data available, Machine Learning is mainly divided into three categories.

```
Machine Learning
│
├── Supervised Learning
├── Unsupervised Learning
└── Reinforcement Learning
```

---

# 1. Supervised Learning

## Definition

Supervised Learning is a learning technique where both **input features (X)** and the **correct output (Y)** are available.

The model learns the relationship between input and output.

```
Input (Features)
        │
        ▼
Machine Learning Model
        │
        ▼
Correct Output (Target)
```

Think of it like a teacher teaching students using questions **and** correct answers.

---

## Example

Predict student marks.

| Hours Studied | Marks |
| ------------- | ----: |
| 2             |    40 |
| 4             |    65 |
| 6             |    85 |

The model learns

```
Hours Studied
        ↓
Marks
```

Now if a student studies **5 hours**, the model predicts approximately **75 marks**.

---

## Real World Examples

* House Price Prediction
* Salary Prediction
* Sales Forecasting
* Disease Prediction
* Spam Detection
* Loan Approval

---

# Types of Supervised Learning

Supervised Learning is divided into two categories.

```
Supervised Learning
│
├── Regression
└── Classification
```

---

# Regression

## Definition

Regression is used when the output is a **continuous numerical value**.

### Easy Trick

**Predict "How Much?"**

Examples

* House Price
* Salary
* Temperature
* Future Sales
* Electricity Consumption

Example

```
House Features

↓

₹75 Lakhs
```

Output is numeric.

### Popular Algorithms

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

---

# Classification

## Definition

Classification is used when the output belongs to predefined categories.

### Easy Trick

**Predict "Which Class?"**

Examples

* Spam / Not Spam
* Fraud / Genuine
* Diabetes / No Diabetes
* Pass / Fail

Example

```
Email

↓

Spam
```

Output is a category.

### Popular Algorithms

* Logistic Regression
* Decision Tree
* Random Forest
* SVM
* Naive Bayes
* KNN

---

# Regression vs Classification

| Regression        | Classification          |
| ----------------- | ----------------------- |
| Predicts numbers  | Predicts categories     |
| Continuous output | Discrete output         |
| Example: Sales    | Example: Spam Detection |

---

# Retail Sales Forecasting Example

Features

* Store
* Product
* Month
* Holiday
* Discount
* Previous Sales

Target

```
Next Month Sales
```

Since the target is a numerical value, this is a **Supervised Regression** problem.

---

# 2. Unsupervised Learning

## Definition

In Unsupervised Learning, only input data is available.

There is **no target/output column**.

The machine tries to discover hidden patterns or relationships automatically.

```
Features

↓

Machine

↓

Hidden Patterns
```

Think of giving a teacher a class of students without any labels and asking them to group similar students.

---

# Types of Unsupervised Learning

CampusX introduces three major categories.

```
Unsupervised Learning
│
├── Clustering
├── Association
└── Dimensionality Reduction
```

---

# A. Clustering

## Definition

Clustering groups similar data points together.

The machine itself decides which observations belong to the same group.

Example

Customer Data

↓

```
Premium Customers

Budget Customers

Regular Customers
```

No labels are given.

### Applications

* Customer Segmentation
* Image Segmentation
* News Clustering
* Document Clustering

### Popular Algorithms

* K-Means
* DBSCAN
* Hierarchical Clustering

---

## Retail Example

Suppose a supermarket has one million customers.

The company doesn't know who is

* Premium
* Regular
* Budget

The ML algorithm automatically creates these groups.

---

# B. Association Rule Learning

## Definition

Association finds relationships between items that frequently occur together.

It answers:

**"If one item is bought, what else is likely to be bought?"**

Example

```
Bread

↓

Butter

↓

Jam
```

Machine discovers the rule

```
Bread

⇒

Butter
```

Applications

* Amazon Recommendations
* Flipkart Recommendations
* Grocery Basket Analysis
* Cross Selling

### Popular Algorithms

* Apriori
* FP-Growth

---

# C. Dimensionality Reduction

## Definition

Sometimes datasets contain hundreds or thousands of features.

Many of them carry duplicate or unnecessary information.

Dimensionality Reduction reduces the number of features while preserving most of the useful information.

Example

```
100 Features

↓

20 Important Features
```

Benefits

* Faster training
* Less storage
* Better visualization
* Reduces noise
* Can reduce overfitting

### Popular Algorithms

* PCA (Principal Component Analysis)
* t-SNE
* UMAP

---

## Retail Example

Suppose a retail dataset has 150 features.

Instead of training on all 150 columns,

PCA may reduce them to 30 important features, making the model faster and easier to train.

---

# 3. Reinforcement Learning

## Definition

Reinforcement Learning is a learning technique where an **Agent** learns by interacting with an **Environment**.

The agent receives

* Reward
* Penalty

and improves its decisions over time.

```
Agent

↓

Action

↓

Environment

↓

Reward / Penalty

↓

Learning
```

Think of teaching a dog.

Correct trick → Reward

Wrong trick → No reward

The dog gradually learns.

---

## Applications

* Self Driving Cars
* Chess
* Robotics
* Game Playing
* Recommendation Optimization

---

# Complete Comparison

| Feature          | Supervised  | Unsupervised          | Reinforcement     |
| ---------------- | ----------- | --------------------- | ----------------- |
| Labels Available | ✅ Yes       | ❌ No                  | Reward Signal     |
| Goal             | Prediction  | Discover Patterns     | Learn Best Action |
| Output           | Known       | Unknown               | Policy            |
| Example          | House Price | Customer Segmentation | Self Driving      |

---

# How to Identify the Problem?

### Question 1

Do you have the target/output column?

Yes → Supervised Learning

No → Go to Question 2

---

### Question 2

Do you want to find hidden groups or relationships?

Yes → Unsupervised Learning

---

### Question 3

Does the system learn through rewards and penalties?

Yes → Reinforcement Learning

---

# Interview Questions

### What is Supervised Learning?

A learning technique where both input features and correct output labels are available during training.

---

### What are the two types of Supervised Learning?

* Regression
* Classification

---

### What is Regression?

Regression predicts continuous numerical values.

---

### What is Classification?

Classification predicts categorical outputs.

---

### What is Unsupervised Learning?

A learning technique where the dataset has no target variable and the model discovers hidden patterns automatically.

---

### What are the types of Unsupervised Learning?

* Clustering
* Association Rule Learning
* Dimensionality Reduction

---

### What is Reinforcement Learning?

A learning approach where an agent learns by interacting with the environment using rewards and penalties.

---

### Is Sales Forecasting Regression or Classification?

Regression because the output is numerical.

---

### Is Customer Segmentation Supervised?

No.

It is an Unsupervised Learning problem because there are no labels.

---

# Common Interview Traps

❌ Spam Detection → Regression

✅ Classification

---

❌ House Price Prediction → Classification

✅ Regression

---

❌ Customer Segmentation → Supervised

✅ Unsupervised

---

❌ Market Basket Analysis → Clustering

✅ Association Rule Learning

---

# Key Takeaways

* Machine Learning has three major categories.
* Supervised Learning requires labeled data.
* Regression predicts numbers.
* Classification predicts categories.
* Unsupervised Learning has three important types:

  * Clustering
  * Association
  * Dimensionality Reduction
* Reinforcement Learning learns using rewards and penalties.

---

# 30-Second Revision

```
Machine Learning
│
├── Supervised
│   ├── Regression → Numbers
│   └── Classification → Categories
│
├── Unsupervised
│   ├── Clustering
│   ├── Association
│   └── Dimensionality Reduction
│
└── Reinforcement Learning
    └── Reward & Penalty
```

---

# Next Lecture

**Day 4 – Machine Learning Development Life Cycle (End-to-End ML Pipeline)**

We will learn how an ML project moves from raw data to a deployed model, which is one of the most frequently asked interview topics.

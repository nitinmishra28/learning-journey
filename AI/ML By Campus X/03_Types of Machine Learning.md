# Day 3 - Types of Machine Learning (Part 1)

> "Not every Machine Learning problem is solved in the same way."
> The type of data decides the type of Machine Learning.

---

# 🎯 Learning Objectives

After completing this lecture, you should be able to:

- Explain why Machine Learning is divided into different types.
- Understand Supervised Learning in detail.
- Differentiate Regression and Classification.
- Identify whether a real-world problem is Regression or Classification.
- Answer interview questions based on Supervised Learning.

---

# Prerequisites

Before starting this lecture you should know

- What is AI?
- What is Machine Learning?
- Difference between AI, ML and DL

---

# Why Do We Need Different Types of Machine Learning?

Suppose you are a teacher.

Sometimes students come with:

- Questions + Answers

Sometimes they come with:

- Only Questions

Sometimes they learn by making mistakes.

Will you teach everyone in the same way?

No.

Exactly the same thing happens in Machine Learning.

Every dataset is different.

Therefore every learning approach is different.

---

# Simple Analogy

Imagine you want to teach a child.

### Case 1

You show

Apple

and tell him

"This is Apple."

You repeat many examples.

Now the child learns.

This is

✅ Supervised Learning

---

### Case 2

You simply give him

Apple

Banana

Orange

Mango

without telling names.

After some time

he starts grouping similar fruits.

This is

✅ Unsupervised Learning

---

### Case 3

You teach using

small number of labeled fruits

and many unlabeled fruits.

This becomes

✅ Semi-Supervised Learning

---

### Case 4

You teach a child to ride a bicycle.

Correct balance

↓

Praise

Wrong balance

↓

Falls

↓

Learns

This is

✅ Reinforcement Learning

---

# Machine Learning Paradigms

Machine Learning is mainly divided into four learning paradigms.

```
Machine Learning

│

├── Supervised Learning

├── Unsupervised Learning

├── Semi-Supervised Learning

└── Reinforcement Learning
```

---

# How to Remember?

| Type | Learns From |
|------|-------------|
| Supervised | Labeled Data |
| Unsupervised | Unlabeled Data |
| Semi-Supervised | Few Labels + Many Unlabeled Samples |
| Reinforcement | Rewards & Penalties |

---

# Interview Definition

## What is Machine Learning?

Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from historical data and make predictions or decisions without being explicitly programmed.

---

# What is Supervised Learning?

## Definition

Supervised Learning is a Machine Learning technique in which the training dataset contains both

- Input Features (X)

and

- Correct Output (Y)

The model learns the mapping

```
X

↓

Model

↓

Y
```

Later,

for a new X,

it predicts Y.

---

# Why is it called "Supervised"?

Because the model is learning under the supervision of correct answers.

Think of a school exam.

Teacher gives

Question

+

Correct Answer

Student learns.

Exactly the same happens here.

---

# Mathematical View

Training Data

```
(X₁,Y₁)

(X₂,Y₂)

(X₃,Y₃)

...

(Xₙ,Yₙ)
```

Goal

Learn a function

```
f(X)=Y
```

Once learned,

predict

```
f(New X)=?
```

---

# Real World Examples

- House Price Prediction
- Sales Forecasting
- Weather Prediction
- Disease Prediction
- Loan Approval
- Credit Risk
- Employee Attrition
- Customer Churn
- Spam Detection
- Face Mask Detection

---

# Retail Sales Forecasting Example

Suppose we have

| Store | Product | Month | Discount | Sales |
|-------|---------|--------|----------|------|
| A | TV | Jan | 10% | 120 |
| A | TV | Feb | 5% | 105 |
| B | AC | Jan | 15% | 60 |

Features

- Store
- Product
- Month
- Discount

Target

Sales

Since the correct output is already available,

this is

✅ Supervised Learning.

---

# Types of Supervised Learning

There are only two major categories.

```
Supervised Learning

│

├── Regression

└── Classification
```

---

# Regression

## Definition

Regression predicts

continuous numerical values.

Simple question:

**How much?**

Examples

- ₹25,000
- 45°C
- 123 Sales
- ₹15 Lakhs

These are numbers.

Hence,

Regression.

---

# Everyday Examples

Predict

- House Price
- Petrol Consumption
- Salary
- Rainfall
- Electricity Usage
- Sales
- Gold Price

---

# Retail Example

Question

How many units of Milk will be sold next Sunday?

Output

```
215 Units
```

Since output is a number,

this is Regression.

---

# Popular Regression Algorithms

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

> **Interview Tip:** Linear Regression is usually the first baseline model in regression problems.

---

# Classification

## Definition

Classification predicts categories.

Question

**Which class?**

Examples

Spam

Not Spam

Fraud

Not Fraud

Diabetes

No Diabetes

Customer Will Churn

Customer Will Not Churn

---

# Retail Example

Predict

Will customer buy again?

Possible outputs

```
Yes

No
```

Since output belongs to predefined classes,

this is Classification.

---

# Types of Classification

### Binary Classification

Only two classes.

Examples

- Spam / Not Spam
- Yes / No
- Fraud / Genuine

---

### Multi-Class Classification

More than two classes.

Example

Animal Image

↓

Cat

Dog

Horse

Cow

---

### Multi-Label Classification

One sample can belong to multiple classes.

Example

Movie Genres

↓

Comedy

Action

Drama

All can be true together.

---

# Popular Classification Algorithms

- Logistic Regression
- KNN
- Decision Tree
- Random Forest
- SVM
- Naive Bayes
- XGBoost Classifier
- LightGBM Classifier

---

# Regression vs Classification

| Regression | Classification |
|------------|----------------|
| Predicts Numbers | Predicts Categories |
| Continuous Output | Discrete Output |
| Example: Salary | Example: Spam Detection |
| Example: Sales | Example: Fraud Detection |

---

# Memory Trick

Regression

↓

"How Much?"

Classification

↓

"Which Class?"

Remember this.

90% interview confusion ends here.

---

# Common Mistakes

❌ House Price → Classification

✅ Regression

---

❌ Spam Detection → Regression

✅ Classification

---

❌ Sales Forecasting → Classification

✅ Regression

---

# Interview Questions

### Q1. What is Supervised Learning?

A learning technique where both input features and target labels are available during training.

---

### Q2. Why is it called Supervised Learning?

Because the model learns using correct answers already present in the dataset.

---

### Q3. What are the types of Supervised Learning?

- Regression
- Classification

---

### Q4. Difference between Regression and Classification?

Regression predicts continuous numerical values, whereas Classification predicts categorical outputs.

---

### Q5. Is Retail Sales Forecasting Regression or Classification?

Regression, because future sales are numerical.

---

# Key Takeaways

- Supervised Learning requires labeled data.
- It is divided into Regression and Classification.
- Regression predicts numbers.
- Classification predicts categories.
- Choosing the correct problem type is the first step in building an ML model.

---

# What's Coming in Part 2?

We will cover:

- Unsupervised Learning
- Clustering
- Association Rule Learning
- Beer & Diapers Case Study
- Dimensionality Reduction
- PCA
- t-SNE
- MNIST Visualization
- Anomaly Detection
- Python Examples
- Interview Questions
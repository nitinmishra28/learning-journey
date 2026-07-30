# Day 05 - Instance-Based Learning vs Model-Based Learning (Part 1)

> **Course:** CampusX - 100 Days of Machine Learning

---

# 🎯 Learning Objectives

After completing this lecture, you will be able to:

- Understand what "learning" actually means in Machine Learning.
- Differentiate Instance-Based and Model-Based Learning.
- Understand Lazy Learning.
- Learn why KNN is an Instance-Based algorithm.
- Decide when Instance-Based Learning should be used.

---

# 📚 Prerequisites

Before starting this lecture, you should know:

- Supervised Learning
- Batch vs Online Learning
- Basic idea of Machine Learning

---

# Introduction

When we say

> "A Machine Learning model learns from data"

one important question arises.

**How does it actually learn?**

There are mainly two approaches.

```
Machine Learning

│

├── Instance-Based Learning

└── Model-Based Learning
```

Almost every ML algorithm belongs to one of these two categories.

Understanding this distinction is very important because it tells us **how a model stores knowledge** and **how it makes predictions**.

---

# What Does "Learning" Mean?

Suppose you are preparing for an exam.

There are two possible strategies.

### Strategy 1

Memorize every solved question.

Whenever a similar question comes,

find the most similar answer.

↓

Instance-Based Learning

---

### Strategy 2

Understand the concepts.

Learn formulas.

Solve completely new questions using the concepts.

↓

Model-Based Learning

This simple analogy explains the difference.

---

# Instance-Based Learning

## Definition

Instance-Based Learning is a learning approach where the algorithm **stores the training examples** instead of building a mathematical model.

Whenever a new data point arrives,

it compares the new point with previously stored examples

and predicts using the most similar ones.

---

# Why is it called Instance-Based?

Because it remembers individual **instances (examples)** from the training data.

Instead of learning equations,

it remembers data.

---

# How Instance-Based Learning Works

```
Training Data

↓

Store Every Example

↓

New Data Arrives

↓

Compare with Stored Examples

↓

Find Most Similar Data

↓

Prediction
```

Notice something interesting.

There is **almost no learning during training**.

Most of the work happens during prediction.

---

# Everyday Analogy

Imagine your teacher gives you

100 solved mathematics questions.

Instead of understanding the formulas,

you memorize all 100 solutions.

During the exam,

you search for the question that looks most similar.

This is Instance-Based Learning.

---

# Why is it called Lazy Learning?

Instance-Based Learning is also known as **Lazy Learning**.

Reason:

The algorithm postpones the learning process until prediction time.

Instead of learning during training,

it waits until a query arrives.

---

# Training Phase

```
Training Data

↓

Store Data

↓

Done
```

Training is extremely fast because almost nothing is computed.

---

# Prediction Phase

```
New Customer

↓

Compare with All Customers

↓

Find Similar Customers

↓

Predict
```

Prediction is slower because comparisons happen at runtime.

---

# Characteristics

- Stores training data.
- No mathematical model is created.
- Fast training.
- Slow prediction.
- Memory intensive.

---

# K-Nearest Neighbors (KNN)

The most famous Instance-Based Learning algorithm is

**K-Nearest Neighbors (KNN).**

Instead of creating a formula,

KNN stores every training example.

When a new point arrives,

it finds the **K nearest neighbors**.

Then,

it predicts using those neighbors.

---

# Example

Suppose we have customer ages.

```
20

22

23

25

45

46

47
```

A new customer has age

```
24
```

The algorithm checks

Which existing customers are closest?

Those nearby examples influence the prediction.

---

# Retail Example

Suppose we want to predict whether a customer will purchase a product.

Instead of creating a mathematical equation,

we search for customers with

- Similar age
- Similar income
- Similar shopping behavior

Then,

we use their outcomes to predict the new customer.

---

# Real World Applications

- Recommendation Systems
- Face Recognition
- Pattern Matching
- Image Classification
- Similar Product Search
- Document Retrieval

---

# Advantages

✅ Very simple

✅ Easy to understand

✅ No complex training

✅ Can adapt immediately when new data is added

---

# Disadvantages

❌ High memory usage

❌ Slow prediction

❌ Doesn't scale well to huge datasets

❌ Sensitive to irrelevant features

---

# Python Example

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

Although we call `fit()`,

KNN mainly stores the training data.

It does **not** learn a mathematical equation like Linear Regression.

---

# Interview Questions

### What is Instance-Based Learning?

A learning approach where the algorithm stores training examples and predicts by comparing new examples with stored ones.

---

### Why is KNN called Lazy Learning?

Because it delays learning until prediction time.

---

### Why is KNN called Instance-Based?

Because it stores individual training instances rather than creating a mathematical model.

---

### Is KNN training fast?

Yes.

Training mainly involves storing the dataset.

---

### Is prediction fast?

No.

Prediction requires comparing the new sample with many stored examples.

---

# Common Interview Traps

❌ KNN learns an equation.

✅ KNN stores training instances.

---

❌ KNN training is expensive.

✅ Training is cheap.

Prediction is expensive.

---

# Key Takeaways

- Instance-Based Learning remembers data instead of equations.
- KNN is the most common Instance-Based algorithm.
- Training is fast.
- Prediction is slow.
- It is also called Lazy Learning.

---

# Next Part

In Part 2 we will cover:

- Model-Based Learning
- Eager Learning
- Linear Regression
- Logistic Regression
- Decision Trees
- Training vs Prediction
- Instance vs Model comparison


# Day 05 - Instance-Based Learning vs Model-Based Learning (Part 2)

> **Topics Covered**
>
> - Model-Based Learning
> - Eager Learning
> - Training Process
> - Mathematical Models
> - Linear Regression
> - Logistic Regression
> - Decision Trees
> - Advantages & Disadvantages
> - Python Examples
> - Interview Questions

---

# Model-Based Learning

## Definition

Model-Based Learning is a Machine Learning approach where the algorithm **learns a mathematical model** from the training data.

Instead of storing every training example,

the algorithm finds the underlying relationship or pattern in the data.

After training,

only the learned model is used for prediction.

---

# Why is it called Model-Based?

Because the algorithm builds a **model** that represents the knowledge learned from the data.

Instead of remembering every training sample,

it remembers only the learned parameters.

---

# How Model-Based Learning Works

```
Training Data

↓

Choose Algorithm

↓

Learn Pattern

↓

Build Mathematical Model

↓

Discard Raw Data (optional)

↓

Prediction
```

Unlike Instance-Based Learning,

most of the computation happens **during training**.

---

# Everyday Analogy

Imagine preparing for an exam.

Instead of memorizing 500 solved questions,

you understand

- Concepts
- Formulas
- Rules

During the exam,

you solve completely new questions using those concepts.

This is Model-Based Learning.

---

# Why is it called Eager Learning?

Model-Based Learning is also called **Eager Learning**.

Reason:

The algorithm learns everything during the training phase.

When prediction time comes,

it simply uses the already learned model.

---

# Training Phase

```
Training Data

↓

Learn Relationship

↓

Create Model

↓

Training Complete
```

Training usually takes longer than Instance-Based Learning because the model is learning patterns.

---

# Prediction Phase

```
New Data

↓

Use Learned Model

↓

Prediction
```

Prediction is fast because the model already knows the relationship.

---

# Characteristics

- Learns mathematical relationships.
- Creates a predictive model.
- Slow training.
- Fast prediction.
- Lower memory usage after training.
- Suitable for large-scale applications.

---

# Example 1: Linear Regression

Suppose we want to predict house prices.

Training Data:

| House Size (sq.ft.) | Price (₹ Lakhs) |
|---------------------|-----------------|
| 800 | 40 |
| 1000 | 52 |
| 1200 | 63 |
| 1500 | 80 |

The algorithm does **not** store every house.

Instead, it learns a line like:

```
Price = m × Size + c
```

This equation becomes the model.

When a new house arrives,

the equation is used to predict its price.

---

# Example 2: Logistic Regression

Goal:

Predict whether an email is Spam or Not Spam.

The model learns the relationship between input features and the probability of spam.

Instead of memorizing all emails,

it learns weights that help classify future emails.

---

# Example 3: Decision Tree

A Decision Tree learns a set of decision rules.

Example:

```
Income > ₹50,000 ?

        │

      Yes

        │

Credit Score > 700 ?

        │

      Yes

        │

Approve Loan
```

The tree itself becomes the model.

---

# Retail Forecasting Example

Suppose a supermarket wants to predict tomorrow's sales.

Features:

- Store ID
- Product Category
- Holiday
- Promotion
- Temperature
- Day of Week

The algorithm learns how these features influence sales.

It does **not** remember every historical sales record.

Instead, it creates a predictive model.

---

# Popular Model-Based Algorithms

### Regression Algorithms

- Linear Regression
- Ridge Regression
- Lasso Regression

---

### Classification Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes
- Support Vector Machine
- XGBoost
- LightGBM

---

### Neural Networks

- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- Transformers

All of these are Model-Based Learning algorithms because they learn parameters during training.

---

# Advantages

✅ Fast predictions

✅ Lower memory usage

✅ Better scalability

✅ Suitable for production systems

✅ Captures underlying relationships

---

# Disadvantages

❌ Training can be expensive

❌ May underfit if the model is too simple

❌ May overfit if the model is too complex

❌ Choosing the right model requires experience

---

# Python Example: Linear Regression

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

Here,

`fit()` learns the parameters (coefficients and intercept).

The model is then used for prediction.

---

# Python Example: Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

The algorithm learns decision boundaries instead of storing all samples.

---

# Python Example: Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

The learned tree becomes the model.

---

# Training vs Prediction

| Stage | Instance-Based | Model-Based |
|--------|----------------|-------------|
| Training | Store Data | Learn Model |
| Prediction | Compare with Stored Data | Use Learned Model |

---

# Memory Usage

### Instance-Based

```
Store Entire Dataset

↓

High Memory
```

### Model-Based

```
Store Only Parameters

↓

Low Memory
```

---

# Speed Comparison

### Training

- Instance-Based → Fast
- Model-Based → Slower

### Prediction

- Instance-Based → Slower
- Model-Based → Fast

---

# Real World Applications

- House Price Prediction
- Sales Forecasting
- Disease Prediction
- Loan Approval
- Weather Forecasting
- Customer Churn Prediction
- Demand Forecasting
- Credit Risk Analysis

---

# Interview Questions

### What is Model-Based Learning?

A learning approach where the algorithm builds a mathematical model from the training data.

---

### Why is it called Eager Learning?

Because the algorithm performs learning during the training phase.

---

### Give examples of Model-Based algorithms.

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest
- Neural Networks

---

### Why are Neural Networks Model-Based?

Because they learn weights and biases that represent the knowledge extracted from the data.

---

### Which is faster during prediction: KNN or Linear Regression?

Linear Regression.

KNN must search through stored data, while Linear Regression directly uses its learned equation.

---

# Common Interview Traps

❌ Linear Regression stores all training examples.

✅ It stores only learned coefficients.

---

❌ Decision Trees are Instance-Based.

✅ Decision Trees are Model-Based.

---

❌ Neural Networks memorize data.

✅ Neural Networks learn parameters (weights and biases).

---

# Key Takeaways

- Model-Based Learning creates a mathematical model.
- Most computation happens during training.
- Prediction is generally fast.
- Linear Regression, Logistic Regression, Decision Trees, and Neural Networks are Model-Based algorithms.
- Model-Based Learning is also known as Eager Learning.

---

# What's Next?

In Part 3 we will cover:

- Instance-Based vs Model-Based Comparison
- Lazy vs Eager Learning
- Parametric vs Non-Parametric Models
- KNN vs Linear Regression
- Retail Forecasting Mapping
- Industry Use Cases
- Revision Cheat Sheet
- Advanced Interview Questions
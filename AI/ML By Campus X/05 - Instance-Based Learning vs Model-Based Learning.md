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
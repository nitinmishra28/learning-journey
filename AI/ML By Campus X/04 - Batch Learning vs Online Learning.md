# Day 04 - Batch Learning vs Online Learning

> **Course:** CampusX - 100 Days of Machine Learning
>
> **Topics Covered**
>
> - Batch Learning
> - Online Learning
> - Incremental Learning
> - Out-of-Core Learning
> - Learning Rate
> - Batch vs Online Learning
> - Python Examples
> - Retail Sales Forecasting Example
> - Interview Questions

---

# 🎯 Learning Objectives

After completing this lecture you should be able to

- Understand Batch Learning.
- Understand Online Learning.
- Know when to use each approach.
- Explain Incremental Learning.
- Explain Out-of-Core Learning.
- Decide whether a real-world problem requires Batch or Online Learning.

---

# 📚 Prerequisites

Before starting this lecture you should know

- What is Machine Learning?
- Types of Machine Learning
- Supervised Learning basics

---

# Why Do We Need Different Learning Strategies?

Imagine you have trained a Machine Learning model.

Now tomorrow you receive

10 new records.

Should you train the entire model again?

Maybe.

Now imagine instead you receive

10 million new records every day.

Can you retrain the model from scratch every minute?

No.

That is why different learning strategies exist.

Some models learn once.

Some models learn continuously.

---

# Everyday Analogy

Imagine preparing for an exam.

### Student A

Studies the complete syllabus.

Gives the exam.

Never studies again until next semester.

↓

Batch Learning

---

### Student B

Studies every day.

Learns new concepts daily.

Improves continuously.

↓

Online Learning

---

# Machine Learning Training Strategies

```
Machine Learning

│

├── Batch Learning

└── Online Learning
```

---

# What is Batch Learning?

## Definition

Batch Learning is a Machine Learning approach where the model is trained using the **entire dataset at once**.

Once training is complete,

the model is deployed.

If new data arrives,

the model **does not learn automatically**.

Instead,

the entire model is trained again.

---

# Batch Learning Workflow

```
Historical Data

↓

Train Model

↓

Deploy Model

↓

Prediction

↓

New Data Arrives

↓

Retrain Entire Model

↓

Deploy Updated Model
```

---

# Why is it called Batch Learning?

Because the complete dataset is given as one **batch** during training.

The model learns everything at once.

---

# Example

Suppose we have sales data from

2021

2022

2023

We train one model using all three years.

The model predicts

2024 sales.

Now after six months,

new sales data becomes available.

Instead of updating the model,

we retrain it using

2021

2022

2023

2024

This is Batch Learning.

---

# Real World Examples

- House Price Prediction
- Salary Prediction
- Monthly Sales Forecasting
- Customer Churn Prediction
- Loan Approval
- Disease Prediction

---

# Retail Forecasting Example

Suppose a supermarket trains a model every month.

Training Data

```
January

February

March

April
```

Model predicts

```
May Sales
```

After May ends,

June training starts using all available data again.

This is Batch Learning.

---

# Advantages of Batch Learning

✅ Simple to implement

✅ Stable model

✅ Usually higher accuracy on static datasets

✅ Easy to reproduce experiments

✅ Easy debugging

---

# Disadvantages

❌ Retraining takes time

❌ Requires more memory

❌ Doesn't adapt immediately

❌ Expensive for continuously changing data

---

# When Should We Use Batch Learning?

Use Batch Learning when

- Data changes slowly.
- Retraining cost is acceptable.
- Historical data is available.
- Real-time updates are not required.

---

# Python Example

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

The `fit()` function trains the model using the complete training dataset.

---

# What is Online Learning?

## Definition

Online Learning is a Machine Learning approach where the model learns **incrementally** from new data.

Instead of retraining from scratch,

the existing model is updated.

---

# Online Learning Workflow

```
Initial Model

↓

Receive New Data

↓

Update Model

↓

Better Model

↓

Receive More Data

↓

Update Again
```

---

# Why is it called Online Learning?

The word "Online" **does not mean Internet**.

It means

the model keeps learning while data keeps arriving.

---

# Everyday Example

Imagine learning English.

Instead of reading one big book once,

you learn

5 new words every day.

Your knowledge improves continuously.

This is Online Learning.

---

# Real World Examples

- Stock Market Prediction
- Fraud Detection
- Recommendation Systems
- Self Driving Cars
- Spam Detection
- Dynamic Pricing

---

# Retail Forecasting Example

Suppose an online shopping website receives

5,000 orders every hour.

Instead of training once every month,

the model updates itself every hour.

Prediction becomes more accurate.

This is Online Learning.

---

# Advantages

✅ Learns continuously

✅ Handles streaming data

✅ Fast updates

✅ Low memory requirement

✅ Suitable for Big Data

---

# Disadvantages

❌ Sensitive to noisy data

❌ Can forget old patterns

❌ Requires monitoring

❌ More difficult to debug

---

# Incremental Learning

Incremental Learning means

the model improves step by step.

Instead of rebuilding everything,

it updates only using new data.

This is the core idea behind Online Learning.

---

# Python Example

```python
from sklearn.linear_model import SGDClassifier

model = SGDClassifier()

model.partial_fit(
    X_batch,
    y_batch,
    classes=[0,1]
)
```

Unlike `fit()`,

`partial_fit()` updates the existing model.

---

# What is Out-of-Core Learning?

Sometimes the dataset is so large

that it cannot fit into RAM.

Example

100 GB dataset

RAM

16 GB

Impossible to load everything.

Solution

Split data into smaller chunks.

Train chunk by chunk.

---

# Workflow

```
Huge Dataset

↓

Chunk 1

↓

Train

↓

Chunk 2

↓

Update

↓

Chunk 3

↓

Update

↓

Final Model
```

Out-of-Core Learning is often implemented using Online Learning algorithms.

---

# Learning Rate

While updating a model,

we must decide

**How much should the model learn from new data?**

This is controlled by the **Learning Rate**.

---

## High Learning Rate

Model changes too quickly.

May become unstable.

---

## Low Learning Rate

Model learns very slowly.

Training takes longer.

---

## Good Learning Rate

Learns steadily.

Balances speed and stability.

---

# Batch Learning vs Online Learning

| Feature | Batch Learning | Online Learning |
|----------|----------------|-----------------|
| Training | Entire Dataset | Incremental |
| Memory | High | Low |
| Speed | Slow Retraining | Fast Updates |
| New Data | Retrain Model | Update Model |
| Streaming Data | No | Yes |
| Best For | Static Data | Dynamic Data |

---

# Which One Should You Choose?

Choose **Batch Learning** when

- Data is stable.
- Retraining once a week/month is enough.

Choose **Online Learning** when

- Data arrives continuously.
- Predictions need frequent updates.
- Real-time systems are involved.

---

# Retail Sales Forecast Mapping

| Problem | Learning Strategy |
|----------|------------------|
| Monthly Sales Forecast | Batch Learning |
| Daily Demand Forecast | Online Learning |
| Flash Sale Prediction | Online Learning |
| Quarterly Inventory Planning | Batch Learning |
| Dynamic Pricing | Online Learning |

---

# Interview Questions

### Q1. What is Batch Learning?

Training a model using the complete dataset at once.

---

### Q2. What is Online Learning?

Updating the model continuously using new incoming data.

---

### Q3. Difference between fit() and partial_fit()?

`fit()` trains from scratch.

`partial_fit()` updates an existing model.

---

### Q4. What is Incremental Learning?

Learning continuously from new data without retraining from scratch.

---

### Q5. What is Out-of-Core Learning?

Training on datasets that do not fit into memory by processing data in chunks.

---

### Q6. Why is Online Learning useful?

Because it can quickly adapt to changing data.

---

# Common Interview Traps

❌ Online Learning means learning through the internet.

✅ It means continuous model updates.

---

❌ Batch Learning is old technology.

✅ It is still heavily used in production.

---

❌ Online Learning is always better.

✅ Choose based on the problem.

---

# Key Takeaways

- Batch Learning trains on the complete dataset.
- Online Learning updates continuously.
- Incremental Learning is the foundation of Online Learning.
- Out-of-Core Learning helps process datasets larger than RAM.
- `fit()` is used for Batch Learning.
- `partial_fit()` is commonly used for Online Learning.

---

# Revision Cheat Sheet

```
Machine Learning

│

├── Batch Learning
│      ├── Train Once
│      ├── Entire Dataset
│      ├── fit()
│      └── Retrain Model
│
└── Online Learning
       ├── Continuous Updates
       ├── Streaming Data
       ├── partial_fit()
       └── Incremental Learning
```

---

# What's Next?

In the next lecture we will learn

- Instance-Based Learning
- Model-Based Learning
- Lazy Learning
- Eager Learning
- KNN Intuition
- Parametric vs Non-Parametric Models
- Interview Questions
- Retail Examples
# Day 3 - Types of Machine Learning

## 🎯 Goal

After this lecture you should know:

- What are the types of Machine Learning?
- When to use each type?
- Real-world examples
- Interview explanation
- How to identify an ML problem

---

# What is Machine Learning?

Machine Learning means learning patterns from data.

But the question is,

**What kind of data do we have?**

Depending upon the data, Machine Learning is divided into three major categories.

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

Supervised Learning is a type of Machine Learning where the dataset contains both

- Input (Features)
- Correct Output (Target)

The model learns the relationship between them.

```
Input

↓

Machine Learning Model

↓

Correct Output
```

---

## Example

Student Data

| Hours Studied | Marks |
|---------------|-------|
| 2 | 40 |
| 4 | 60 |
| 6 | 80 |

The model learns

```
Hours Studied

↓

Marks
```

Now,

Input

```
5 Hours
```

Prediction

```
70 Marks
```

---

## Real World Examples

- House Price Prediction
- Sales Forecasting
- Email Spam Detection
- Loan Approval
- Disease Prediction
- Stock Price Prediction

---

## Retail Sales Forecasting Example

Features

```
Store

Month

Product

Discount

Festival

Previous Sales
```

Target

```
Next Month Sales
```

Since output is already available,

This is

✅ Supervised Learning

---

# Types of Supervised Learning

There are two types.

```
Supervised Learning

│

├── Regression

└── Classification
```

---

# Regression

Output is Continuous.

Examples

```
₹25,000

42°C

180 Sales

₹12 Lakhs
```

Question

Predict

**How much?**

Examples

- House Price
- Sales
- Temperature
- Salary

Algorithms

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

# Classification

Output is Categories.

Examples

```
Spam

Not Spam
```

```
Fraud

Not Fraud
```

```
Diabetes

No Diabetes
```

Question

Predict

**Which class?**

Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- Naive Bayes

---

# Easy Trick

Regression

↓

Answer is Number

Classification

↓

Answer is Category

---

# 2. Unsupervised Learning

Definition

Dataset contains

Only Inputs

No Target Column.

```
Features

↓

Model

↓

Hidden Patterns
```

---

Imagine you have customer data.

But you don't know

- Rich Customer
- Poor Customer
- Premium Customer

Machine automatically groups similar customers.

---

## Example

Customer Data

| Age | Income | Spending |
|------|----------|-----------|
| 20 | 25000 | High |
| 22 | 27000 | High |
| 55 | 90000 | Low |

Model says

```
Group A

Group B

Group C
```

No labels were given.

---

## Applications

- Customer Segmentation
- Market Basket Analysis
- Recommendation Systems
- Fraud Pattern Detection
- Topic Modeling

---

## Retail Example

Suppose a supermarket has

10 lakh customers.

You don't know

- Premium
- Budget
- Regular

Machine automatically creates groups.

This is

✅ Unsupervised Learning

---

# 3. Reinforcement Learning

Definition

A machine learns by interacting with the environment.

It receives

- Reward
- Penalty

and improves over time.

```
Action

↓

Environment

↓

Reward / Penalty

↓

Learn
```

---

Example

Teaching a Dog

Correct Action

↓

Give Biscuit

Wrong Action

↓

No Reward

The dog gradually learns.

Exactly same idea.

---

Applications

- Self Driving Cars
- Chess
- Robotics
- Games
- Recommendation Optimization

---

# Comparison

| Feature | Supervised | Unsupervised | Reinforcement |
|----------|------------|--------------|---------------|
| Labels Available | ✅ Yes | ❌ No | Reward |
| Goal | Prediction | Pattern Discovery | Best Action |
| Output | Known | Unknown | Policy |
| Example | House Price | Customer Segmentation | Self Driving |

---

# How to Identify the Problem?

Question 1

Do you have target/output?

YES

↓

Supervised Learning

---

Question 2

No target?

↓

Need grouping?

↓

Unsupervised Learning

---

Question 3

Learning by trial and error?

↓

Reinforcement Learning

---

# Interview Questions

## What is Supervised Learning?

A Machine Learning technique where the dataset contains both input features and correct output labels, allowing the model to learn the mapping between them.

---

## What is Unsupervised Learning?

A Machine Learning technique where the dataset has no target variable and the model discovers hidden patterns or groups in the data.

---

## What is Reinforcement Learning?

A Machine Learning approach where an agent learns by interacting with an environment using rewards and penalties.

---

## Difference Between Regression and Classification?

Regression predicts continuous numerical values.

Classification predicts discrete categories.

---

## Is Sales Forecasting Regression or Classification?

Regression.

Because sales are numerical values.

---

## Is Spam Detection Regression?

No.

It is Classification because output is

Spam / Not Spam.

---

# Common Interview Trap

Question:

Customer Segmentation belongs to?

❌ Supervised Learning

✅ Unsupervised Learning

Because there is no target column.

---

# Key Takeaways

✅ Machine Learning has three major types.

✅ Supervised Learning uses labeled data.

✅ Regression predicts numbers.

✅ Classification predicts categories.

✅ Unsupervised Learning finds hidden patterns.

✅ Reinforcement Learning learns using rewards.

---

# 30 Second Revision

Machine Learning

│

├── Supervised

│     ├── Regression → Numbers

│     └── Classification → Categories

│

├── Unsupervised → Hidden Patterns

│

└── Reinforcement → Rewards & Penalties

---

# What's Next?

➡️ Machine Learning Development Life Cycle (End-to-End ML Pipeline)

This is one of the most important lectures because every real-world ML project follows this workflow.
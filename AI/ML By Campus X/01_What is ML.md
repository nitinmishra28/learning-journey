# Day 1 - What is Machine Learning?

## 🎯 Learning Objective

Understand:
- What Machine Learning is  
- Why it is needed
- Where it is used
- Types of learning problems
- How ML differs from traditional programming

---

# What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data instead of being explicitly programmed.

Instead of writing every rule manually, we provide examples (data), and the machine learns those rules automatically.

---

## Traditional Programming

Input + Rules
↓

Output

Example:

```
Marks = 95

if marks > 90:
    grade = "A"
```

Here, the programmer writes every rule.

---

## Machine Learning

Input + Correct Output
↓

Machine Learns Rules
↓

Predicts Future Output

Example:

```
Past Sales
↓

Machine Learning Model

↓

Future Sales Prediction
```

No manual rules are written.

---

# Why Machine Learning?

Some real-world problems are impossible or extremely difficult to solve using fixed rules.

Examples:

- Spam Email Detection
- Netflix Recommendations
- YouTube Recommendations
- Credit Card Fraud Detection
- Face Recognition
- Speech Recognition
- Demand Forecasting

Instead of writing millions of rules, ML discovers patterns automatically.

---

# Real-Life Example

Suppose a retail company has sales data for the last five years.

Data:

- Month
- Product
- Store
- Discount
- Festival
- Previous Sales

Target:

```
Next Month Sales
```

Machine Learning learns the relationship between these variables and predicts future demand.

This is exactly what we'll build in our Retail Sales Forecasting project.

---

# What Does Machine Learning Learn?

Machine Learning tries to learn a mathematical relationship between:

Input (Features)

↓

Output (Target)

Example:

Features

```
Area
Bedrooms
Location
Age
```

Target

```
House Price
```

The model learns the mapping:

```
Features → Price
```

---

# Basic Machine Learning Workflow

1. Collect Data
2. Clean Data
3. Explore Data (EDA)
4. Feature Engineering
5. Split Data
6. Train Model
7. Evaluate Model
8. Predict
9. Deploy

---

# Where is Machine Learning Used?

Healthcare

- Disease Prediction
- Medical Imaging

Finance

- Fraud Detection
- Loan Approval

Retail

- Sales Forecasting
- Product Recommendation
- Inventory Management

Social Media

- Feed Ranking
- Friend Suggestions

Transportation

- Self Driving Cars
- Route Optimization

Cyber Security

- Malware Detection
- Spam Detection

---

# Advantages of Machine Learning

- Learns from data
- Improves with more data
- Handles complex problems
- Automates decision making
- Finds hidden patterns

---

# Limitations

- Needs good quality data
- Requires sufficient training data
- Can overfit
- Sometimes difficult to interpret
- Needs continuous monitoring

---

# Python Example

Even without training a model, we can load data using Pandas.

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())
```

This is the first step in every ML project.

---

# Retail Forecasting Connection

Dataset

| Month | Product | Discount | Previous Sales | Target |
|--------|----------|----------|----------------|--------|
| Jan | TV | 10% | 250 | 270 |
| Feb | TV | 5% | 270 | 290 |

Machine Learning learns:

```
Features
↓

Sales Prediction
```

---

# Interview Questions

### What is Machine Learning?

Machine Learning is a subset of AI where systems learn patterns from historical data to make predictions or decisions without being explicitly programmed.

---

### Why not use traditional programming?

Because many real-world problems have no fixed rules.

---

### Give some Machine Learning applications.

- Recommendation Systems
- Sales Forecasting
- Fraud Detection
- Spam Detection
- Face Recognition
- Medical Diagnosis

---

### What is data?

A collection of observations used to train Machine Learning models.

---

# Key Takeaways

✅ ML learns patterns from data.

✅ More quality data usually leads to better models.

✅ ML is used when writing explicit rules is difficult.

✅ Every ML project follows a standard workflow.

✅ Retail Sales Forecasting is a supervised ML problem.

---

# Next Lecture

➡️ AI vs Machine Learning vs Deep Learning

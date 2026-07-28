# 01 - AI, Machine Learning & Model Fundamentals

## 🎯 Goal

Understand the foundation of Machine Learning before building any ML model.

---

# 1. Artificial Intelligence (AI)

Artificial Intelligence (AI) is the field of making machines perform tasks that normally require human intelligence.

Examples:
- ChatGPT
- Self-driving Cars
- Face Recognition
- Recommendation Systems
- Voice Assistants

> AI is a broad field. Machine Learning is one part of AI.

---

# 2. Machine Learning (ML)

Machine Learning is a technique where computers learn patterns from historical data instead of following manually written rules.

### Traditional Programming

```
Input + Rules
      ↓
   Output
```

Example

```python
if marks >= 40:
    print("Pass")
```

Rules are written by the programmer.

---

### Machine Learning

```
Historical Data + Correct Answers
               ↓
          Model Learns Patterns
               ↓
           Future Prediction
```

Rules are **not** written manually.

The model learns them automatically from data.

---

# 3. AI vs Machine Learning

| AI | Machine Learning |
|----|------------------|
| Broad field | Subset of AI |
| Focuses on intelligent systems | Focuses on learning from data |
| Can be rule-based | Always learns from data |

---

# 4. Where does our Retail Forecasting Project fit?

```
Artificial Intelligence
        │
Machine Learning
        │
Regression
        │
Time Series Forecasting
        │
Retail Sales Forecasting
```

Our project belongs to **Machine Learning (Regression + Time Series)**.

---

# 5. Machine Learning Goal

The goal of Machine Learning is:

> Learn hidden relationships from historical data and use them to predict unseen data.

Example

Input

- Month
- Product
- Territory
- Brand
- Previous Sales

↓

Output

- Next Month Sales Quantity

---

# 6. Raw Data vs Features

## Raw Data

Data received directly from the company.

Example

| Posting Date | Customer Name | Document No | Sales Quantity |
|--------------|---------------|-------------|----------------|

Raw data contains:

- Useful information
- Duplicate information
- Noise
- IDs
- Missing values

---

## Features

Features are useful pieces of information extracted from raw data that help the model learn patterns.

Example

Raw Data

```
Posting Date = 15-Jul-2026
```

Features

```
Month = July
Quarter = Q3
Year = 2026
```

Another Example

Raw Data

```
Posting Date
```

Feature Engineering

```
Lag 1 Month Sales
Rolling Average
Lag 12 Month Sales
```

These features do not exist in raw data.

We create them.

---

### Golden Definition

> Features are meaningful representations of raw data that help the model learn patterns.

---

# 7. Feature & Target

### Features (Input)

Examples

- Month
- Year
- Territory
- Brand
- ItemCode

### Target (Output)

```
Sales Quantity
```

The model learns the relationship between Features and Target.

---

# 8. What is a Model?

A Model is **not AI magic**.

A Model is simply a mathematical function that learns the relationship between input features and the target.

Example

```
Experience
      ↓
Model Learns
      ↓
Salary
```

Mathematically

```
Salary = f(Experience)
```

Here **f** is the model.

---

# 9. What happens inside model.fit() ?

```
Historical Data
        ↓
Model Learns Relationships
        ↓
Creates Trained Model
```

`fit()` does **NOT** memorize the dataset.

It learns patterns.

---

# 10. What happens inside model.predict() ?

```
New Features
       ↓
Trained Model
       ↓
Prediction
```

Prediction uses learned knowledge.

It does **not** read the original CSV again.

---

# 11. Does the Model store the CSV?

No.

The model stores only learned knowledge.

Different algorithms store different information.

Examples

### Linear Regression

Stores

- Slope
- Intercept

### Decision Tree

Stores

- Decision Rules

### LightGBM

Stores

- Hundreds/Thousands of Decision Trees

---

# 12. ML Pipeline

```
CSV
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
model.fit()
   ↓
Trained Model
   ↓
model.predict()
   ↓
Prediction
```

---

# 13. Software Engineering vs AI

| Task | AI? |
|------|-----|
| Read CSV | ❌ |
| Data Cleaning | ❌ |
| GroupBy | ❌ |
| Feature Engineering | ❌ |
| Train Model (`fit`) | ✅ |
| Prediction (`predict`) | ✅ |
| Save Model | ❌ |
| FastAPI Deployment | ❌ |

> Most of an ML Engineer's work is Software Engineering.

---

# 14. Learning vs Memorization

Machine Learning should learn patterns, not memorize data.

### Learning

```
Training Data
      ↓
Learns Relationship
      ↓
Correct Prediction on New Data
```

### Memorization

```
Training Data
      ↓
Remembers Every Record
      ↓
Fails on New Data
```

---

# 15. Generalization

Generalization means:

> The ability of a model to make accurate predictions on unseen data.

This is the ultimate goal of Machine Learning.

---

# 16. Overfitting

Overfitting happens when the model memorizes the training data instead of learning general patterns.

Characteristics

- Very high training accuracy
- Poor performance on new data

```
Training Data
      ↓
Model memorizes everything
      ↓
Future prediction becomes poor
```

---

# 17. Underfitting

Underfitting happens when the model is too simple to learn the patterns.

Characteristics

- Poor training performance
- Poor testing performance

```
Too Simple Model
        ↓
Fails to learn patterns
```

---

# 18. Golden Rules

### Rule 1

> Machine Learning learns patterns, not rules written by programmers.

---

### Rule 2

> Features are more important than algorithms.

---

### Rule 3

> `fit()` learns relationships.

---

### Rule 4

> `predict()` uses learned relationships.

---

### Rule 5

> The goal of ML is **Generalization**, not high training accuracy.

---

# 📝 Key Takeaways

- AI is the broader field.
- Machine Learning is a subset of AI.
- Forecasting is a Regression problem.
- Features are created from raw data.
- Target is the value we want to predict.
- A model is a mathematical function that learns relationships.
- `fit()` trains the model.
- `predict()` makes predictions using learned knowledge.
- Models do not store the original dataset.
- ML should learn patterns, not memorize data.
- Generalization is the primary goal of Machine Learning.
- Overfitting memorizes data.
- Underfitting fails to learn patterns.
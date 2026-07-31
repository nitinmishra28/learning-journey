# Day 06 - Machine Learning Development Life Cycle (Part 1)

> **Course:** CampusX - 100 Days of Machine Learning

---

# 🎯 Learning Objectives

After completing this lecture, you will be able to:

- Understand the complete Machine Learning Development Life Cycle.
- Know why ML projects follow a structured pipeline.
- Learn the first three stages of the ML lifecycle.
- Connect these stages with a real Retail Sales Forecasting project.
- Answer interview questions related to the ML pipeline.

---

# 📚 Prerequisites

Before starting this lecture, you should know:

- What is Machine Learning?
- Types of Machine Learning
- Batch vs Online Learning
- Instance-Based vs Model-Based Learning

---

# Introduction

Building a Machine Learning model is **not just about training an algorithm**.

Many beginners think that Machine Learning means

```
Dataset

↓

Algorithm

↓

Prediction
```

But in reality,

this is only a small part of the complete process.

A real Machine Learning project goes through multiple stages before reaching production.

---

# What is Machine Learning Development Life Cycle?

The **Machine Learning Development Life Cycle (MLDLC)** is a structured process that guides us from understanding the business problem to deploying and maintaining an ML model in production.

Think of it as a roadmap for building reliable, scalable, and useful Machine Learning systems.

---

# Why Do We Need a Life Cycle?

Imagine you are building a house.

Would you start by painting the walls?

No.

You would first:

- Buy land
- Create a design
- Build the foundation
- Construct the structure
- Paint
- Decorate

Machine Learning follows the same principle.

If we skip important steps like data cleaning or evaluation, the final model may fail even if we use a powerful algorithm.

---

# Complete Machine Learning Life Cycle

```
Business Problem

↓

Data Collection

↓

Data Understanding

↓

Data Cleaning

↓

Feature Engineering

↓

Feature Selection

↓

Model Selection

↓

Model Training

↓

Model Evaluation

↓

Deployment

↓

Monitoring

↓

Retraining
```

This is the complete journey of an ML model.

In this part, we will focus on the first three stages.

---

# Step 1: Business Problem Understanding

## Definition

Before writing a single line of code, we must clearly understand **what problem we are trying to solve**.

Machine Learning should always solve a **business problem**, not just a technical problem.

---

# Why is this Step Important?

If the business problem is unclear,

the entire project can fail.

A highly accurate model is useless if it solves the wrong problem.

---

# Questions to Ask

Before starting, ask:

- What problem are we solving?
- Why does this problem matter?
- Who will use the model?
- What type of prediction is required?
- How will success be measured?

---

# Example

Business:

A supermarket wants to reduce inventory wastage.

Problem:

Products expire because demand is predicted incorrectly.

Goal:

Predict future product demand accurately.

Machine Learning Task:

Demand Forecasting (Regression).

---

# Retail Sales Forecasting Example

Suppose a retail company asks:

> "How many units of milk should we stock next week?"

This is the business problem.

The ML engineer converts it into a Machine Learning problem:

**Predict future sales using historical data.**

---

# Interview Tip

Always start with the business objective.

Interviewers often ask:

> "Why are you building this model?"

Never answer with:

> "Because I want to use XGBoost."

Instead, answer with the business goal.

---

# Step 2: Data Collection

## Definition

Once the problem is understood,

the next step is collecting relevant data.

A Machine Learning model is only as good as the data used to train it.

---

# Sources of Data

Data can come from:

- Company Databases
- CSV Files
- APIs
- IoT Devices
- Sensors
- Web Scraping
- Public Datasets (Kaggle, UCI)
- Cloud Storage
- Data Warehouses

---

# Retail Example

For Retail Sales Forecasting, we may collect:

- Product ID
- Store ID
- Date
- Sales Quantity
- Promotion
- Holiday
- Temperature
- Fuel Price
- Competitor Pricing
- Inventory Levels

These features help the model learn sales patterns.

---

# Why Data Quality Matters

Poor data leads to poor models.

A famous saying in Machine Learning is:

> **"Garbage In, Garbage Out (GIGO)."**

If the collected data contains errors, duplicates, or missing values, the model's predictions will also be poor.

---

# Common Challenges

- Missing values
- Duplicate records
- Incorrect labels
- Inconsistent formats
- Data collected from multiple sources

---

# Interview Question

### Which is more important: Algorithm or Data?

Generally, **high-quality data** has a greater impact than choosing a complex algorithm.

---

# Step 3: Data Understanding (Exploratory Data Analysis - Introduction)

## Definition

After collecting the data, we should not immediately train a model.

First, we need to understand the dataset.

This process is called **Exploratory Data Analysis (EDA).**

---

# Goals of EDA

- Understand the structure of the data.
- Identify missing values.
- Detect outliers.
- Find relationships between features.
- Understand the target variable.
- Generate insights for feature engineering.

---

# Questions to Explore

- How many rows and columns are there?
- What are the data types?
- Are there missing values?
- Are there duplicate records?
- What is the distribution of the target variable?
- Are there unusual patterns?

---

# Retail Example

Suppose we have:

| Date | Product | Sales |
|------|---------|------|
| Jan 1 | Milk | 200 |
| Jan 2 | Milk | 205 |
| Jan 3 | Milk | NULL |
| Jan 4 | Milk | 198 |

EDA helps us identify that sales are missing on Jan 3.

Instead of directly training the model, we first investigate why this value is missing.

---

# Python Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df.head()

df.info()

df.describe()

df.isnull().sum()
```

These commands help us quickly understand the dataset.

---

# Interview Questions

### What is the first step in an ML project?

Understanding the business problem.

---

### Why do we perform EDA?

To understand the dataset before training the model.

---

### What is GIGO?

Garbage In, Garbage Out.

Poor-quality data results in poor predictions.

---

### Why is Business Understanding important?

Because solving the wrong business problem makes even an accurate model useless.

---

# Common Mistakes

❌ Starting model training immediately after collecting data.

✅ Always perform EDA first.

---

❌ Choosing an algorithm before understanding the problem.

✅ Understand the business objective first.

---

❌ Assuming collected data is always clean.

✅ Verify data quality before model training.

---

# Key Takeaways

- Every ML project starts with understanding the business problem.
- High-quality data is essential for good models.
- EDA helps us understand and validate the dataset.
- Never train a model without understanding your data first.

---

# What's Next?

In **Part 2**, we will cover:

- Data Cleaning
- Feature Engineering
- Feature Selection
- Model Selection
- Model Training
- Python Examples
- Interview Questions


# Day 06 - Machine Learning Development Life Cycle (Part 2)

> **Topics Covered**
>
> - Data Cleaning
> - Feature Engineering
> - Feature Selection
> - Model Selection
> - Model Training
> - Python Examples
> - Retail Sales Forecasting Examples
> - Interview Questions

---

# Step 4: Data Cleaning

## Definition

Data Cleaning is the process of improving the quality of the dataset before training a Machine Learning model.

Real-world datasets are almost never perfect.

They usually contain

- Missing Values
- Duplicate Records
- Incorrect Data
- Outliers
- Inconsistent Formats

If these problems are not fixed, the model will learn incorrect patterns.

---

# Why is Data Cleaning Important?

Remember the famous quote:

> **Garbage In = Garbage Out (GIGO)**

Even the best Machine Learning algorithm cannot produce good predictions if the input data is poor.

---

# Common Data Cleaning Tasks

### Missing Values

Example

| Product | Sales |
|----------|------|
| Milk | 200 |
| Bread | NULL |
| Eggs | 180 |

Possible solutions

- Remove the row
- Replace with Mean
- Replace with Median
- Replace with Mode
- Predict the missing value

---

### Duplicate Records

Example

| Product | Sales |
|----------|------|
| Milk | 200 |
| Milk | 200 |

Duplicates should usually be removed.

---

### Incorrect Data

Example

Age = -15

Temperature = 300°C

Sales = -500

These values should be investigated.

---

### Outliers

Example

```
200

198

210

205

15000
```

The value **15000** may be an outlier.

Possible reasons

- Festival
- Data Entry Error
- Fraud

---

# Python Example

```python
df.isnull().sum()

df.drop_duplicates()

df.fillna(df["Sales"].mean())
```

---

# Retail Example

Suppose yesterday's sales are missing.

Instead of directly training the model,

we first decide how to handle the missing values.

Otherwise,

the forecasting model may become inaccurate.

---

# Step 5: Feature Engineering

## Definition

Feature Engineering is the process of creating new useful features from existing data.

It is one of the most important steps in Machine Learning.

Many Kaggle competitions are won because of better feature engineering rather than better algorithms.

---

# Why Do We Need Feature Engineering?

Raw data is often not informative enough.

We create features that help the model understand hidden patterns.

---

# Example

Original Feature

```
Date

2025-07-15
```

New Features

- Day
- Month
- Year
- Week Number
- Weekend
- Quarter
- Festival Indicator

The model can now learn seasonal patterns.

---

# Retail Forecasting Example

Original Features

- Date
- Sales

New Features

- Day of Week
- Is Weekend
- Holiday
- Month
- Season
- Previous Day Sales
- 7-Day Moving Average

These new features often improve forecasting accuracy significantly.

---

# More Examples

Customer DOB

↓

Age

---

Timestamp

↓

Hour

↓

Morning / Evening

---

City

↓

Region

↓

State

---

# Python Example

```python
df["Month"] = df["Date"].dt.month

df["Day"] = df["Date"].dt.day

df["Weekday"] = df["Date"].dt.dayofweek
```

---

# Interview Tip

A simple model with excellent features often outperforms a complex model with poor features.

---

# Step 6: Feature Selection

## Definition

Feature Selection means selecting only the most useful features for model training.

Not every column is useful.

Some columns

- Add noise
- Increase computation
- Cause overfitting
- Increase training time

---

# Example

Dataset

```
Customer ID

Product ID

Sales

Temperature

Holiday

Weather

```

Question

Should Customer ID be used?

Usually

No.

Customer ID has no predictive relationship with sales.

---

# Benefits

- Faster training
- Better interpretability
- Reduced overfitting
- Lower computational cost

---

# Common Techniques

- Correlation Analysis
- Recursive Feature Elimination (RFE)
- Feature Importance
- Lasso Regression
- Tree-Based Selection

---

# Python Example

```python
from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=5)

X_new = selector.fit_transform(X, y)
```

---

# Feature Engineering vs Feature Selection

| Feature Engineering | Feature Selection |
|---------------------|------------------|
| Create New Features | Remove Unnecessary Features |
| Adds Information | Removes Noise |

---

# Step 7: Model Selection

## Definition

After preparing the data,

the next step is choosing the appropriate Machine Learning algorithm.

Different problems require different algorithms.

---

# Examples

Regression Problems

- Linear Regression
- Decision Tree Regressor
- Random Forest
- XGBoost

Classification Problems

- Logistic Regression
- KNN
- SVM
- Random Forest

Clustering Problems

- K-Means
- DBSCAN
- Hierarchical Clustering

---

# How to Choose?

Ask

- Is the problem Regression?
- Is it Classification?
- How much data is available?
- Is interpretability important?
- Is prediction speed important?

---

# Retail Forecasting Example

Target

Future Sales

Output

Numeric

Problem Type

Regression

Possible Models

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- LightGBM

---

# Interview Tip

Never start with the most complex algorithm.

Start with a simple baseline model.

Example

Linear Regression

↓

Random Forest

↓

XGBoost

Compare their performance.

---

# Step 8: Model Training

## Definition

Model Training is the process where the algorithm learns patterns from historical data.

This is the stage where Machine Learning actually happens.

---

# Training Process

```
Training Data

↓

Algorithm

↓

Learn Pattern

↓

Trained Model
```

---

# Python Example

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

The `fit()` function trains the model.

---

# Retail Forecasting Example

Training Data

| Date | Sales |
|------|------|
| Jan | 200 |
| Feb | 210 |
| Mar | 225 |

The algorithm learns how different factors influence sales.

Later,

it predicts future demand.

---

# Common Training Mistakes

❌ Training on raw data

✅ Clean data first

---

❌ Using all features

✅ Select meaningful features

---

❌ Jumping directly to XGBoost

✅ Start with a simple baseline model

---

# Interview Questions

### What is Feature Engineering?

Creating new useful features from existing data.

---

### What is Feature Selection?

Selecting only relevant features for training.

---

### Difference between Feature Engineering and Feature Selection?

Feature Engineering creates features.

Feature Selection removes unnecessary features.

---

### Why is Model Selection important?

Because different algorithms perform differently on different problems.

---

### What happens during Model Training?

The algorithm learns patterns from historical data.

---

# Key Takeaways

- Clean data before training.
- Better features often improve performance more than better algorithms.
- Select only useful features.
- Choose the algorithm based on the problem.
- Train the model using historical data.

---

# What's Next?

In **Part 3**, we will cover:

- Model Evaluation
- Deployment
- Monitoring
- Model Retraining
- MLOps Introduction
- End-to-End Retail Forecasting Pipeline
- Industry Best Practices
- Revision Cheat Sheet
- 25+ Interview Questions



# Day 06 - Machine Learning Development Life Cycle (Part 3)

> Topics Covered
>
> - Model Evaluation
> - Model Deployment
> - Model Monitoring
> - Model Retraining
> - MLOps Introduction
> - Complete Retail Sales Forecasting Pipeline
> - Industry Best Practices
> - Interview Questions
> - Revision Cheat Sheet

---

# Step 9: Model Evaluation

## Definition

Training a model is **not the end of the Machine Learning process**.

Before deploying a model, we must evaluate how well it performs on unseen data.

Model Evaluation helps answer questions like:

- Is the model accurate?
- Can it generalize to new data?
- Is it better than the baseline model?
- Can we trust it in production?

---

# Why Can't We Evaluate on Training Data?

Imagine a student memorizes all textbook questions.

If the exam contains the same questions, the student scores 100%.

But if the exam contains new questions, the student performs poorly.

The same happens in Machine Learning.

Evaluating on training data gives an overly optimistic result.

Always evaluate on **unseen data**.

---

# Train-Test Split

A common practice is to split the dataset.

```
Dataset

↓

Train Set (80%)

↓

Learn Patterns

↓

Test Set (20%)

↓

Evaluate Performance
```

The model never sees the test data during training.

---

# Common Evaluation Metrics

### Regression

Used when predicting numerical values.

Examples

- Sales Forecasting
- House Price Prediction
- Temperature Prediction

Metrics

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

Smaller error values indicate better performance.

---

### Classification

Used when predicting categories.

Examples

- Spam Detection
- Fraud Detection
- Disease Prediction

Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Different problems require different metrics.

For example, in fraud detection, Recall is often more important than Accuracy.

---

# Python Example

```python
from sklearn.metrics import mean_absolute_error

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print(mae)
```

---

# Retail Forecasting Example

Suppose actual sales are

```
200
220
250
```

Predicted sales

```
198
225
245
```

The evaluation metrics calculate how close the predictions are to the actual sales.

---

# Step 10: Model Deployment

## Definition

After evaluation,

the model is made available for real users.

This process is called **Deployment**.

Without deployment,

a Machine Learning model has no business value.

---

# Deployment Flow

```
Train Model

↓

Save Model

↓

Deploy API

↓

User Request

↓

Prediction

↓

Return Response
```

---

# Common Deployment Methods

- Flask API
- FastAPI
- Streamlit
- Docker
- AWS SageMaker
- Azure ML
- Google Vertex AI

---

# Example

A retail manager enters

- Product
- Store
- Date
- Promotion

The deployed model predicts

```
Expected Sales = 238 Units
```

within a few milliseconds.

---

# Python Example

```python
import joblib

joblib.dump(model, "sales_forecast.pkl")
```

Later, the saved model can be loaded inside a FastAPI or Flask application.

---

# Step 11: Model Monitoring

## Definition

Deployment is **not the end**.

Models may become less accurate over time because the real world changes.

Monitoring continuously checks whether the model is still performing well.

---

# Why Monitoring is Needed

Customer behavior changes.

New competitors appear.

Weather changes.

Prices change.

Festivals occur.

The model trained six months ago may no longer represent current patterns.

---

# What Do We Monitor?

- Prediction Accuracy
- Response Time
- Error Rate
- Missing Predictions
- Data Quality
- Resource Usage

---

# Retail Example

Suppose your model was trained before a festive season.

After the festival,

customer buying behavior changes.

Monitoring detects that prediction errors are increasing.

This signals that the model may need retraining.

---

# Step 12: Model Retraining

## Definition

As new data becomes available,

the model should learn from it.

This process is called **Model Retraining**.

---

# Why Retraining?

Suppose your model was trained using 2024 data.

Now it's 2026.

Customer behavior has changed.

Without retraining,

predictions become less accurate.

---

# Retraining Flow

```
New Data

↓

Data Cleaning

↓

Feature Engineering

↓

Train Again

↓

Deploy Updated Model
```

---

# Concept: Data Drift

Data Drift occurs when the distribution of input data changes over time.

Example

Earlier

Milk sales = 200/day

Now

Milk sales = 450/day

The model may fail because the data distribution has shifted.

---

# Concept: Concept Drift

Concept Drift occurs when the relationship between inputs and outputs changes.

Example

Earlier

Rain increased umbrella sales.

Now

A new competitor offers discounts.

Customer behavior changes.

The old relationship no longer holds.

---

# Introduction to MLOps

## What is MLOps?

MLOps (Machine Learning Operations) is the practice of managing Machine Learning models throughout their lifecycle.

It combines

- Machine Learning
- DevOps
- Automation

to make ML systems reliable and scalable.

---

# Responsibilities of MLOps

- Model Versioning
- Automated Training
- Deployment Pipelines
- Continuous Monitoring
- Retraining
- Experiment Tracking

---

# Popular MLOps Tools

- MLflow
- DVC
- Kubeflow
- Airflow
- Docker
- Kubernetes
- GitHub Actions

---

# End-to-End Retail Sales Forecasting Pipeline

Let's connect everything we've learned.

```
Business Goal
↓
Predict Weekly Sales
↓
Collect Historical Sales Data
↓
Perform EDA
↓
Clean Data
↓
Feature Engineering
↓
Feature Selection
↓
Train Model
↓
Evaluate Model
↓
Deploy with FastAPI
↓
Predict Future Sales
↓
Monitor Accuracy
↓
Retrain Every Month
```

This is exactly how a production ML project works.

---

# Industry Best Practices

- Always define the business objective first.
- Understand the data before training.
- Start with a simple baseline model.
- Track experiments and model versions.
- Evaluate on unseen data.
- Monitor deployed models.
- Retrain periodically.
- Automate repetitive tasks.

---

# Interview Questions

### What is the Machine Learning Development Life Cycle?

A structured process of building, deploying, monitoring, and maintaining ML models.

---

### Why is EDA important?

To understand the dataset and identify issues before training.

---

### Why is Feature Engineering important?

It helps the model learn better patterns by creating informative features.

---

### Why shouldn't we evaluate on training data?

Because it leads to overly optimistic performance estimates and doesn't measure generalization.

---

### What is Deployment?

Making the trained model available for real users or applications.

---

### Why do we monitor deployed models?

To detect performance degradation, failures, and changing data patterns.

---

### What is Data Drift?

A change in the distribution of input data over time.

---

### What is Concept Drift?

A change in the relationship between input features and the target variable.

---

### Why is Retraining necessary?

Because real-world data evolves, and models need to learn from new information.

---

### What is MLOps?

The practice of automating and managing the ML lifecycle from development to production.

---

# Common Mistakes

❌ Deploying without evaluation.

✅ Evaluate thoroughly before deployment.

---

❌ Ignoring model performance after deployment.

✅ Continuously monitor production models.

---

❌ Assuming a model works forever.

✅ Retrain when data or business conditions change.

---

❌ Chasing only high accuracy.

✅ Choose evaluation metrics based on the business problem.

---

# Revision Cheat Sheet

```
Business Problem
        │
        ▼
Data Collection
        │
        ▼
Data Understanding (EDA)
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Feature Selection
        │
        ▼
Model Selection
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Deployment
        │
        ▼
Model Monitoring
        │
        ▼
Model Retraining
```

---

# Key Takeaways

- Machine Learning is a complete lifecycle, not just model training.
- Data quality directly impacts model performance.
- Feature Engineering often has a larger impact than changing algorithms.
- Always evaluate on unseen data.
- Deployment brings business value.
- Monitoring ensures long-term reliability.
- Retraining keeps the model relevant as data evolves.
- MLOps enables scalable, automated ML systems.

---

# Final Summary

The **Machine Learning Development Life Cycle** provides a systematic approach to building production-ready ML solutions. Every successful ML project follows this journey—from understanding the business problem, preparing and modeling data, to deployment, monitoring, and continuous improvement.

Mastering this lifecycle is essential because it reflects how Machine Learning is applied in real companies such as Amazon, Netflix, Uber, Flipkart, and Walmart. Whether you're building a recommendation system, fraud detection model, or retail sales forecasting solution, these stages remain the foundation of every professional ML workflow.
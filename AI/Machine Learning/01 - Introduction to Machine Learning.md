# 01 - Introduction to Machine Learning

## What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from historical data and make predictions or decisions without being explicitly programmed for every scenario.

Instead of writing thousands of rules manually, we provide data to the machine, and it learns those rules automatically.

---

## Traditional Programming vs Machine Learning

### Traditional Programming

```
Data + Rules
        ↓
     Program
        ↓
      Output
```

Example:

```
Age = 22
Rule:
If age >= 18
    Eligible
Else
    Not Eligible
```

Here, **we write the rules**.

---

### Machine Learning

```
Data + Correct Output
          ↓
     Train Model
          ↓
      Learned Rules
          ↓
      Prediction
```

Instead of writing rules manually, the algorithm learns them from the data.

---

# Retail Forecasting Example

Suppose you own a supermarket.

Every day you record:

| Date | Product | Price | Discount | Store | Quantity Sold |
|------|----------|--------|-----------|---------|---------------|
|1 Jan|Milk|50|10%|Delhi|120|
|2 Jan|Milk|45|20%|Delhi|165|
|3 Jan|Milk|55|0%|Delhi|95|

After collecting data for many months, we want to answer:

> **"How many units will be sold tomorrow?"**

This is where Machine Learning is used.

---

# Machine Learning Pipeline

```
Raw Data
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train Model
     ↓
Evaluate Model
     ↓
Prediction
```

Let's understand every step.

---

# Step 1 - Raw Data

Raw Data is the original data collected from different sources.

It contains everything, including useful information, unnecessary columns, duplicate records and missing values.

Example:

| Date | Product | Price | Discount | Store | Quantity Sold |
|------|----------|--------|-----------|---------|---------------|
|1 Jan|Milk|50|10%|Delhi|120|

This is simply collected data.

Nothing has been prepared for Machine Learning yet.

---

# Step 2 - Data Cleaning

Raw data is usually messy.

Problems may include

- Missing values
- Duplicate rows
- Wrong values
- Different formats
- Incorrect data types

Example

```
Price = NULL

↓

Replace with average price
```

or

```
Store = delhi
Store = Delhi

↓

Store = Delhi
```

Goal:

Make the dataset clean before training.

---

# Step 3 - Features

Features are the input variables given to the model.

They are represented by **X**.

For our retail dataset,

Possible Features are:

- Product Category
- Price
- Discount
- Store Location
- Day of Week

The model studies these variables to learn patterns.

---

# Step 4 - Target

Target is the value that we want the model to predict.

It is represented by **y**.

For Retail Forecasting,

```
Target = Quantity Sold
```

The model learns

```
Features
↓

Quantity Sold
```

---

# Features vs Target

Example

| Price | Discount | Store | Day | Quantity Sold |
|--------|-----------|--------|-----|---------------|
|50|10%|Delhi|Monday|120|

Features (X)

- Price
- Discount
- Store
- Day

Target (y)

- Quantity Sold

---

# Step 5 - Feature Engineering

Feature Engineering means creating better input features from existing data.

Instead of directly giving the date,

```
01-01-2025
```

we can extract

- Day
- Month
- Weekend
- Festival
- Quarter

These new features help the model learn better.

Example

```
Date

↓

Saturday

↓

Weekend = Yes
```

This gives more useful information to the model.

---

# Step 6 - Model

A model is a mathematical function that learns patterns from historical data.

During training,

the model learns relationships like

```
Higher Discount
        +
Weekend
        +
Festival

↓

Higher Sales
```

After training,

the model can predict sales for unseen data.

---

# Step 7 - Training

Training means teaching the model using historical data.

Example

```
Previous 2 Years Sales

↓

Model learns patterns

↓

Ready for Prediction
```

The more quality data we have, the better the model usually performs.

---

# Step 8 - Prediction

Now suppose tomorrow's information is

| Price | Discount | Store | Weekend |
|--------|-----------|--------|----------|
|45|20%|Delhi|Yes|

The trained model predicts

```
Expected Quantity Sold = 170 Units
```

This prediction helps the business plan inventory.

---

# Why Machine Learning?

Without ML,

we would need thousands of rules.

Example

```
IF Weekend
AND Discount > 20%
AND Festival

THEN Increase Sales
```

But writing rules for every situation is impossible.

Machine Learning automatically learns these patterns.

---

# Real-Life Applications

- Retail Sales Forecasting
- House Price Prediction
- Stock Price Prediction
- Recommendation Systems
- Spam Detection
- Fraud Detection
- Medical Diagnosis
- Face Recognition

---

# Important Terms

## Dataset

A collection of data used for Machine Learning.

---

## Observation

One complete row in the dataset.

---

## Feature

Input variable (X)

---

## Target

Output variable (y)

---

## Model

Mathematical function that learns patterns.

---

## Prediction

Output produced by the trained model.

---

# Quick Revision

```
Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Features (X)
    ↓
Train Model
    ↓
Prediction (Target y)
```

---

# Interview Questions

### What is Machine Learning?

Machine Learning is a technique where computers learn patterns from historical data to make predictions without explicitly programming every rule.

---

### What are Features?

Features are the input variables given to the model.

Example:

- Price
- Discount
- Store
- Day

---

### What is Target?

The output variable that the model predicts.

Example:

Quantity Sold

---

### What is a Model?

A mathematical function that learns patterns from training data and predicts outputs for unseen data.

---

### Difference between Raw Data and Features?

| Raw Data | Features |
|----------|-----------|
|Original collected data|Useful input variables|
|Contains everything|Contains selected useful columns|
|May contain noise|Prepared for the model|

---

### Retail Forecasting Problem

**Features (X)**

- Product Category
- Price
- Discount
- Store Location
- Day of Week

**Target (y)**

- Quantity Sold

```

---

### 💡 Ek suggestion (jo long term me bahut help karega)

Har lecture ke end me ye 3 sections zarur rakhna:

1. **Revision (1 minute)**
2. **Interview Questions**
3. **Common Confusions**

Jaise is lecture me "Raw Data vs Features", "Features vs Target", aur "Traditional Programming vs Machine Learning" wale confusions. Jab tum 6–8 mahine baad revise karoge ya interview doge, ye sections sabse zyada useful rahenge.
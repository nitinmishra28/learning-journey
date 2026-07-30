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


# Day 3 - Types of Machine Learning (Part 2)

> Topics Covered
>
> - Unsupervised Learning
> - Clustering
> - Association Rule Learning
> - Beer & Diapers Story
> - Market Basket Analysis
> - Dimensionality Reduction
> - PCA
> - t-SNE
> - MNIST Visualization
> - Anomaly Detection

---

# 2. Unsupervised Learning

## Definition

Unsupervised Learning is a Machine Learning paradigm where the dataset contains **only input features (X)** and **no target variable (Y)**.

Unlike Supervised Learning, the model is **not told the correct answer**.

Instead, it tries to discover hidden structures, similarities, relationships, or unusual patterns in the data.

---

## Intuition

Imagine you enter a library where thousands of books are scattered on the floor.

Nobody tells you which book belongs to which category.

You naturally start grouping books based on similarity:

- Programming Books
- Mathematics Books
- History Books
- Fiction Books

No one supervised you.

You found the patterns yourself.

This is exactly what an Unsupervised Learning algorithm does.

---

# Why Do We Need Unsupervised Learning?

Real-world companies generate huge amounts of data.

Example:

Customer Data

- Age
- Income
- Location
- Purchase Amount
- Number of Orders

But nobody has labeled customers as

- Premium
- Regular
- Budget

The machine automatically discovers these groups.

---

# Mathematical View

Dataset

```
X₁

X₂

X₃

...

Xₙ
```

Notice

There is **no Y**.

Goal

```
Find Hidden Patterns
```

---

# Applications

- Customer Segmentation
- Product Recommendation
- Market Basket Analysis
- Fraud Pattern Discovery
- Image Compression
- Topic Modeling
- Document Clustering
- Medical Research
- Social Network Analysis

---

# Types of Unsupervised Learning

```
Unsupervised Learning

│

├── Clustering

├── Association Rule Learning

├── Dimensionality Reduction

└── Anomaly Detection
```

---

# 1. Clustering

## Definition

Clustering means grouping similar data points together.

Points inside one cluster are more similar to each other than to points in other clusters.

---

## Everyday Example

Imagine your phone gallery.

You never told your phone

"This is Mom."

"This is Dad."

"This is Friend."

Still,

Google Photos groups similar faces together.

This is Clustering.

---

## Retail Example

Suppose a supermarket has data of 5 lakh customers.

Available information:

- Income
- Age
- Shopping Frequency
- Monthly Spending

The company doesn't know who is:

- Premium
- Budget
- Regular

The algorithm automatically forms groups.

Example:

```
Cluster 1

High Income

High Spending

↓

Premium Customers
```

```
Cluster 2

Low Income

Low Spending

↓

Budget Customers
```

---

## Applications

- Customer Segmentation
- Image Segmentation
- News Grouping
- Disease Analysis
- Social Network Communities

---

## Popular Algorithms

### K-Means

Most popular clustering algorithm.

Works well when clusters are roughly spherical.

---

### Hierarchical Clustering

Creates a tree-like hierarchy of clusters.

Useful when you want to understand relationships between groups.

---

### DBSCAN

Density-Based Spatial Clustering.

Advantages

- Finds irregular-shaped clusters.
- Detects noise.
- Finds outliers.

Interview Tip:

DBSCAN does **not require specifying the number of clusters** beforehand.

---

# Interview Question

### Difference Between K-Means and DBSCAN?

| K-Means | DBSCAN |
|----------|---------|
| Need K | No K Required |
| Spherical Clusters | Arbitrary Shapes |
| Sensitive to Outliers | Handles Outliers |

---

# 2. Association Rule Learning

## Definition

Association Rule Learning discovers relationships between items that frequently occur together.

Question:

"If a customer buys Product A, what else is likely to be purchased?"

---

## Example

Customer 1

Bread

Milk

Butter

Customer 2

Bread

Butter

Jam

Customer 3

Milk

Bread

Machine discovers

```
Bread

↓

Butter
```

This is called an **Association Rule**.

---

# Market Basket Analysis

Market Basket Analysis studies customer transactions to discover product combinations.

Purpose

- Increase Sales
- Improve Product Placement
- Build Recommendation Systems

Example

If customers buying

Laptop

also buy

Mouse

then place them nearby or recommend the mouse online.

---

# Beer & Diapers Story

One of the most famous stories in Data Mining is the Beer & Diapers example.

### Story

A retailer analyzed customer transactions.

They noticed that customers buying diapers were also buying beer more often than expected.

The retailer used this information for better shelf placement and promotions.

> **Important Interview Note**
>
> The historical accuracy of every detail of this story is debated, but it remains one of the best examples for explaining Association Rule Learning and Market Basket Analysis.

---

## Important Terms

### Support

How frequently an itemset appears in the dataset.

### Confidence

How often Rule B is true when Rule A is true.

### Lift

Measures whether the relationship is stronger than random chance.

> Interview Tip:
>
> Lift > 1 indicates a positive association.

---

## Popular Algorithms

- Apriori
- FP-Growth
- ECLAT

---

# 3. Dimensionality Reduction

## Definition

Real-world datasets may contain hundreds or even thousands of features.

Many features are:

- Redundant
- Highly Correlated
- Noisy

Dimensionality Reduction reduces the number of features while preserving most of the useful information.

---

## Why Is It Needed?

Imagine a retail dataset with

- Product ID
- Brand
- Category
- Supplier
- Region
- State
- City
- Temperature
- Holiday
- Promotion
- Inventory
- Competitor Price
- ... (200+ features)

Training directly on all features can:

- Increase computation time.
- Cause overfitting.
- Reduce interpretability.

Instead, we transform the data into fewer informative dimensions.

---

## Benefits

- Faster Training
- Less Storage
- Better Visualization
- Reduced Noise
- Reduced Multicollinearity
- Can improve model performance

---

## PCA (Principal Component Analysis)

PCA is the most widely used Dimensionality Reduction technique.

It creates **new features**, called **Principal Components**, that capture the maximum variance in the data.

### Key Points

- Components are orthogonal (uncorrelated).
- First component captures the maximum variance.
- Second captures the remaining variance, and so on.

Interview Tip:

PCA is a **feature extraction** technique, not simply feature selection.

---

## t-SNE (t-Distributed Stochastic Neighbor Embedding)

t-SNE is mainly used for **visualization**.

It projects high-dimensional data into 2D or 3D while preserving local neighborhood relationships.

### Where is it used?

- Data Visualization
- Cluster Inspection
- Embedding Visualization

### Interview Tip

t-SNE is **not** typically used for model training because it is computationally expensive and does not preserve global distances well.

---

# MNIST Visualization

MNIST contains handwritten digits (0–9).

Each image is 28 × 28 pixels.

This means every image has **784 features**.

Humans cannot visualize data in 784 dimensions.

Using PCA or t-SNE, these 784-dimensional points can be projected into **2D**, where digits with similar shapes naturally cluster together.

This makes it much easier to inspect the data visually.

---

# PCA vs t-SNE

| PCA | t-SNE |
|------|--------|
| Linear | Non-linear |
| Faster | Slower |
| Good for preprocessing | Good for visualization |
| Preserves variance | Preserves local neighborhoods |

---

# 4. Anomaly Detection

## Definition

Anomaly Detection identifies observations that are significantly different from the majority of the data.

These observations are called:

- Outliers
- Anomalies
- Rare Events

---

## Examples

- Credit Card Fraud
- Cyber Attacks
- Manufacturing Defects
- Medical Abnormalities
- Retail Sales Outliers

---

## Retail Example

Daily Sales

```
210

215

205

220

210

218
```

Suddenly

```
3500
```

Possible Reasons

- Festival
- Flash Sale
- Data Entry Error
- Fraud

Anomaly Detection flags this observation for investigation.

---

## Popular Algorithms

- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- DBSCAN (can identify noise points)

---

# Interview Questions

### What is Unsupervised Learning?

Learning from unlabeled data to discover hidden patterns.

---

### Name the common tasks in Unsupervised Learning.

- Clustering
- Association Rule Learning
- Dimensionality Reduction
- Anomaly Detection

---

### Why is Customer Segmentation Unsupervised?

Because there are no predefined labels.

---

### Difference Between PCA and t-SNE?

PCA is mainly used for feature extraction and dimensionality reduction.

t-SNE is mainly used for visualization.

---

### Which algorithm is commonly used for Market Basket Analysis?

- Apriori
- FP-Growth

---

### Which algorithm detects anomalies?

- Isolation Forest
- One-Class SVM
- LOF

---

# Common Interview Traps

❌ Customer Segmentation → Classification

✅ Clustering

---

❌ PCA removes useless columns.

✅ PCA creates new components from existing features.

---

❌ t-SNE is mainly for model training.

✅ t-SNE is mainly for visualization.

---

❌ Beer & Diapers is a Clustering example.

✅ It is an Association Rule Learning example.

---

# Key Takeaways

- Unsupervised Learning works without labels.
- Clustering groups similar observations.
- Association Rule Learning discovers relationships between items.
- Market Basket Analysis is a business application of Association Rules.
- PCA reduces dimensions while preserving variance.
- t-SNE is primarily for visualization.
- Anomaly Detection identifies unusual observations.

---

# What's Coming in Part 3?

- Semi-Supervised Learning
- Reinforcement Learning
- Complete ML Comparison
- Retail Forecasting Mapping
- Python Examples
- Industry Notes
- Interview Cheat Sheet

# Day 3 - Types of Machine Learning (Part 3)

> Topics Covered
>
> - Semi-Supervised Learning
> - Reinforcement Learning
> - Complete Comparison of ML Types
> - Choosing the Right Machine Learning Approach
> - Retail Forecasting Mapping
> - Industry Use Cases
> - Python Examples
> - Interview Questions
> - Common Mistakes

---

# 3. Semi-Supervised Learning

## Definition

Semi-Supervised Learning is a Machine Learning paradigm where the model is trained using:

- A **small amount of labeled data**
- A **large amount of unlabeled data**

It lies between Supervised Learning and Unsupervised Learning.

---

## Why Do We Need Semi-Supervised Learning?

Labeling data is expensive.

Imagine building a model for skin disease detection.

Suppose you have:

- 10,000 medical images

But only

- 500 images are labeled by doctors.

Getting labels for the remaining 9,500 images may cost lakhs of rupees and months of effort.

Instead of ignoring them, Semi-Supervised Learning learns from both labeled and unlabeled data.

---

# Intuition

Imagine a classroom.

Teacher solves only five questions.

Students then solve the remaining fifty by observing those examples.

That is exactly how Semi-Supervised Learning works.

---

# Diagram

```
Dataset

│

├── Small Labeled Data

└── Large Unlabeled Data

↓

Model learns from both

↓

Better Accuracy
```

---

# Where Is It Used?

- Face Recognition
- Speech Recognition
- Medical Imaging
- Document Classification
- Image Classification
- OCR Systems
- Satellite Image Analysis

---

# Retail Example

Suppose an e-commerce company has

10 million product images.

Only

50,000

have proper categories.

Instead of manually labeling every product,

the model learns from

- labeled products

+

- unlabeled products.

---

# Advantages

- Requires fewer labeled samples.
- Reduces labeling cost.
- Improves accuracy over pure supervised learning when labels are scarce.
- Makes use of abundant unlabeled data.

---

# Limitations

- Poor-quality labeled data can mislead the model.
- Incorrect pseudo-labels may propagate errors.
- More complex than standard supervised learning.

---

# Popular Techniques

- Self-Training
- Label Propagation
- Label Spreading
- Pseudo Labeling
- Consistency Regularization

---

# Interview Question

### Why not use only Supervised Learning?

Because collecting labeled data is expensive and time-consuming.

Semi-Supervised Learning makes use of the large amount of unlabeled data that organizations already have.

---

# 4. Reinforcement Learning

## Definition

Reinforcement Learning (RL) is a Machine Learning paradigm in which an **agent learns by interacting with an environment**.

Instead of learning from labeled examples, the agent learns through **trial and error**.

Correct actions receive **rewards**.

Incorrect actions receive **penalties**.

The goal is to maximize the total reward over time.

---

# Everyday Analogy

Think about teaching a child to ride a bicycle.

No one gives a labeled dataset.

The child:

- Tries
- Falls
- Learns
- Improves

Eventually, the child rides successfully.

That is Reinforcement Learning.

---

# Components of Reinforcement Learning

```
Agent

↓

Takes Action

↓

Environment

↓

Reward / Penalty

↓

Agent Learns

↓

Better Action
```

---

# Important Terminology

### Agent

The learner or decision-maker.

Example:

A robot.

---

### Environment

The world in which the agent operates.

Example:

Road, Game Board, Warehouse.

---

### State

The current situation.

Example:

Current board position in Chess.

---

### Action

The decision taken by the agent.

Example:

Move left.

Move right.

Accelerate.

Brake.

---

### Reward

Feedback received after taking an action.

Positive reward encourages the action.

Negative reward discourages the action.

---

### Policy

A strategy that tells the agent what action to take in each state.

---

# Example: Self-Driving Car

State

↓

Traffic Signal

↓

Action

↓

Brake

↓

Reward

↓

Safe Driving

---

# Example: Chess AI

State

↓

Current Board

↓

Action

↓

Move Queen

↓

Reward

↓

Win Probability Increases

---

# Applications

- Robotics
- Self-Driving Cars
- Chess Engines
- Recommendation Systems
- Dynamic Pricing
- Resource Allocation
- Traffic Signal Optimization
- Game AI

---

# Retail Example

Suppose an online shopping platform wants to maximize profit.

The system experiments with:

- 5% Discount
- 10% Discount
- 15% Discount

Over time it learns

which discount gives the highest long-term profit.

This is Reinforcement Learning.

---

# Popular Algorithms

- Q-Learning
- SARSA
- Deep Q Network (DQN)
- Policy Gradient
- PPO (Proximal Policy Optimization)
- Actor-Critic

---

# Comparison of Machine Learning Types

| Learning Type | Labeled Data | Goal | Example |
|--------------|-------------|------|---------|
| Supervised | ✅ Yes | Predict Output | Sales Forecasting |
| Unsupervised | ❌ No | Discover Patterns | Customer Segmentation |
| Semi-Supervised | Partial | Use Few Labels + Many Unlabeled | Image Classification |
| Reinforcement | Reward Signal | Learn Best Actions | Self-Driving Cars |

---

# Which Machine Learning Technique Should You Choose?

## Use Supervised Learning When

- Target variable is available.
- Prediction is required.
- Historical labeled data exists.

Examples

- House Price Prediction
- Sales Forecasting
- Churn Prediction

---

## Use Unsupervised Learning When

- No labels are available.
- Hidden patterns need to be discovered.
- Customer segmentation is required.

---

## Use Semi-Supervised Learning When

- Labels are expensive.
- Large unlabeled datasets exist.
- Small labeled datasets are available.

---

## Use Reinforcement Learning When

- Sequential decision-making is required.
- Rewards and penalties are available.
- Long-term optimization matters.

---

# Retail Sales Forecasting Mapping

Let's connect today's concepts with our Retail Sales Forecasting project.

### Supervised Learning

Predict future sales.

Example

```
Tomorrow Sales = 250 Units
```

This is Regression.

---

### Unsupervised Learning

Group stores based on sales patterns.

Example

```
Premium Stores

Budget Stores

Seasonal Stores
```

---

### Association Rule Learning

Discover products frequently purchased together.

Example

```
Bread

↓

Butter
```

---

### Dimensionality Reduction

Reduce 200 sales-related features into a smaller informative set before training.

---

### Anomaly Detection

Detect unusual sales.

Example

Store usually sells

200 Units

Suddenly

3000 Units

↓

Possible Fraud

---

### Semi-Supervised Learning

Only some products have categories.

The remaining products are automatically categorized using both labeled and unlabeled data.

---

### Reinforcement Learning

An online retailer adjusts discounts dynamically.

The system learns which pricing strategy maximizes long-term revenue.

---

# Python Examples

## K-Means Clustering

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)

model.fit(X)
```

---

## PCA

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_new = pca.fit_transform(X)
```

---

## Isolation Forest

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest()

model.fit(X)
```

---

## Q-Learning (Conceptual)

```python
Q[state, action] = reward + gamma * max(Q[next_state])
```

---

# Common Interview Questions

### Explain the four major Machine Learning paradigms.

---

### Difference between Supervised and Semi-Supervised Learning?

---

### Why is Customer Segmentation not a Classification problem?

---

### Why is Reinforcement Learning suitable for robotics?

---

### What is the role of rewards in Reinforcement Learning?

---

### Give one retail use case of each learning paradigm.

---

# Common Interview Traps

❌ Reinforcement Learning requires labeled data.

✅ RL learns through rewards.

---

❌ Semi-Supervised means 50% labeled data.

✅ There is no fixed ratio.

---

❌ PCA removes columns.

✅ PCA creates new transformed features.

---

❌ Customer Segmentation is Classification.

✅ It is Clustering.

---

# Revision Cheat Sheet

```
Machine Learning

│

├── Supervised
│      ├── Regression
│      └── Classification
│
├── Unsupervised
│      ├── Clustering
│      ├── Association Rule Learning
│      ├── Dimensionality Reduction
│      └── Anomaly Detection
│
├── Semi-Supervised
│
└── Reinforcement Learning
```

---

# Key Takeaways

- Semi-Supervised Learning combines labeled and unlabeled data.
- Reinforcement Learning learns through rewards and penalties.
- Choosing the correct learning paradigm depends on the problem and available data.
- A single business problem may involve multiple Machine Learning paradigms.
- Understanding **when** to use each approach is as important as understanding **how** it works.

---

# What's Coming in Part 4?

- Machine Learning Decision Flowchart
- Memory Tricks
- FAQs
- Advanced Interview Questions
- Common Myths
- Beyond CampusX Notes
- Best Practices
- Revision Sheet
- References
- Final Coverage Checklist
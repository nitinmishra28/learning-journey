# Day 3 - Types of Machine Learning

> **Course:** CampusX – 100 Days of Machine Learning
> **Notes By:** Nitin Mishra
> **Purpose:** Learning + Interview Preparation + Project Revision

---

# 🎯 Learning Objectives

After this lecture you should be able to:

* Understand the major types of Machine Learning.
* Differentiate between Supervised, Unsupervised and Reinforcement Learning.
* Differentiate Regression and Classification.
* Understand different types of Unsupervised Learning.
* Select the correct ML approach for a real-world problem.
* Answer common interview questions.

---

# Why Do We Need Different Types of Machine Learning?

Not every dataset looks the same.

Sometimes we already know the correct answer.

Sometimes we only have raw data.

Sometimes a machine has to learn by interacting with an environment.

Because of these different situations, Machine Learning is divided into different categories.

```
Machine Learning

├── Supervised Learning
├── Unsupervised Learning
└── Reinforcement Learning
```

---

# 1. Supervised Learning

## Definition

Supervised Learning is a Machine Learning technique where the dataset contains:

* Input Features (X)
* Correct Output (Y)

The model learns the relationship between them and predicts outputs for unseen data.

Think of it as learning under the supervision of a teacher who already knows the correct answers.

### Example

| Hours Studied | Marks |
| ------------- | ----: |
| 2             |    40 |
| 4             |    65 |
| 6             |    85 |

Input → Hours Studied

Output → Marks

The model learns the relationship and predicts marks for new students.

---

## Real World Applications

* House Price Prediction
* Salary Prediction
* Loan Approval
* Disease Prediction
* Sales Forecasting
* Email Spam Detection

---

# Types of Supervised Learning

```
Supervised Learning

├── Regression
└── Classification
```

---

## Regression

### Definition

Regression predicts continuous numerical values.

Think:

**"How Much?"**

Examples

* House Price
* Sales
* Temperature
* Salary
* Electricity Consumption

### Popular Algorithms

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

---

## Classification

### Definition

Classification predicts categories or classes.

Think:

**"Which Class?"**

Examples

* Spam / Not Spam
* Fraud / Genuine
* Diabetes / No Diabetes
* Pass / Fail

### Popular Algorithms

* Logistic Regression
* Decision Tree
* Random Forest
* SVM
* Naive Bayes
* KNN

---

## Regression vs Classification

| Regression        | Classification          |
| ----------------- | ----------------------- |
| Predicts Numbers  | Predicts Categories     |
| Continuous Output | Discrete Output         |
| Example: Sales    | Example: Spam Detection |

---

# Retail Sales Forecasting Example

Features

* Product
* Store
* Discount
* Holiday
* Weather
* Previous Sales

Target

**Next Month Sales**

Since the target is numerical, Retail Sales Forecasting is generally a **Supervised Regression** problem.

---

# 2. Unsupervised Learning

## Definition

In Unsupervised Learning, the dataset contains only input features.

There is **no target column**.

The model automatically discovers hidden patterns.

Think of giving someone a box of mixed objects without labels and asking them to organize similar objects together.

---

# Types of Unsupervised Learning

```
Unsupervised Learning

├── Clustering
├── Association Rule Learning
├── Dimensionality Reduction
└── Anomaly Detection
```

---

# A. Clustering

## Definition

Clustering groups similar data points together.

No labels are provided.

The algorithm itself discovers natural groups.

### Applications

* Customer Segmentation
* Image Segmentation
* Document Clustering
* News Grouping

### Popular Algorithms

* K-Means
* Hierarchical Clustering
* DBSCAN

### Retail Example

A supermarket has one million customers.

The company doesn't know who is

* Premium
* Budget
* Regular

The algorithm automatically creates these customer groups.

---

# B. Association Rule Learning

## Definition

Association Rule Learning discovers relationships between items that frequently occur together.

It answers the question:

**"If a customer buys X, what else are they likely to buy?"**

### Classic Example

Bread → Butter

Milk → Bread

Bread + Butter → Jam

### Business Applications

* Product Recommendations
* Cross Selling
* Grocery Basket Analysis
* E-commerce Recommendations

### Popular Algorithms

* Apriori
* FP-Growth

### Beer & Diapers Case Study

One of the most famous examples of Association Rule Learning is the **Beer and Diapers** story.

The idea is that transaction data can reveal products that are frequently purchased together, allowing stores to improve product placement and marketing campaigns.

> **Interview Note:** Whether every detail of the original story is historically accurate is debated, but it remains an excellent illustration of Market Basket Analysis.

---

# C. Dimensionality Reduction

## Definition

Real-world datasets often contain hundreds or thousands of features.

Many features are redundant or highly correlated.

Dimensionality Reduction reduces the number of features while preserving most of the useful information.

### Benefits

* Faster Training
* Better Visualization
* Lower Memory Usage
* Reduced Noise
* Can reduce overfitting

### Popular Algorithms

* PCA (Principal Component Analysis)
* t-SNE
* UMAP

### MNIST Visualization

The famous **MNIST handwritten digit dataset** contains images represented in high-dimensional space.

Using techniques like **t-SNE**, these high-dimensional images can be projected into 2D, making clusters of handwritten digits visible.

This demonstrates why Dimensionality Reduction is valuable—not just for speeding up models, but also for understanding data visually.

---

# D. Anomaly Detection

## Definition

Anomaly Detection identifies observations that behave very differently from the majority of the data.

These unusual observations are called:

* Outliers
* Anomalies
* Exceptions

### Examples

* Credit Card Fraud
* Network Intrusion
* Manufacturing Defects
* Medical Diagnosis
* Server Monitoring

### Retail Example

Suppose daily sales are:

210

225

205

215

220

Suddenly one day:

3500

The model flags this observation because it is significantly different from normal sales.

Possible reasons:

* Festival
* Flash Sale
* Data Entry Error
* Fraud

### Popular Algorithms

* Isolation Forest
* One-Class SVM
* Local Outlier Factor (LOF)

> **Beyond Lecture:** Isolation Forest is one of the most commonly used anomaly detection algorithms in industry interviews.

---

# 3. Reinforcement Learning

## Definition

Reinforcement Learning is a learning technique where an **Agent** interacts with an **Environment**.

Based on its actions, it receives:

* Reward
* Penalty

The objective is to maximize long-term rewards.

### Applications

* Self Driving Cars
* Robotics
* Chess
* Go
* Recommendation Optimization

---

# Choosing the Right Machine Learning Type

| Question                                | Technique              |
| --------------------------------------- | ---------------------- |
| Do you have labeled outputs?            | Supervised Learning    |
| Need to discover hidden patterns?       | Unsupervised Learning  |
| Learning through rewards and penalties? | Reinforcement Learning |

---

# Python Example

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

# Clustering
kmeans = KMeans(n_clusters=3)

# Dimensionality Reduction
pca = PCA(n_components=2)

# Anomaly Detection
model = IsolationForest(random_state=42)
```

---

# Common Interview Questions

### What are the three major types of Machine Learning?

* Supervised Learning
* Unsupervised Learning
* Reinforcement Learning

---

### What are the two types of Supervised Learning?

* Regression
* Classification

---

### What are the four common types of Unsupervised Learning?

* Clustering
* Association Rule Learning
* Dimensionality Reduction
* Anomaly Detection

---

### Why is Sales Forecasting a Regression problem?

Because the target variable (future sales) is a continuous numerical value.

---

### Why is Customer Segmentation an Unsupervised Learning problem?

Because there are no predefined labels; the algorithm discovers groups automatically.

---

### What is the difference between Clustering and Classification?

| Clustering   | Classification         |
| ------------ | ---------------------- |
| No Labels    | Labels Available       |
| Finds Groups | Predicts Known Classes |

---

# Common Interview Traps

❌ Spam Detection → Regression

✅ Classification

---

❌ Customer Segmentation → Supervised Learning

✅ Unsupervised Learning

---

❌ House Price Prediction → Classification

✅ Regression

---

❌ Market Basket Analysis → Clustering

✅ Association Rule Learning

---

# Key Takeaways

* Machine Learning is divided into Supervised, Unsupervised and Reinforcement Learning.
* Supervised Learning requires labeled data.
* Regression predicts numbers.
* Classification predicts categories.
* Unsupervised Learning includes Clustering, Association Rule Learning, Dimensionality Reduction and Anomaly Detection.
* Reinforcement Learning learns through rewards and penalties.

---

# 30-Second Revision

```
Machine Learning
│
├── Supervised
│   ├── Regression
│   └── Classification
│
├── Unsupervised
│   ├── Clustering
│   ├── Association
│   ├── Dimensionality Reduction
│   └── Anomaly Detection
│
└── Reinforcement Learning
```

---

# Further Reading

* Visualizing high-dimensional data using t-SNE with the MNIST dataset (helps build intuition for Dimensionality Reduction).
* Beer & Diapers / Market Basket Analysis (understanding Association Rule Learning in retail).

---

# Coverage Checklist

✅ Supervised Learning
✅ Regression
✅ Classification
✅ Unsupervised Learning
✅ Clustering
✅ Association Rule Learning
✅ Dimensionality Reduction
✅ Anomaly Detection
✅ Reinforcement Learning
✅ Retail Examples
✅ Python Examples
✅ Interview Questions
✅ Common Interview Traps
✅ Revision Notes

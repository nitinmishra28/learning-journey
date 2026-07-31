# Day 2 - AI vs Machine Learning vs Deep Learning

## 🎯 Learning Objective

In this lecture, we will understand:

- What is Artificial Intelligence (AI)?
- What is Machine Learning (ML)?
- What is Deep Learning (DL)?
- Relationship between AI, ML, and DL
- Real-world applications
- Which one should you learn?

---

# Artificial Intelligence (AI)

Artificial Intelligence is the broad field of making machines perform tasks that normally require human intelligence.

AI aims to make computers capable of:

- Thinking
- Learning
- Reasoning
- Problem Solving
- Decision Making
- Understanding Language
- Recognizing Images

AI does **not always** require Machine Learning.

Example:

- Chess Engine
- Rule-Based Expert System
- Chatbots
- Robotics

---

# Machine Learning (ML)

Machine Learning is a subset of Artificial Intelligence.

Instead of manually writing rules, machines learn patterns from historical data.

Example

Input

```
Customer Data
```

↓

Machine learns

↓

```
Will customer buy or not?
```

Examples

- House Price Prediction
- Spam Detection
- Sales Forecasting
- Recommendation Systems

---

# Deep Learning (DL)

Deep Learning is a subset of Machine Learning.

Instead of manually creating features, Deep Learning automatically learns features using Neural Networks.

It performs extremely well when working with

- Images
- Videos
- Audio
- Text

Examples

- Face Recognition
- Self Driving Cars
- ChatGPT
- Voice Assistant

---

# Relationship

```
Artificial Intelligence

        │

Machine Learning

        │

Deep Learning
```

Think of it like this:

```
Universe
   ↓
Earth
   ↓
India
```

or

```
Vehicle
   ↓
Car
   ↓
Electric Car
```

AI is the biggest field.

ML is inside AI.

DL is inside ML.

---

# Traditional Programming vs Machine Learning

Traditional Programming

```
Data + Rules

↓

Output
```

Example

```python
if marks >= 90:
    print("A Grade")
```

Everything is manually programmed.

---

Machine Learning

```
Data + Correct Output

↓

Machine Learns Rules

↓

Prediction
```

No manual rules are required.

---

# Why Deep Learning?

Machine Learning struggles when

- Data is huge
- Features are complex
- Images are involved
- Audio is involved
- Natural language is involved

Deep Learning automatically extracts useful features.

Example

Machine Learning

```
Cat Detection

↓

Need to manually create features
```

Deep Learning

```
Image

↓

Neural Network

↓

Cat Detected
```

---

# Real World Applications

## Artificial Intelligence

- Robotics
- Virtual Assistants
- Rule-Based Systems
- Smart Homes

---

## Machine Learning

- Demand Forecasting
- Fraud Detection
- Recommendation Systems
- Stock Prediction
- Disease Prediction

---

## Deep Learning

- Image Classification
- Face Unlock
- ChatGPT
- Speech Recognition
- Object Detection
- Medical Image Analysis

---

# Retail Sales Forecasting Example

Suppose a supermarket wants to predict next month's sales.

Features

- Product
- Store
- Festival
- Discount
- Previous Sales

Target

```
Next Month Sales
```

This is a Machine Learning problem.

---

Now suppose the company wants to detect damaged products using camera images.

Images

↓

Neural Network

↓

Damaged / Not Damaged

This becomes a Deep Learning problem.

---

# AI vs ML vs DL

| Feature | AI | ML | DL |
|----------|----|----|----|
| Definition | Making machines intelligent | Learning from data | Learning using Neural Networks |
| Requires Data | Sometimes | Yes | Large Amount |
| Manual Feature Engineering | Yes | Yes | No |
| Image Processing | Limited | Moderate | Excellent |
| Training Time | Low | Medium | High |
| Hardware Requirement | Low | Medium | High (GPU) |

---

# Advantages

## AI

- Automates tasks
- Decision making
- Intelligent systems

---

## ML

- Learns patterns
- Improves over time
- Handles complex data

---

## DL

- Highest accuracy
- Learns automatically
- Excellent for images, audio and NLP

---

# Limitations

## AI

- Can become rule-heavy
- Difficult to scale manually

---

## ML

- Needs quality data
- Manual feature engineering

---

## DL

- Huge amount of data required
- Requires GPUs
- Longer training time
- Harder to interpret

---

# Python Libraries

Machine Learning

```python
import sklearn
```

Deep Learning

```python
import tensorflow as tf

# or

import torch
```

---

# Which One Should You Learn?

If you are a beginner

↓

Learn Python

↓

Machine Learning

↓

Deep Learning

Never start directly with Deep Learning.

---

# Interview Questions

### What is Artificial Intelligence?

AI is the science of making machines capable of performing tasks that require human intelligence.

---

### What is Machine Learning?

Machine Learning is a subset of AI where machines learn patterns from historical data.

---

### What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses Neural Networks with multiple layers to learn complex patterns.

---

### Why is Deep Learning more powerful?

Because it automatically learns features from raw data and performs well on unstructured data like images, text, and audio.

---

### Can AI exist without Machine Learning?

Yes.

Rule-based expert systems are examples of AI without Machine Learning.

---

# Key Takeaways

✅ AI is the parent field.

✅ Machine Learning is a subset of AI.

✅ Deep Learning is a subset of Machine Learning.

✅ ML is best for structured/tabular data.

✅ DL is best for images, text, audio, and videos.

✅ Retail Sales Forecasting is a Machine Learning problem.

✅ Face Recognition is a Deep Learning problem.

---

# Revision (1 Minute)

✔ AI = Intelligence

✔ ML = Learning from Data

✔ DL = Neural Networks

AI ⊃ ML ⊃ DL

ML → Structured Data

DL → Unstructured Data

---

# Next Lecture

➡️ Types of Machine Learning

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
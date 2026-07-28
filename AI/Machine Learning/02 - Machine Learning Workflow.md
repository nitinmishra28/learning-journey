# 02 - Machine Learning Workflow

In the previous lecture, we learned that a Machine Learning model learns patterns from historical data.

Now let's understand the complete workflow of a Machine Learning project and identify where the actual AI happens.

---

# Complete Workflow

```
CSV File
   │
   ▼
Read Data (Pandas)
   │
   ▼
Clean Data
   │
   ▼
Select Features (X) and Target (y)
   │
   ▼
Train Machine Learning Model
   │
   ▼
Save Model
   │
   ▼
Load Model
   │
   ▼
Predict on New Data
```

---

# Step 1 - Read Data

Usually, data is stored in a CSV file.

Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")
```

What happens here?

- Pandas opens the CSV file.
- Reads all rows and columns.
- Converts them into a DataFrame.

At this stage,

❌ No AI is involved.

It is simply reading data from disk into memory.

Think of it like opening an Excel sheet.

---

# Step 2 - Data Cleaning

Real-world data is never perfect.

Common problems:

- Missing values
- Duplicate rows
- Wrong data types
- Invalid values

Example

```python
df.drop_duplicates()
df.fillna(0)
```

Again,

❌ No AI is involved.

These are normal data processing operations.

---

# Step 3 - Select Features and Target

Example Dataset

| Price | Discount | Store | Quantity Sold |
|--------|-----------|--------|---------------|
|50|10|Delhi|120|

Features (X)

- Price
- Discount
- Store

Target (y)

- Quantity Sold

Example

```python
X = df[["Price", "Discount", "Store"]]
y = df["Quantity Sold"]
```

Still,

❌ No AI is involved.

We are only preparing data.

---

# Step 4 - Train the Model

This is where Machine Learning starts.

Example

```python
model.fit(X, y)
```

This single line performs the learning process.

During training,

the algorithm studies thousands (or millions) of examples and finds mathematical relationships between Features (X) and Target (y).

This is the actual AI part.

```
Historical Data

↓

Model learns patterns

↓

Trained Model
```

---

# What is Actually Stored Inside the Model?

The model does NOT store the entire dataset.

Instead, it stores learned mathematical parameters.

Example

```
Input

Price = 45
Discount = 20%

↓

Model

↓

Expected Sales = 170
```

The model remembers the relationship, not every row.

---

# Step 5 - Save the Model

Once training is complete,

the model can be saved.

Example

```python
joblib.dump(model, "sales_model.pkl")
```

Now we don't need to train again every time.

---

# Step 6 - Load the Model

Later,

we simply load the trained model.

Example

```python
model = joblib.load("sales_model.pkl")
```

Still,

❌ No AI is happening.

We are only loading an already trained model.

---

# Step 7 - Prediction

Example

```python
model.predict(new_data)
```

Input

```
Price = 45
Discount = 20%
Weekend = Yes
```

Output

```
Predicted Sales = 170
```

Prediction uses the knowledge learned during training.

---

# Where Does AI Actually Happen?

| Step | AI Involved? |
|------|--------------|
| Read CSV | ❌ No |
| Data Cleaning | ❌ No |
| Feature Selection | ❌ No |
| Train Model (`fit()`) | ✅ Yes |
| Save Model | ❌ No |
| Load Model | ❌ No |
| Prediction (`predict()`) | ✅ Uses Learned AI |

---

# Understanding `fit()`

During training,

```
X (Features)

+

y (Target)

↓

fit()

↓

Model Learns Patterns
```

Example

```
Price = 50
Discount = 10%

↓

Sales = 120
```

After seeing thousands of such examples,

the model understands how Price and Discount affect Sales.

---

# Understanding `predict()`

During prediction,

the target is NOT provided.

```
New Features

↓

predict()

↓

Predicted Target
```

Example

```
Price = 45
Discount = 20%

↓

170 Units
```

---

# Why Don't We Train Every Time?

Training can take

- Minutes
- Hours
- Days

depending on the dataset and algorithm.

Therefore,

we train once,

save the model,

and reuse it many times.

---

# Real-Life Retail Forecasting Workflow

```
Historical Sales Data

↓

Read CSV

↓

Clean Data

↓

Train Model

↓

Save Model

↓

Deploy

↓

User enters

Price
Discount
Store

↓

Predict Sales
```

---

# Common Misconception

Many beginners think this is AI:

```python
df = pd.read_csv(...)
```

It is NOT.

Reading files is normal programming.

The AI begins when the model starts learning patterns during

```python
model.fit(X, y)
```

---

# Key Points

- Pandas is a data processing library.
- Reading CSV is not AI.
- Cleaning data is not AI.
- Feature selection is not AI.
- `fit()` is where learning happens.
- `predict()` uses the learned knowledge.
- A trained model stores mathematical relationships, not the original dataset.

---

# Interview Questions

### Is Pandas an AI library?

No.

Pandas is a data analysis and manipulation library.

---

### Which line performs Machine Learning?

```python
model.fit(X, y)
```

---

### Does `predict()` train the model?

No.

It only uses the already trained model.

---

### Why do we save the model?

To avoid retraining every time and use the learned knowledge for future predictions.

---

### Does the model store the dataset?

No.

The model stores learned mathematical parameters (patterns), not the entire dataset.

---

# Revision

```
Read CSV
   ↓
Clean Data
   ↓
Features (X)
Target (y)
   ↓
fit()
   ↓
Trained Model
   ↓
Save
   ↓
Load
   ↓
predict()
   ↓
Prediction
```
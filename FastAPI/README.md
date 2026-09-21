# FastAPI — Lecture 1: Introduction

## 1. What is FastAPI?

**FastAPI** is a modern Python web framework used to build **APIs and backend applications**.

It is built on top of:

* **Starlette** → Web framework functionality
* **Pydantic** → Data validation and serialization
* **Uvicorn** → ASGI server used to run FastAPI applications

Simple way to remember:

```text
FastAPI
   ↓
Build APIs using Python
   ↓
Client → API → Backend Logic → Database
```

---

## 2. What is an API?

API stands for:

> **Application Programming Interface**

An API allows two applications to communicate with each other.

For example:

```text
React Frontend
      ↓
   HTTP Request
      ↓
   FastAPI Backend
      ↓
    Database
      ↓
   FastAPI Backend
      ↓
   HTTP Response
      ↓
React Frontend
```

Example:

```text
GET /users
```

The frontend asks the backend:

> Give me the users.

FastAPI processes the request and returns data.

---

## 3. Why FastAPI?

FastAPI is popular because it provides:

* High performance
* Automatic request validation
* Automatic API documentation
* Type hints
* Async support
* Dependency Injection
* Easy integration with databases
* Easy authentication implementation
* Clean API development

---

## 4. FastAPI vs Flask

Both can be used to build APIs, but their approach is different.

| Feature              | FastAPI             | Flask                                 |
| -------------------- | ------------------- | ------------------------------------- |
| Language             | Python              | Python                                |
| API development      | Excellent           | Good                                  |
| Type hints           | Strongly integrated | Not built-in                          |
| Validation           | Pydantic            | Usually requires additional libraries |
| Automatic API docs   | Yes                 | Usually requires additional setup     |
| Async support        | Built-in            | More limited / different approach     |
| Performance          | High                | Good                                  |
| Dependency Injection | Built-in            | Not built-in                          |

For modern Python API development, FastAPI provides many features out of the box.

---

# 5. ASGI vs WSGI

This is an important interview concept.

### WSGI

WSGI stands for:

> Web Server Gateway Interface

It is traditionally used by Python web frameworks such as Flask and Django.

### ASGI

ASGI stands for:

> Asynchronous Server Gateway Interface

FastAPI uses **ASGI**.

ASGI supports:

* Asynchronous programming
* `async` / `await`
* WebSockets
* Long-running connections

Simple flow:

```text
Client
  ↓
ASGI Server
  ↓
FastAPI
  ↓
Application Logic
```

---

# 6. What is Uvicorn?

**Uvicorn** is an ASGI server.

FastAPI is the framework.

Uvicorn runs the FastAPI application.

Think of it like:

```text
FastAPI = Application
Uvicorn = Server that runs the application
```

Example:

```bash
uvicorn main:app --reload
```

Here:

```text
main
 ↓
main.py

app
 ↓
FastAPI object

--reload
 ↓
Automatically restart when code changes
```

---

# 7. Installing FastAPI

Create a virtual environment first.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Check installation:

```bash
pip show fastapi
```

---

# 8. Your First FastAPI Application

Create:

```text
main.py
```

Code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

---

# 9. Understanding the Code

### Import FastAPI

```python
from fastapi import FastAPI
```

We import the `FastAPI` class.

---

### Create the application

```python
app = FastAPI()
```

This creates our FastAPI application object.

---

### Create an API endpoint

```python
@app.get("/")
```

This means:

> When a GET request comes to `/`, execute the function below it.

---

### Function

```python
def home():
    return {"message": "Hello FastAPI"}
```

The function returns a Python dictionary.

FastAPI converts it into JSON.

Response:

```json
{
    "message": "Hello FastAPI"
}
```

---

# 10. Run the Application

Run:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

Open:

```text
http://127.0.0.1:8000
```

You should get:

```json
{
    "message": "Hello FastAPI"
}
```

---

# 11. Automatic API Documentation

One of the biggest advantages of FastAPI is automatic documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive Swagger UI.

You can test your APIs directly from the browser.

There is also another documentation endpoint:

```text
http://127.0.0.1:8000/redoc
```

---

# 12. Basic FastAPI Project Structure

For now, keep it simple:

```text
fastapi-learning/
│
├── venv/
│
├── main.py
│
└── requirements.txt
```

Later, when we build real applications, we will move to a proper structure.

---

# 13. requirements.txt

You can save installed dependencies:

```bash
pip freeze > requirements.txt
```

Example:

```text
fastapi
uvicorn
```

The exact versions may also appear depending on your environment.

---

# 14. Important Terminology

Remember these terms:

| Term       | Meaning                                                |
| ---------- | ------------------------------------------------------ |
| FastAPI    | Python framework for building APIs                     |
| API        | Interface for application communication                |
| ASGI       | Interface used by asynchronous Python web applications |
| Uvicorn    | ASGI server                                            |
| Endpoint   | A specific API URL                                     |
| Route      | URL + HTTP method                                      |
| JSON       | Common format for API data                             |
| Swagger UI | Interactive API documentation                          |
| Pydantic   | Data validation library used by FastAPI                |

---

# 15. Interview Questions

### Q1. What is FastAPI?

FastAPI is a modern Python web framework used to build APIs and backend applications.

---

### Q2. Why is FastAPI fast?

FastAPI is built on **Starlette** and uses the **ASGI** standard. It supports asynchronous programming using `async` and `await`.

---

### Q3. What server is commonly used to run FastAPI?

**Uvicorn** is commonly used as the ASGI server for FastAPI.

---

### Q4. What is ASGI?

ASGI stands for **Asynchronous Server Gateway Interface**.

It provides a standard interface between asynchronous Python web applications and web servers.

---

### Q5. What is Pydantic?

Pydantic is used by FastAPI for **data validation, parsing, and serialization**.

We will study it properly in a later lecture.

---

### Q6. What is the difference between FastAPI and Uvicorn?

```text
FastAPI
    ↓
Web framework

Uvicorn
    ↓
ASGI server
```

FastAPI defines the application.

Uvicorn runs the application.

---

### Q7. What is `--reload`?

```bash
uvicorn main:app --reload
```

`--reload` automatically reloads the development server when code changes.

It is useful during development.

It should generally not be used as the production server configuration.

---

# 16. What You Should Remember

```text
FastAPI → Python framework

Starlette → Web/ASGI functionality

Pydantic → Data validation

Uvicorn → ASGI server

ASGI → Interface for async Python web applications

/docs → Swagger UI

/redoc → ReDoc documentation
```

Most important:

```text
FastAPI ≠ Uvicorn

FastAPI = Framework
Uvicorn = Server
```

---

# 17. Practice

Create a FastAPI application that returns:

```json
{
    "name": "Your Name",
    "role": "Backend Developer",
    "technology": "FastAPI"
}
```

Use:

```text
GET /
```

Then verify it using:

```text
http://127.0.0.1:8000
```

Also open:

```text
http://127.0.0.1:8000/docs
```

---

# Quick Revision

```text
What is FastAPI?
        ↓
Python framework for APIs
        ↓
Uses ASGI
        ↓
Commonly runs with Uvicorn
        ↓
Pydantic handles validation
        ↓
Automatic Swagger/ReDoc documentation
```

## Next Lecture

### Lecture 2 — Routes, HTTP Methods & Path Operations

We will learn:

* What is a route?
* GET
* POST
* PUT
* PATCH
* DELETE
* `@app.get()`
* `@app.post()`
* Path operations
* How request/response flow works
* Interview questions

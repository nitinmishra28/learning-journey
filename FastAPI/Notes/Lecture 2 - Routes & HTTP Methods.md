# FastAPI — Lecture 2: Routes & HTTP Methods

## 1. What is a Route?

A **route** tells FastAPI:

> When a particular HTTP request comes to a particular URL, which function should execute?

Example:

```python
@app.get("/users")
def get_users():
    return {"message": "All users"}
```

Here:

```text
GET + /users
      ↓
get_users()
      ↓
Response
```

---

## 2. What is a Path?

The part after the domain is called the **path**.

Example:

```text
http://127.0.0.1:8000/users
```

Here:

```text
http://127.0.0.1:8000
        ↓
     Base URL

/users
   ↓
 Path
```

Examples:

```text
/products
/orders
/students
/teachers
```

---

## 3. What is an HTTP Method?

HTTP methods tell the server **what operation we want to perform**.

The most important methods are:

```text
GET
POST
PUT
PATCH
DELETE
```

---

## 4. GET

`GET` is generally used to **retrieve data**.

Example:

```python
@app.get("/users")
def get_users():
    return {
        "users": ["Nitin", "Rahul", "Aman"]
    }
```

Request:

```text
GET /users
```

Response:

```json
{
    "users": ["Nitin", "Rahul", "Aman"]
}
```

Think:

```text
GET → Give me data
```

---

## 5. POST

`POST` is generally used to **create new data**.

Example:

```python
@app.post("/users")
def create_user():
    return {
        "message": "User created"
    }
```

Request:

```text
POST /users
```

Think:

```text
POST → Create something
```

We will learn how to receive data from the client using Pydantic models in a later lecture.

---

## 6. PUT

`PUT` is generally used to **update or replace an existing resource**.

Example:

```python
@app.put("/users/1")
def update_user():
    return {
        "message": "User updated"
    }
```

Request:

```text
PUT /users/1
```

Think:

```text
PUT → Update/replace a resource
```

---

## 7. PATCH

`PATCH` is generally used for a **partial update**.

Example:

```python
@app.patch("/users/1")
def update_user_name():
    return {
        "message": "User name updated"
    }
```

Think:

```text
PATCH → Partially update something
```

Example:

```text
User:

name     → Nitin
email    → nitin@example.com
age      → 25
```

If we only want to change:

```text
age → 26
```

PATCH is commonly used.

---

## 8. DELETE

`DELETE` is used to **delete a resource**.

Example:

```python
@app.delete("/users/1")
def delete_user():
    return {
        "message": "User deleted"
    }
```

Think:

```text
DELETE → Delete something
```

---

## 9. FastAPI Path Operation Decorators

FastAPI provides decorators for HTTP methods:

```python
@app.get()
@app.post()
@app.put()
@app.patch()
@app.delete()
```

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Home"}


@app.get("/users")
def get_users():
    return {"message": "Get users"}


@app.post("/users")
def create_user():
    return {"message": "Create user"}


@app.put("/users")
def update_user():
    return {"message": "Update user"}


@app.delete("/users")
def delete_user():
    return {"message": "Delete user"}
```

---

## 10. What is a Path Operation?

This is an important FastAPI term.

Consider:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

FastAPI calls this a **path operation**.

It consists of:

```text
@app.get("/users")
       ↓
HTTP method + path
       ↓
Path Operation
```

The function:

```python
def get_users():
```

is the function that handles that operation.

---

## 11. Why is it Called a Decorator?

This:

```python
@app.get("/users")
```

is a Python **decorator**.

It tells FastAPI:

> Register the function below as the handler for GET `/users`.

Example:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

The decorator connects:

```text
GET /users
    ↓
get_users()
```

---

## 12. Multiple Routes

A FastAPI application can have many routes.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Home"}


@app.get("/users")
def get_users():
    return {"message": "Users"}


@app.get("/products")
def get_products():
    return {"message": "Products"}


@app.get("/orders")
def get_orders():
    return {"message": "Orders"}
```

The API now has:

```text
GET /
GET /users
GET /products
GET /orders
```

---

## 13. Same Path with Different HTTP Methods

You can use the same path with different HTTP methods.

```python
@app.get("/users")
def get_users():
    return {"message": "Get users"}


@app.post("/users")
def create_user():
    return {"message": "Create user"}
```

This is completely valid.

Why?

Because these are different operations:

```text
GET  /users → Get users
POST /users → Create user
```

The combination of:

```text
HTTP Method + Path
```

identifies the operation.

---

## 14. REST API Example

Imagine a student management system.

We can have:

```text
GET    /students
POST   /students
GET    /students/{id}
PUT    /students/{id}
PATCH  /students/{id}
DELETE /students/{id}
```

Conceptually:

```text
GET /students
      ↓
Get all students

POST /students
      ↓
Create student

GET /students/10
      ↓
Get student 10

PUT /students/10
      ↓
Update student 10

PATCH /students/10
      ↓
Partially update student 10

DELETE /students/10
      ↓
Delete student 10
```

The `{id}` part will be covered properly in the next lecture on **Path Parameters**.

---

## 15. Complete Example

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


@app.get("/students")
def get_students():
    return {
        "message": "Get all students"
    }


@app.post("/students")
def create_student():
    return {
        "message": "Student created"
    }


@app.put("/students/1")
def update_student():
    return {
        "message": "Student updated"
    }


@app.patch("/students/1")
def partially_update_student():
    return {
        "message": "Student partially updated"
    }


@app.delete("/students/1")
def delete_student():
    return {
        "message": "Student deleted"
    }
```

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You can test all the endpoints from Swagger UI.

---

## 16. GET vs POST

This is commonly asked in interviews.

| GET | POST |
|---|---|
| Retrieve data | Create data |
| Usually no request body | Can contain request body |
| Should not modify server data | Can modify server data |
| `/users` | `/users` |

Example:

```text
GET /users
```

means:

> Give me users.

While:

```text
POST /users
```

means:

> Create a new user.

---

## 17. PUT vs PATCH

Another common interview question.

### PUT

Generally represents replacing/updating the resource as a whole.

```text
PUT /users/10
```

### PATCH

Generally represents a partial modification.

```text
PATCH /users/10
```

Example:

```text
PUT

name
email
age
address
```

You may send the complete updated representation.

With PATCH:

```text
PATCH

age
```

You may update only the required field.

---

## 18. Idempotency — Interview Concept

An operation is **idempotent** if repeating the same request produces the same intended final state.

Common HTTP semantics:

```text
GET     → Idempotent
PUT     → Idempotent
DELETE  → Idempotent
PATCH   → Depends on the operation
POST    → Generally not idempotent
```

Example:

```text
PUT /users/10
```

If the same update is sent multiple times, the final state can remain the same.

But repeatedly:

```text
POST /orders
```

may create multiple orders.

---

## 19. Important HTTP Methods to Remember

```text
GET
 ↓
Read

POST
 ↓
Create

PUT
 ↓
Replace / Update

PATCH
 ↓
Partial Update

DELETE
 ↓
Delete
```

---

## 20. Common Mistakes

### Mistake 1 — Forgetting the decorator

Wrong:

```python
def get_users():
    return {"users": []}
```

FastAPI doesn't know this should be an API endpoint.

Correct:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

---

### Mistake 2 — Confusing the method and path

```python
@app.get("/users")
```

This means:

```text
GET + /users
```

Not just `/users`.

---

### Mistake 3 — Using POST for everything

Don't automatically use:

```text
POST /get-users
POST /delete-user
POST /update-user
```

Use HTTP methods according to the operation.

Prefer:

```text
GET    /users
POST   /users
PUT    /users/{id}
PATCH  /users/{id}
DELETE /users/{id}
```

---

## 21. Interview Questions

### Q1. What is a path operation in FastAPI?

A path operation maps an HTTP method and URL path to a Python function.

Example:

```python
@app.get("/users")
def get_users():
    ...
```

---

### Q2. What is the difference between a route and a path?

A **path** is the URL portion such as:

```text
/users
```

A **route/path operation** includes the HTTP method and path:

```text
GET /users
```

---

### Q3. Can GET and POST use the same path?

Yes.

```python
@app.get("/users")
def get_users():
    ...


@app.post("/users")
def create_user():
    ...
```

They are different operations because their HTTP methods are different.

---

### Q4. What is the difference between PUT and PATCH?

```text
PUT   → Generally replaces/updates the resource
PATCH → Partially updates the resource
```

---

### Q5. What is the purpose of `@app.get()`?

It registers a Python function as the handler for a GET request at the specified path.

---

### Q6. What does this mean?

```python
@app.get("/users")
def get_users():
```

It means:

```text
GET /users
      ↓
get_users()
```

---

## 22. Quick Revision

```text
Route
 ↓
URL + HTTP Method

Path
 ↓
/users

HTTP Methods
 ↓
GET
POST
PUT
PATCH
DELETE

Path Operation
 ↓
HTTP Method + Path + Function
```

Example:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

Remember:

```text
GET    → Read
POST   → Create
PUT    → Replace / Update
PATCH  → Partial Update
DELETE → Delete
```

---

## 23. Practice

Create these endpoints for a **School Management API**:

```text
GET    /students
POST   /students
GET    /teachers
POST   /teachers
PUT    /students/1
PATCH  /students/1
DELETE /students/1
```

For now, simply return a message from each endpoint.

Example:

```python
@app.get("/students")
def get_students():
    return {"message": "All students"}
```

Don't use a database or Pydantic yet.

---

## Next Lecture

### Lecture 3 — Path Parameters & Query Parameters

We will learn:

- What are path parameters?
- What are query parameters?
- `/students/10`
- `/students?class_name=10`
- Difference between path and query parameters
- Optional query parameters
- Type conversion
- Interview questions
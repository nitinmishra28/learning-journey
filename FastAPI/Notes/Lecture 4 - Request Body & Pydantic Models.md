# FastAPI — Lecture 4: Request Body & Pydantic Models

## 1. What is a Request Body?

A **request body** is data sent by the client to the backend inside an HTTP request.

For example, when creating a student, the frontend may send:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

This data is called the **request body**.

Typical flow:

```text
React / Client
      ↓
POST Request
      ↓
JSON Request Body
      ↓
FastAPI
      ↓
Validate Data
      ↓
Business Logic
```

---

# 2. When Do We Use a Request Body?

Request bodies are commonly used when we need to:

- Create data
- Update data
- Send structured information to the backend

Example:

```text
POST /students
```

The client can send:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

---

# 3. What is Pydantic?

**Pydantic** is a Python library used for:

- Data validation
- Data parsing
- Data serialization
- Defining data schemas

FastAPI uses Pydantic heavily for handling request and response data.

Simple idea:

```text
Client Data
     ↓
Pydantic Model
     ↓
Validation
     ↓
FastAPI
```

---

# 4. Why Do We Need Pydantic?

Suppose our API expects:

```json
{
    "name": "Nitin",
    "age": 25
}
```

But the client sends:

```json
{
    "name": "Nitin",
    "age": "hello"
}
```

There is a problem.

We expect:

```text
age → integer
```

but received:

```text
age → string
```

Pydantic helps FastAPI validate this data.

---

# 5. Creating a Pydantic Model

In modern Pydantic:

```python
from pydantic import BaseModel
```

Then create a model:

```python
class Student(BaseModel):
    name: str
    age: int
    class_name: str
```

This defines the expected structure of a student.

```text
Student
│
├── name → str
├── age → int
└── class_name → str
```

---

# 6. Using Pydantic with FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    class_name: str


@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "class_name": student.class_name
    }
```

Now send:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

Response:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

---

# 7. How FastAPI Understands the Request Body

Look at:

```python
def create_student(student: Student):
```

FastAPI sees:

```text
student: Student
       ↓
Pydantic model
       ↓
Request body
```

Because `Student` is a Pydantic model, FastAPI expects JSON data matching that model.

---

# 8. Request Body Flow

For:

```python
@app.post("/students")
def create_student(student: Student):
```

The flow is:

```text
Client
  ↓
POST /students
  ↓
JSON Body
  ↓
FastAPI
  ↓
Pydantic Validation
  ↓
Student Object
  ↓
Function
```

---

# 9. Accessing Model Fields

Suppose:

```python
class Student(BaseModel):
    name: str
    age: int
```

Then:

```python
@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age
    }
```

We access fields using:

```python
student.name
student.age
```

---

# 10. Required Fields

By default, fields without a default value are required.

Example:

```python
class Student(BaseModel):
    name: str
    age: int
```

The client must send:

```json
{
    "name": "Nitin",
    "age": 25
}
```

If the client sends:

```json
{
    "name": "Nitin"
}
```

the request fails validation because:

```text
age
↓
Required
```

---

# 11. Optional Fields

We can make a field optional.

```python
class Student(BaseModel):
    name: str
    age: int
    phone: str | None = None
```

Now:

```json
{
    "name": "Nitin",
    "age": 25
}
```

is valid.

And this is also valid:

```json
{
    "name": "Nitin",
    "age": 25,
    "phone": "9876543210"
}
```

The important part is:

```python
phone: str | None = None
```

---

# 12. Default Values

We can provide a default value.

```python
class Student(BaseModel):
    name: str
    age: int
    active: bool = True
```

If the client sends:

```json
{
    "name": "Nitin",
    "age": 25
}
```

then:

```text
active
  ↓
True
```

will be used.

---

# 13. Type Validation

Suppose:

```python
class Student(BaseModel):
    name: str
    age: int
```

Valid:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Invalid:

```json
{
    "name": "Nitin",
    "age": "abc"
}
```

Pydantic validates the data before the function processes it.

---

# 14. Automatic Validation Error

Suppose the API expects:

```python
class Student(BaseModel):
    name: str
    age: int
```

But the client sends:

```json
{
    "name": "Nitin"
}
```

FastAPI returns a validation error because `age` is missing.

Similarly:

```json
{
    "name": "Nitin",
    "age": "abc"
}
```

will fail because `age` should be an integer.

This prevents invalid data from reaching our application logic.

---

# 15. Request Body vs Query Parameter

This is an important interview concept.

### Query Parameter

```text
GET /students?class_id=10
```

Data:

```text
class_id=10
```

### Request Body

```text
POST /students
```

Body:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Simple difference:

```text
Query Parameter
        ↓
URL

Request Body
        ↓
HTTP Request Body
```

---

# 16. Request Body vs Path Parameter

Path parameter:

```text
GET /students/10
```

Here:

```text
10
↓
Path Parameter
```

Request body:

```text
POST /students
```

with:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Here the JSON is the:

```text
Request Body
```

---

# 17. Complete Student Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    class_name: str
    phone: str | None = None


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created",
        "student": {
            "name": student.name,
            "age": student.age,
            "class_name": student.class_name,
            "phone": student.phone
        }
    }
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10",
    "phone": "9876543210"
}
```

Response:

```json
{
    "message": "Student created",
    "student": {
        "name": "Nitin",
        "age": 25,
        "class_name": "10",
        "phone": "9876543210"
    }
}
```

---

# 18. Nested Pydantic Models

Pydantic models can contain other Pydantic models.

Example:

```python
class Address(BaseModel):
    city: str
    state: str


class Student(BaseModel):
    name: str
    age: int
    address: Address
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "address": {
        "city": "Bhopal",
        "state": "Madhya Pradesh"
    }
}
```

FastAPI/Pydantic validates the nested structure as well.

---

# 19. Multiple Request Body Fields

A Pydantic model can contain many fields.

Example:

```python
class Student(BaseModel):
    name: str
    age: int
    email: str
    class_name: str
    section: str
    active: bool
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "email": "nitin@example.com",
    "class_name": "10",
    "section": "A",
    "active": true
}
```

---

# 20. Pydantic Model is Not the Database Model

This is important.

A Pydantic model:

```python
class Student(BaseModel):
    name: str
    age: int
```

is mainly used for:

```text
Validation
Serialization
Request/Response schema
```

It does **not automatically create a database table**.

Database models are a separate concept and will be covered later with SQLAlchemy.

---

# 21. Pydantic Model Naming

Use meaningful names.

Good:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
```

```python
class StudentResponse(BaseModel):
    id: int
    name: str
```

Avoid unclear names:

```python
class Data(BaseModel):
    ...
```

As projects become larger, meaningful names become important.

---

# 22. Create and Update Models

In real APIs, different operations may need different schemas.

For example:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    class_name: str
```

For updating:

```python
class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    class_name: str | None = None
```

This allows partial updates.

We will study response models and better schema design in upcoming lectures.

---

# 23. Automatic Swagger Documentation

One major benefit of using Pydantic models is that FastAPI automatically uses them in API documentation.

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You will see the request body schema.

For example:

```text
Student
├── name
├── age
├── class_name
└── phone
```

Swagger lets you test the API directly.

---

# 24. Common Mistakes

### Mistake 1 — Not Using a Pydantic Model

You could manually process dictionaries, but for structured API input, Pydantic models are the standard approach.

Prefer:

```python
class Student(BaseModel):
    name: str
    age: int
```

---

### Mistake 2 — Confusing Model and Object

This:

```python
class Student(BaseModel):
    name: str
    age: int
```

is the **model definition**.

This:

```python
student: Student
```

means the function receives a `Student` object.

---

### Mistake 3 — Making Everything Optional

Avoid:

```python
class Student(BaseModel):
    name: str | None = None
    age: int | None = None
    email: str | None = None
```

unless those fields are actually optional.

Required fields should remain required.

---

### Mistake 4 — Putting Database Logic Inside the Pydantic Model

Don't mix responsibilities.

```text
Pydantic
   ↓
Validation / Schema

SQLAlchemy
   ↓
Database ORM / Database operations
```

Keep these responsibilities separate.

---

# 25. Interview Questions

### Q1. What is Pydantic?

Pydantic is a Python library used for data validation, parsing, and serialization. FastAPI uses Pydantic models for structured request and response data.

---

### Q2. Why does FastAPI use Pydantic?

Pydantic allows FastAPI to validate incoming data based on Python type definitions.

Example:

```python
class Student(BaseModel):
    name: str
    age: int
```

FastAPI can automatically validate the request against this schema.

---

### Q3. How do you define a request body in FastAPI?

Using a Pydantic model.

```python
class Student(BaseModel):
    name: str
    age: int


@app.post("/students")
def create_student(student: Student):
    return student
```

---

### Q4. What happens if required data is missing?

FastAPI returns a validation error before the endpoint function processes the request.

---

### Q5. What is the difference between Pydantic and SQLAlchemy?

```text
Pydantic
   ↓
Validation / Serialization / API Schema

SQLAlchemy
   ↓
Database ORM / Database Interaction
```

They solve different problems.

---

### Q6. Can Pydantic models be nested?

Yes.

```python
class Address(BaseModel):
    city: str


class Student(BaseModel):
    name: str
    address: Address
```

---

### Q7. What is the difference between a request body and query parameter?

Request body:

```text
POST /students

{
    "name": "Nitin",
    "age": 25
}
```

Query parameter:

```text
GET /students?class_id=10
```

---

# 26. Quick Revision

Remember:

```text
Pydantic
    ↓
Define Data Structure
    ↓
Validate Data
    ↓
FastAPI Processes Request
```

Example:

```python
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
```

Use it:

```python
@app.post("/students")
def create_student(student: Student):
    return student
```

Request:

```json
{
    "name": "Nitin",
    "age": 25
}
```

---

## Most Important Points

```text
1. Request body contains data sent by the client.

2. Pydantic models define the expected structure.

3. FastAPI validates the request using the model.

4. Required fields must be provided.

5. Optional fields can have None/default values.

6. Pydantic models are API schemas, not database tables.

7. Nested Pydantic models are supported.

8. FastAPI automatically generates request-body documentation.
```

---

# 27. Practice

Create a Pydantic model for a teacher:

```text
Teacher
├── name
├── age
├── email
├── subject
└── experience
```

Create:

```text
POST /teachers
```

Request:

```json
{
    "name": "Rahul",
    "age": 30,
    "email": "rahul@example.com",
    "subject": "Mathematics",
    "experience": 5
}
```

Return the received teacher data.

---

### Extra Practice

Create a nested model:

```text
Student
├── name
├── age
└── address
      ├── city
      └── state
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "address": {
        "city": "Bhopal",
        "state": "Madhya Pradesh"
    }
}
```

Don't use a database yet.

---

## Next Lecture
       
### Lecture 5 — Response Models & Status Codes

We will learn:

- What is a response model?
- Why response models are needed
- `response_model`
- Controlling API response data
- Response validation
- HTTP status codes
- `status_code`
- `201`, `200`, `204`, `400`, `401`, `403`, `404`, `422`, `500`
- Request model vs response model
- Interview questions
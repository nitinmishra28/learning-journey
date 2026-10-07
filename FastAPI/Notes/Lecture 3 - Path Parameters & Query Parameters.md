# FastAPI — Lecture 3: Path Parameters & Query Parameters

## 1. What are Parameters?

Parameters are values that we send to an API to tell it **which data we want** or **how we want the API to behave**.

For example:

```text
GET /students/10
```

Here:

```text
10
↓
Parameter
```

We mainly use two types in FastAPI:

```text
Path Parameters
Query Parameters
```

---

# 2. Path Parameters

A **path parameter** is a value that is part of the URL path.

Example:

```text
GET /students/10
```

Here:

```text
/students/10
          ↑
      Path Parameter
```

Usually, path parameters are used when we want to identify a **specific resource**.

Examples:

```text
/students/10
/users/25
/products/100
/orders/500
```

---

# 3. Creating a Path Parameter

FastAPI uses `{}` to define a path parameter.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/students/{student_id}")
def get_student(student_id):
    return {
        "student_id": student_id
    }
```

Now if we call:

```text
GET /students/10
```

Response:

```json
{
    "student_id": "10"
}
```

---

# 4. How FastAPI Understands It

This route:

```python
@app.get("/students/{student_id}")
def get_student(student_id):
```

means:

```text
/students/{student_id}
          ↓
     Dynamic value
          ↓
        10

/students/10
```

FastAPI takes:

```text
10
```

and passes it to:

```python
student_id
```

---

# 5. Path Parameter with Type

We should normally specify the expected type.

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

Now:

```text
GET /students/10
```

produces:

```json
{
    "student_id": 10
}
```

Notice:

```text
"10"
```

became:

```text
10
```

because we specified:

```python
student_id: int
```

FastAPI uses the type information for validation and conversion.

---

# 6. Automatic Validation

Suppose we have:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

Valid:

```text
GET /students/10
```

Invalid:

```text
GET /students/abc
```

Because:

```text
abc
↓
Cannot be converted to int
```

FastAPI returns a validation error.

This is one of the advantages of using type hints with FastAPI.

---

# 7. Multiple Path Parameters

We can have multiple path parameters.

Example:

```python
@app.get("/schools/{school_id}/students/{student_id}")
def get_student(school_id: int, student_id: int):
    return {
        "school_id": school_id,
        "student_id": student_id
    }
```

Request:

```text
GET /schools/5/students/10
```

Response:

```json
{
    "school_id": 5,
    "student_id": 10
}
```

---

# 8. Real-World Example

For a school management system:

```text
GET /students/101
```

could mean:

> Get student whose ID is 101.

Another example:

```text
GET /schools/5/students/101
```

could mean:

> Get student 101 from school 5.

---

# 9. Query Parameters

A **query parameter** is a value added after `?` in the URL.

Example:

```text
GET /students?class_name=10
```

Here:

```text
/students
     ?
class_name=10
```

`class_name` is a query parameter.

---

# 10. Creating a Query Parameter

In FastAPI, if a function parameter is not part of the path, FastAPI treats it as a query parameter.

Example:

```python
@app.get("/students")
def get_students(class_name: str):
    return {
        "class": class_name
    }
```

Request:

```text
GET /students?class_name=10
```

Response:

```json
{
    "class": "10"
}
```

---

# 11. Query Parameter with Type

We can specify the type.

```python
@app.get("/students")
def get_students(class_id: int):
    return {
        "class_id": class_id
    }
```

Request:

```text
GET /students?class_id=10
```

Response:

```json
{
    "class_id": 10
}
```

---

# 12. Multiple Query Parameters

We can have multiple query parameters.

```python
@app.get("/students")
def get_students(
    class_id: int,
    section: str
):
    return {
        "class_id": class_id,
        "section": section
    }
```

Request:

```text
GET /students?class_id=10&section=A
```

Response:

```json
{
    "class_id": 10,
    "section": "A"
}
```

Query parameters are separated using:

```text
&
```

Example:

```text
?class_id=10&section=A
```

---

# 13. Optional Query Parameters

A query parameter can be optional.

Example:

```python
@app.get("/students")
def get_students(class_name: str | None = None):
    return {
        "class_name": class_name
    }
```

Now both requests are valid:

```text
GET /students
```

and:

```text
GET /students?class_name=10
```

Without the parameter:

```json
{
    "class_name": null
}
```

With the parameter:

```json
{
    "class_name": "10"
}
```

---

# 14. Default Values

We can provide a default value.

```python
@app.get("/students")
def get_students(limit: int = 10):
    return {
        "limit": limit
    }
```

Request:

```text
GET /students
```

Response:

```json
{
    "limit": 10
}
```

If the client sends:

```text
GET /students?limit=20
```

Response:

```json
{
    "limit": 20
}
```

---

# 15. Path Parameter vs Query Parameter

This is a very important interview topic.

### Path Parameter

```text
GET /students/10
```

Used to identify a specific resource.

```text
10
↓
student_id
```

### Query Parameter

```text
GET /students?class_id=10
```

Used to filter, search, sort, paginate, or control the response.

```text
class_id=10
↓
Filter
```

---

# 16. Main Difference

| Path Parameter | Query Parameter |
|---|---|
| Part of URL path | Comes after `?` |
| Usually identifies a resource | Usually filters/modifies the request |
| Generally required | Can be optional |
| `/students/10` | `/students?class_id=10` |
| Uses `{}` in route | Defined as function parameter |

---

# 17. Real-World Example

Suppose we have:

```text
GET /students/101
```

This means:

> Get student 101.

Here `101` is a **path parameter**.

Now:

```text
GET /students?class_id=10
```

means:

> Get students belonging to class 10.

Here `class_id` is a **query parameter**.

We can combine both:

```text
GET /schools/5/students?class_id=10
```

Here:

```text
5
↓
Path parameter

class_id=10
↓
Query parameter
```

---

# 18. Path + Query Parameter Together

Example:

```python
@app.get("/schools/{school_id}/students")
def get_students(
    school_id: int,
    class_id: int | None = None
):
    return {
        "school_id": school_id,
        "class_id": class_id
    }
```

Request:

```text
GET /schools/5/students?class_id=10
```

Response:

```json
{
    "school_id": 5,
    "class_id": 10
}
```

FastAPI automatically understands:

```text
school_id
↓
Path parameter

class_id
↓
Query parameter
```

---

# 19. Query Parameters for Filtering

Query parameters are commonly used for filtering.

Example:

```python
@app.get("/students")
def get_students(
    class_id: int | None = None,
    section: str | None = None
):
    return {
        "class_id": class_id,
        "section": section
    }
```

Possible requests:

```text
GET /students
```

```text
GET /students?class_id=10
```

```text
GET /students?section=A
```

```text
GET /students?class_id=10&section=A
```

---

# 20. Query Parameters for Pagination

Pagination is a common real-world use case.

Example:

```python
@app.get("/students")
def get_students(
    page: int = 1,
    limit: int = 10
):
    return {
        "page": page,
        "limit": limit
    }
```

Request:

```text
GET /students?page=2&limit=20
```

Response:

```json
{
    "page": 2,
    "limit": 20
}
```

Later, when we build database APIs, these parameters will be used to fetch a specific portion of records.

---

# 21. Type Conversion

FastAPI automatically converts values according to the type hint.

Example:

```python
@app.get("/students")
def get_students(limit: int):
    return {
        "limit": limit
    }
```

Request:

```text
GET /students?limit=20
```

FastAPI converts:

```text
"20"
 ↓
20
```

because:

```python
limit: int
```

---

# 22. Boolean Query Parameters

FastAPI can also convert boolean values.

Example:

```python
@app.get("/students")
def get_students(active: bool = True):
    return {
        "active": active
    }
```

Request:

```text
GET /students?active=false
```

Response:

```json
{
    "active": false
}
```

---

# 23. Complete Example

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }


@app.get("/students")
def get_students(
    class_id: int | None = None,
    section: str | None = None,
    page: int = 1,
    limit: int = 10
):
    return {
        "class_id": class_id,
        "section": section,
        "page": page,
        "limit": limit
    }
```

Examples:

```text
GET /students/101
```

```text
GET /students?class_id=10
```

```text
GET /students?class_id=10&section=A
```

```text
GET /students?page=2&limit=20
```

---

# 24. Important FastAPI Concept

FastAPI determines whether a parameter is a path parameter or query parameter based on the route.

Example:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
```

Because `student_id` appears in:

```text
/students/{student_id}
```

FastAPI knows it is a **path parameter**.

Now:

```python
@app.get("/students")
def get_students(class_id: int):
```

Because `class_id` does not appear in the path, FastAPI treats it as a **query parameter**.

---

# 25. Common Mistakes

### Mistake 1 — Forgetting `{}` for Path Parameters

Wrong:

```python
@app.get("/students/student_id")
def get_student(student_id: int):
    ...
```

This creates a fixed path:

```text
/students/student_id
```

Correct:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    ...
```

Now:

```text
/students/10
```

works.

---

### Mistake 2 — Making Everything a Path Parameter

Don't create:

```text
/students/10/class/5/section/A/page/2
```

when these values are really filters or pagination options.

Prefer:

```text
/students/10
```

for identifying a specific student.

And:

```text
/students?class_id=5&section=A&page=2
```

for filtering/pagination.

---

### Mistake 3 — Forgetting Optional Defaults

This:

```python
def get_students(class_id: int):
```

makes `class_id` required.

If it should be optional:

```python
def get_students(class_id: int | None = None):
```

---

# 26. Interview Questions

### Q1. What is a path parameter?

A value embedded directly in the URL path and commonly used to identify a specific resource.

Example:

```text
/students/10
```

---

### Q2. What is a query parameter?

A parameter provided after `?` in the URL.

Example:

```text
/students?class_id=10
```

---

### Q3. What is the difference between path and query parameters?

```text
Path:
GET /students/10

Query:
GET /students?class_id=10
```

Path parameters are part of the URL path, while query parameters are added after `?`.

---

### Q4. How does FastAPI know a parameter is a path parameter?

The parameter appears inside the route path.

Example:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
```

---

### Q5. How does FastAPI know a parameter is a query parameter?

If a function parameter is not included in the path, FastAPI treats it as a query parameter.

Example:

```python
@app.get("/students")
def get_students(class_id: int):
```

Here `class_id` is a query parameter.

---

### Q6. Can path and query parameters be used together?

Yes.

Example:

```text
GET /schools/5/students?class_id=10
```

Here:

```text
5
↓
Path parameter

class_id=10
↓
Query parameter
```

---

### Q7. Can query parameters be optional?

Yes.

```python
@app.get("/students")
def get_students(class_id: int | None = None):
    ...
```

---

# 27. Quick Revision

```text
PATH PARAMETER
        ↓
Part of URL
        ↓
Usually identifies a resource

/students/10
          ↑
       student_id
```

```text
QUERY PARAMETER
        ↓
Comes after ?
        ↓
Usually used for filtering/search/pagination

/students?class_id=10
          ↑
      query parameter
```

Remember:

```text
/students/10
        ↓
Path Parameter


/students?class_id=10
          ↓
Query Parameter
```

---

# 28. Practice

Create these APIs:

### 1. Get a specific teacher

```text
GET /teachers/{teacher_id}
```

Expected:

```text
GET /teachers/10
```

Return:

```json
{
    "teacher_id": 10
}
```

---

### 2. Filter students

```text
GET /students?class_id=10&section=A
```

Return:

```json
{
    "class_id": 10,
    "section": "A"
}
```

---

### 3. Pagination

Create:

```text
GET /students?page=2&limit=20
```

Return:

```json
{
    "page": 2,
    "limit": 20
}
```

---

### 4. Combine Path + Query

Create:

```text
GET /schools/5/students?class_id=10
```

Return:

```json
{
    "school_id": 5,
    "class_id": 10
}
```

Don't use a database or Pydantic yet.

---

## Next Lecture

### Lecture 4 — Request Body & Pydantic Models

We will learn:

- What is a request body?
- Why do APIs need request bodies?
- Pydantic models
- Creating request schemas
- Sending JSON data
- Automatic validation
- Required vs optional fields
- Nested models
- Interview questions
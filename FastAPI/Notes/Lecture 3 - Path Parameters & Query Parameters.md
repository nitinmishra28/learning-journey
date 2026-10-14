# FastAPI — Lecture 3: Path Parameters & Query Parameters

My personal notes for learning **Path Parameters, Query Parameters, and Data Validation in FastAPI**.

## 1. What Are Parameters?

Parameters are values sent to an API to specify which data we want or how we want the API to behave.

Example:

```text
GET /students/10
```

Here, `10` identifies a particular student.

FastAPI commonly uses two types of parameters:

- **Path Parameters** — values included in the URL path.
- **Query Parameters** — values provided after `?` in the URL.

---

## 2. Path Parameters

A path parameter is a value included directly in the URL path.

Examples:

```text
GET /students/10
GET /users/25
GET /products/100
```

Path parameters are generally used to identify a specific resource.

### Creating a Path Parameter

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/students/{student_id}")
async def get_student(student_id):
    return {
        "student_id": student_id
    }
```

Request:

```text
GET /students/10
```

Response:

```json
{
    "student_id": "10"
}
```

Without a type hint, the value is treated as a string.

---

## 3. Path Parameters With Types

We should specify the expected data type of a parameter.

```python
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

Request:

```text
GET /students/10
```

Response:

```json
{
    "student_id": 10
}
```

FastAPI converts the URL value into an integer.

If we send:

```text
GET /students/abc
```

FastAPI returns a validation error because `"abc"` cannot be converted into an integer.

**Remember:** Type hints provide type conversion and validation, but they do not enforce every business rule. For example, `int` alone allows negative numbers.

---

## 4. Multiple Path Parameters

We can define multiple path parameters in one endpoint.

```python
@app.get("/schools/{school_id}/students/{student_id}")
async def get_student(school_id: int, student_id: int):
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

FastAPI matches each URL value to its corresponding function parameter.

---

## 5. Query Parameters

A query parameter is a value added after `?` in the URL.

Example:

```text
GET /students?class_id=10
```

Here:

- `/students` is the path.
- `class_id` is the query parameter.
- `10` is its value.

Query parameters are commonly used for filtering, searching, sorting, and pagination.

### Creating a Query Parameter

```python
@app.get("/students")
async def get_students(class_name: str):
    return {
        "class_name": class_name
    }
```

Request:

```text
GET /students?class_name=10
```

Response:

```json
{
    "class_name": "10"
}
```

A simple function parameter that is not part of the route path is generally interpreted as a query parameter, unless it is otherwise declared, such as a request body or dependency.

---

## 6. Query Parameters With Types

```python
@app.get("/students")
async def get_students(class_id: int):
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

FastAPI converts the query parameter into an integer.

If a required parameter is missing or its value cannot be converted to the specified type, FastAPI returns a validation error.

---

## 7. Multiple Query Parameters

```python
@app.get("/students")
async def get_students(class_id: int, section: str):
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

Query parameters are separated using `&`.

---

## 8. Optional Query Parameters

A query parameter can be optional if we provide a default value.

```python
@app.get("/students")
async def get_students(class_name: str | None = None):
    return {
        "class_name": class_name
    }
```

Both requests are valid:

```text
GET /students
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

**Important:**

- `str | None` means the type can be a string or `None`.
- `= None` supplies a default value and makes the parameter optional.

A parameter can also have a default value without accepting `None` explicitly:

```python
@app.get("/students")
async def get_students(limit: int = 10):
    return {"limit": limit}
```

---

## 9. Default Values

We can define default values for query parameters.

```python
@app.get("/students")
async def get_students(limit: int = 10):
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

The supplied query parameter overrides the default value.

---

## 10. Path Parameter Validation Using `Path()`

Type hints validate the data type, but sometimes we need additional constraints.

For example, a book ID should be a positive integer.

FastAPI provides `Path()` to declare metadata and validation constraints for path parameters.

### Example

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(
    book_id: int = Path(gt=0)
):
    return {
        "book_id": book_id
    }
```

### Understanding the Code

- `book_id: int` means the value must be an integer.
- `Path()` declares path parameter constraints.
- `gt=0` means the value must be **greater than zero**.

### Valid Requests

```text
GET /books/1
GET /books/10
GET /books/100
```

### Invalid Requests

```text
GET /books/0
GET /books/-5
GET /books/abc
```

These requests fail validation because the value is either not an integer or does not satisfy the positive-value constraint.

FastAPI automatically returns a validation error, normally with HTTP status code `422 Unprocessable Entity`.

### Common `Path()` Constraints

| Constraint | Meaning |
|---|---|
| `gt=0` | Greater than zero |
| `ge=1` | Greater than or equal to one |
| `lt=100` | Less than 100 |
| `le=100` | Less than or equal to 100 |
| `min_length=3` | Minimum string length of 3 |
| `max_length=20` | Maximum string length of 20 |
| `description="Book ID"` | Adds a description to the API documentation |

`gt`, `ge`, `lt`, and `le` are numeric constraints. String length constraints apply to string parameters.

### Example With Multiple Constraints

```python
@app.get("/books/{book_id}")
async def read_book(
    book_id: int = Path(
        gt=0,
        le=1000,
        description="Unique ID of the book"
    )
):
    return {
        "book_id": book_id
    }
```

Here, `book_id` must be greater than `0` and less than or equal to `1000`.

---

## 11. Query Parameter Validation Using `Query()`

FastAPI provides `Query()` to apply validation constraints to query parameters.

For example, we want to allow a page limit between `1` and `100`.

```python
from fastapi import Query

@app.get("/students")
async def get_students(
    limit: int = Query(
        default=10,
        gt=0,
        le=100
    )
):
    return {
        "limit": limit
    }
```

### Understanding the Code

- `default=10` means the default limit is `10`.
- `gt=0` means the value must be greater than zero.
- `le=100` means the value must be less than or equal to `100`.

### Valid Requests

```text
GET /students
GET /students?limit=1
GET /students?limit=50
GET /students?limit=100
```

### Invalid Requests

```text
GET /students?limit=0
GET /students?limit=-5
GET /students?limit=101
GET /students?limit=abc
```

These requests fail validation.

### Common `Query()` Constraints

| Constraint | Meaning |
|---|---|
| `gt=0` | Greater than zero |
| `ge=1` | Greater than or equal to one |
| `lt=100` | Less than 100 |
| `le=100` | Less than or equal to 100 |
| `min_length=3` | Minimum string length of 3 |
| `max_length=50` | Maximum string length of 50 |
| `pattern="..."` | String must match a regular expression |
| `description="..."` | Adds a description to API documentation |

**Note:** `Path()` and `Query()` do not replace type hints. Use the type hint to specify the expected type and the constraints to define acceptable values.

---

## 12. String Validation

We can validate the length and format of string parameters.

For example, suppose a student section must contain between one and five characters.

```python
@app.get("/students")
async def get_students(
    section: str = Query(
        min_length=1,
        max_length=5
    )
):
    return {
        "section": section
    }
```

Valid requests:

```text
GET /students?section=A
GET /students?section=AB
```

An invalid request:

```text
GET /students?section=TOOLONG
```

The last request fails because the value exceeds the maximum length.

### Using a Pattern

Suppose we want a section containing exactly one uppercase English letter.

```python
@app.get("/students")
async def get_students(
    section: str = Query(
        min_length=1,
        max_length=1,
        pattern="^[A-Z]$"
    )
):
    return {
        "section": section
    }
```

Valid:

```text
GET /students?section=A
GET /students?section=B
```

Invalid:

```text
GET /students?section=AB
GET /students?section=a
GET /students?section=1
```

The pattern `^[A-Z]$` allows exactly one uppercase English letter.

---

## 13. Optional Parameters With Validation

A query parameter can be optional and still have validation constraints.

```python
@app.get("/students")
async def get_students(
    class_id: int | None = Query(
        default=None,
        gt=0
    )
):
    return {
        "class_id": class_id
    }
```

Valid requests:

```text
GET /students
GET /students?class_id=10
```

Invalid request:

```text
GET /students?class_id=0
```

The parameter is optional, but if supplied, it must be greater than zero.

---

## 14. Pagination With Validation

Pagination is a common real-world use case for query parameters.

```python
@app.get("/students")
async def get_students(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
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

Here:

- `page` must be at least `1`.
- `limit` must be between `1` and `100`.
- Both parameters have default values.

Invalid examples:

```text
GET /students?page=0
GET /students?page=-1
GET /students?limit=0
GET /students?limit=500
```

In a real application, these values can control how many records are fetched from the database.

---

## 15. Path and Query Parameters Together

We can use both parameter types in the same endpoint.

```python
@app.get("/schools/{school_id}/students")
async def get_students(
    school_id: int = Path(gt=0),
    class_id: int | None = Query(default=None, gt=0),
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "school_id": school_id,
        "class_id": class_id,
        "limit": limit
    }
```

Request:

```text
GET /schools/5/students?class_id=10&limit=20
```

Response:

```json
{
    "school_id": 5,
    "class_id": 10,
    "limit": 20
}
```

In this example:

- `school_id` is a path parameter and must be positive.
- `class_id` is an optional query parameter and must be positive if provided.
- `limit` is a query parameter between `1` and `100`.

---

## 16. How Does FastAPI Validate Parameters?

FastAPI uses Python type hints and parameter declarations to validate incoming values.

For example:

```python
@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    return {
        "book_id": book_id
    }
```

When a request arrives, FastAPI checks:

1. Is `book_id` present in the URL?
2. Can the value be converted to an integer?
3. Does the value satisfy `gt=0`?
4. If validation succeeds, execute the endpoint function.
5. If validation fails, return an error response.

FastAPI generally returns HTTP `422 Unprocessable Entity` for invalid request parameters.

The error response includes details about the invalid input.

**Important:** FastAPI handles request validation automatically. You do not need to write manual `if` conditions for every basic parameter constraint.

---

## 17. Path Parameter vs Query Parameter

| Path Parameter | Query Parameter |
|---|---|
| Part of the URL path | Comes after `?` |
| Usually identifies a resource | Usually filters or modifies a request |
| Generally required by the route | Can be optional or required |
| Uses `{}` in the route | Declared as a function parameter |
| Can use `Path()` for constraints | Can use `Query()` for constraints |

Examples:

```text
GET /students/10
```

Here, `10` is a path parameter.

```text
GET /students?class_id=10
```

Here, `class_id` is a query parameter.

---

## 18. Type Hints vs `Path()` vs `Query()`

These three concepts serve different purposes.

| Feature | Purpose |
|---|---|
| `book_id: int` | Specifies the expected type |
| `Path(gt=0)` | Adds constraints to a path parameter |
| `Query(gt=0)` | Adds constraints to a query parameter |

Example:

```python
@app.get("/books/{book_id}")
async def read_book(
    book_id: int = Path(gt=0)
):
    return {
        "book_id": book_id
    }
```

Read it as:

- `book_id` is the parameter name.
- `int` is the expected type.
- `Path(gt=0)` declares a constraint for the path parameter.

---

## 19. Common Mistakes

### Mistake 1: Forgetting `{}` in the Path

Incorrect:

```python
@app.get("/students/student_id")
async def get_student(student_id: int):
    return {"student_id": student_id}
```

This creates the fixed URL `/students/student_id`.

Correct:

```python
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}
```

### Mistake 2: Assuming `int` Rejects Negative Values

```python
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id": book_id}
```

The type hint `int` does not reject negative integers.

Use:

```python
@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    return {"book_id": book_id}
```

### Mistake 3: Forgetting That a Parameter Is Required

```python
@app.get("/students")
async def get_students(class_id: int):
    return {"class_id": class_id}
```

The client must supply `class_id`.

To make it optional:

```python
@app.get("/students")
async def get_students(class_id: int | None = None):
    return {"class_id": class_id}
```

### Mistake 4: Using the Wrong Constraint

- `gt=0`: greater than zero.
- `ge=0`: greater than or equal to zero.
- `lt=100`: less than 100.
- `le=100`: less than or equal to 100.

For example, `le=100` allows `100`, but `lt=100` does not.

### Mistake 5: Confusing `Path()` and `Query()`

Use `Path()` for values embedded in the URL path.

Use `Query()` for values provided through the query string.

---

## 20. Interview Questions

### Q1. What is a path parameter?

A value embedded directly in the URL path, commonly used to identify a resource.

Example: `/students/10`

### Q2. What is a query parameter?

A value supplied after `?` in a URL, commonly used for filtering, searching, and pagination.

Example: `/students?class_id=10`

### Q3. How does FastAPI validate path parameters?

FastAPI uses type hints and constraints declared through `Path()`.

```python
book_id: int = Path(gt=0)
```

This requires a positive integer.

### Q4. What is the purpose of `Query()`?

`Query()` declares metadata and validation constraints for query parameters.

```python
limit: int = Query(default=10, ge=1, le=100)
```

This gives `limit` a default value of `10` and restricts it to `1` through `100`.

### Q5. What is the difference between `gt` and `ge`?

- `gt`: greater than.
- `ge`: greater than or equal to.

For example, `gt=0` rejects `0`, whereas `ge=0` accepts it.

### Q6. What happens when parameter validation fails?

FastAPI normally returns HTTP `422 Unprocessable Entity` with details about the validation failure.

### Q7. Can optional query parameters have constraints?

Yes. For example:

```python
class_id: int | None = Query(default=None, gt=0)
```

The parameter can be omitted, but if supplied, it must be greater than zero.

### Q8. Can path parameters have default values?

A path parameter is required because it is part of the route. Use `Path()` to declare its metadata and constraints rather than making it optional.

### Q9. Does `int` alone guarantee a positive value?

No. It validates the integer type, not whether the value is positive. Use a constraint such as `Path(gt=0)` or `Query(gt=0)` when needed.

### Q10. Does FastAPI automatically document parameter constraints?

Yes. FastAPI uses parameter declarations and type information to generate OpenAPI documentation, which is displayed in Swagger UI.

---

## 21. Quick Revision

```text
PATH PARAMETER
    |
    +-- Included in the URL path
    +-- Commonly identifies a resource
    +-- Use Path() for constraints
    |
    +-- Example:
        /books/10
        book_id: int = Path(gt=0)


QUERY PARAMETER
    |
    +-- Included after ?
    +-- Commonly used for filtering and pagination
    +-- Use Query() for constraints
    |
    +-- Example:
        /students?limit=20
        limit: int = Query(default=10, ge=1, le=100)
```

Remember:

- Type hints specify expected data types.
- `Path()` validates path parameters.
- `Query()` validates query parameters.
- FastAPI performs request validation automatically.
- Invalid request parameters normally produce HTTP `422`.

---

## 22. Practice

Implement the following endpoints without using a database or Pydantic request-body models yet.

### Practice 1: Get a Specific Teacher

Create:

```text
GET /teachers/{teacher_id}
```

Requirements:

- `teacher_id` must be an integer.
- `teacher_id` must be greater than zero.

### Practice 2: Filter Students

Create:

```text
GET /students?class_id=10&section=A
```

Requirements:

- `class_id` is an optional positive integer.
- `section` is an optional string.

### Practice 3: Validate Pagination

Create:

```text
GET /students?page=2&limit=20
```

Requirements:

- `page` defaults to `1` and must be at least `1`.
- `limit` defaults to `10` and must be between `1` and `100`.

### Practice 4: Validate a Book ID

Create:

```text
GET /books/{book_id}
```

Requirements:

- `book_id` must be greater than `0`.
- `book_id` must not exceed `1000`.
- Return the validated `book_id`.

### Practice 5: Validate a Section

Create:

```text
GET /students?section=A
```

Requirements:

- `section` must be exactly one uppercase English letter.
- Use `Query()` with an appropriate pattern.

### Practice 6: Combine Path and Query Parameters

Create:

```text
GET /schools/5/students?class_id=10&limit=20
```

Requirements:

- `school_id` must be positive.
- `class_id` is optional and must be positive if provided.
- `limit` must be between `1` and `100`.

---

## Next Lecture

### Lecture 4 — Request Body & Pydantic Models

Topics:

- What is a request body?
- Why APIs need request bodies.
- Pydantic models.
- Creating request schemas.
- Sending JSON data.
- Automatic request-body validation.
- Required and optional fields.
- `Field()` and `model_config`.
- Nested models.
- Create and update schemas.
- Interview questions.

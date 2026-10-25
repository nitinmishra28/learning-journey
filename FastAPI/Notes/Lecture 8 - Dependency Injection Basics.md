# FastAPI — Lecture 8: Dependency Injection Basics

My personal notes for understanding **Dependency Injection (DI)** in FastAPI.

## 1. What Is Dependency Injection?

Dependency Injection is a technique in which a function receives the resources or functionality it needs instead of creating everything itself.

For example, an API may need:
- A database connection
- The current logged-in user
- Common query parameters
- Authentication validation
- Reusable business logic

Instead of repeating the same code in every endpoint, we can define a dependency and let FastAPI provide its result.

**Simple definition:** Dependency Injection allows us to reuse functionality and share common logic across API endpoints.

---

## 2. Understanding the Problem

Suppose multiple endpoints need to validate pagination parameters.

Without dependencies:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/students")
async def get_students(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/teachers")
async def get_teachers(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }
```

The same parameters are repeated in multiple endpoints.

If we need to add validation or change the logic, we may have to update several functions.

Dependency Injection helps us extract this reusable logic.

---

## 3. Creating Our First Dependency

FastAPI provides `Depends()` to declare dependencies.

```python
from fastapi import FastAPI, Depends

app = FastAPI()


def get_pagination():
    return {
        "page": 1,
        "limit": 10
    }


@app.get("/students")
async def get_students(pagination: dict = Depends(get_pagination)):
    return pagination
```

When we call:

```text
GET /students
```

Response:

```json
{
    "page": 1,
    "limit": 10
}
```

### How It Works

1. FastAPI receives the request.
2. It sees `Depends(get_pagination)`.
3. FastAPI calls `get_pagination()`.
4. The dependency returns a dictionary.
5. FastAPI passes that result to the `pagination` parameter.
6. The endpoint returns the result.

We do not need to call `get_pagination()` manually inside the endpoint.

**Important:** Pass the function itself to `Depends()`, without parentheses.

Correct:

```python
Depends(get_pagination)
```

Incorrect:

```python
Depends(get_pagination())
```

---

## 4. Dependencies With Parameters

A dependency can receive parameters just like a normal function.

FastAPI resolves its parameters from the request when appropriate.

```python
from fastapi import FastAPI, Depends

app = FastAPI()


def get_pagination(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/students")
async def get_students(pagination: dict = Depends(get_pagination)):
    return pagination
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

FastAPI identifies `page` and `limit` as query parameters because they are not part of the route path and have simple types.

The dependency handles extracting and validating those values.

---

## 5. Adding Validation to a Dependency

We can use `Query()` inside a dependency to validate its parameters.

```python
from fastapi import FastAPI, Depends, Query

app = FastAPI()


def get_pagination(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/students")
async def get_students(pagination: dict = Depends(get_pagination)):
    return pagination
```

Valid request:

```text
GET /students?page=2&limit=20
```

Invalid request:

```text
GET /students?page=0&limit=200
```

FastAPI validates the parameters before calling the endpoint.

- `page` must be at least `1`.
- `limit` must be between `1` and `100`.

---

## 6. Reusing a Dependency Across Endpoints

One of the main advantages of Dependency Injection is code reuse.

```python
from fastapi import FastAPI, Depends, Query

app = FastAPI()


def get_pagination(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/students")
async def get_students(pagination: dict = Depends(get_pagination)):
    return {
        "resource": "students",
        **pagination
    }


@app.get("/teachers")
async def get_teachers(pagination: dict = Depends(get_pagination)):
    return {
        "resource": "teachers",
        **pagination
    }
```

Both endpoints use the same dependency.

Example:

```text
GET /students?page=2&limit=20
GET /teachers?page=3&limit=5
```

Each request gets its own pagination values.

If pagination validation changes, we can update the dependency in one place.

---

## 7. Using a Pydantic Model for Dependency Results

Instead of returning a dictionary, we can define a Pydantic model for clearer structure and type safety.

```python
from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel

app = FastAPI()


class PaginationParams(BaseModel):
    page: int
    limit: int


def get_pagination(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
) -> PaginationParams:
    return PaginationParams(
        page=page,
        limit=limit
    )


@app.get("/students")
async def get_students(
    pagination: PaginationParams = Depends(get_pagination)
):
    return pagination
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

The Pydantic model makes the dependency's return structure explicit.

---

## 8. The `Annotated` Approach

In modern FastAPI code, `Annotated` is commonly used to declare dependencies.

```python
from typing import Annotated

from fastapi import FastAPI, Depends, Query

app = FastAPI()


def get_pagination(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "page": page,
        "limit": limit
    }


PaginationDep = Annotated[dict, Depends(get_pagination)]


@app.get("/students")
async def get_students(pagination: PaginationDep):
    return pagination


@app.get("/teachers")
async def get_teachers(pagination: PaginationDep):
    return pagination
```

### Understanding `Annotated`

```python
PaginationDep = Annotated[dict, Depends(get_pagination)]
```

This declares a reusable type annotation that combines:
- `dict`: the expected dependency result type.
- `Depends(get_pagination)`: the function FastAPI should execute to obtain that result.

Then we can write:

```python
async def get_students(pagination: PaginationDep):
    return pagination
```

This avoids repeating `Depends(get_pagination)` in every endpoint signature.

**Remember:** `Annotated` is a Python typing feature. `Depends()` tells FastAPI how to resolve the dependency.

---

## 9. Function Dependencies vs Class Dependencies

Dependencies do not have to be functions. A class can also be used.

For now, understand the basic difference.

### Function Dependency

```python
def get_current_user():
    return {
        "username": "nitin"
    }


@app.get("/profile")
async def get_profile(user: dict = Depends(get_current_user)):
    return user
```

### Class Dependency

```python
from typing import Annotated

from fastapi import Depends


class CommonParams:
    def __init__(self, page: int = 1, limit: int = 10):
        self.page = page
        self.limit = limit


@app.get("/students")
async def get_students(
    params: Annotated[CommonParams, Depends(CommonParams)]
):
    return {
        "page": params.page,
        "limit": params.limit
    }
```

FastAPI calls the class to create an instance and resolves its constructor parameters from the request.

Class-based dependencies are useful when we want to group related parameters or behavior.

---

## 10. What Happens When a Dependency Is Called Multiple Times?

FastAPI normally caches the result of a dependency within a single request.

For example:

```python
def get_common_value():
    print("Dependency executed")
    return {"value": 100}


@app.get("/example")
async def example(
    first: dict = Depends(get_common_value),
    second: dict = Depends(get_common_value)
):
    return {
        "first": first,
        "second": second
    }
```

Within the same request, FastAPI normally executes this dependency once and reuses its result.

If you need it to execute again for each use, you can disable this behavior:

```python
Depends(get_common_value, use_cache=False)
```

**Important:** The default dependency cache is scoped to the current request. It is not a persistent application-wide cache.

---

## 11. When Should We Use Dependency Injection?

Common use cases include:

- Authentication and authorization
- Database sessions
- Reusable query parameters
- Current user information
- Shared validation logic
- Configuration and settings
- Common service objects

For example, several endpoints may need the currently logged-in user. We can define one dependency that verifies the user and returns their information.

We will cover authentication and database dependencies in later lectures.

---

## 12. Common Mistakes

### Mistake 1: Calling the Dependency Manually

Incorrect:

```python
pagination: dict = Depends(get_pagination())
```

Correct:

```python
pagination: dict = Depends(get_pagination)
```

Pass the function itself so FastAPI can manage dependency resolution.

### Mistake 2: Repeating Shared Logic

If multiple endpoints need the same validation or setup logic, consider extracting it into a dependency.

### Mistake 3: Thinking Dependencies Must Be Asynchronous

Dependencies can be synchronous or asynchronous.

Synchronous dependency:

```python
def get_data():
    return {"value": 10}
```

Asynchronous dependency:

```python
async def get_data():
    return {"value": 10}
```

FastAPI supports both.

### Mistake 4: Assuming `Depends()` Automatically Creates a Database

`Depends()` does not automatically create a database connection. You must define a dependency that creates, retrieves, or manages the required resource.

### Mistake 5: Confusing Dependency Injection With a Normal Function Call

A normal function call is controlled by your code.

With `Depends()`, FastAPI resolves the dependency as part of processing the request, including its parameters and dependency chain.

---

## 13. Interview Questions

### Q1. What is Dependency Injection?

A technique in which required resources or functionality are provided to a function instead of being created directly inside it.

### Q2. What is `Depends()`?

`Depends()` declares a dependency that FastAPI should resolve when processing a request.

### Q3. Why use Dependency Injection?

It reduces duplicated code, improves separation of concerns, and makes common functionality easier to maintain and test.

### Q4. Can dependencies accept parameters?

Yes. FastAPI resolves supported dependency parameters from request data or other dependencies.

### Q5. Can multiple endpoints share one dependency?

Yes. Multiple endpoints can use the same dependency function or class.

### Q6. Can dependencies be synchronous or asynchronous?

Yes. FastAPI supports both synchronous and asynchronous dependencies.

### Q7. What is dependency caching?

FastAPI normally reuses a dependency's result within a single request when the same dependency is required multiple times.

### Q8. What is `Annotated` used for?

`Annotated` lets us combine a type annotation with additional metadata, such as `Depends()`.

### Q9. Can one dependency depend on another?

Yes. FastAPI supports nested dependencies and resolves the dependency chain.

### Q10. What are common real-world dependencies?

Database sessions, authentication, current user information, shared query parameters, and configuration settings.

---

## 14. Practice

### Practice 1: Pagination Dependency

Create a `get_pagination()` dependency.

Requirements:
- `page` defaults to `1` and must be at least `1`.
- `limit` defaults to `10` and must be between `1` and `100`.
- Use it in `/students` and `/teachers`.

### Practice 2: Common Search Parameters

Create a dependency that accepts:
- `search: str | None = None`
- `page: int = 1`
- `limit: int = 10`

Use it in two endpoints.

### Practice 3: Current User Dependency

Create a `get_current_user()` dependency that returns a sample user dictionary.

Use it in `/profile`.

### Practice 4: Class Dependency

Create a `CommonParams` class that accepts `page` and `limit`.

Use it in `/students` through `Depends()`.

### Practice 5: Use `Annotated`

Rewrite the pagination example using:

```python
PaginationDep = Annotated[dict, Depends(get_pagination)]
```

Use the reusable annotation in multiple endpoints.

---

## Quick Revision

- `Depends()` declares a dependency.
- Dependencies help reuse common logic.
- Dependencies can be functions or classes.
- Dependencies can have their own parameters and dependencies.
- Dependencies can be synchronous or asynchronous.
- FastAPI normally caches repeated dependency results within a request.
- `Annotated` provides a clean way to declare reusable dependencies.
- Common real-world uses include database sessions and authentication.

---

## Next Lecture

### Lecture 9 — FastAPI Project Structure

Topics:
- Why a single `main.py` file becomes difficult to maintain.
- Separating routes, schemas, and business logic.
- Using `APIRouter`.
- Organizing a FastAPI application into modules.
- Understanding a basic project structure.
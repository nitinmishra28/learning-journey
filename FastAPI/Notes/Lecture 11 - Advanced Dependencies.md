# FastAPI — Lecture 11: Advanced Dependencies

My personal notes for understanding advanced dependency patterns in FastAPI.

## 1. What Are Advanced Dependencies?

In the previous lecture, we learned how `Depends()` helps us reuse common functionality across endpoints.

Advanced dependencies cover concepts such as:

- Nested dependencies
- Dependencies depending on other dependencies
- `yield` dependencies
- Resource cleanup
- Dependency overrides for testing
- Dependency caching
- Reusable dependency patterns

These concepts are useful when building real-world FastAPI applications with databases, authentication, and external services.

---

## 2. Nested Dependencies

A nested dependency is a dependency that uses another dependency.

For example, an endpoint needs the current user, and obtaining the current user requires validating a token.

The dependency flow looks like this:

```text
API Endpoint
     |
     v
get_current_user()
     |
     v
get_token()
     |
     v
Extract and validate token
```

### Example

```python
from typing import Annotated

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


async def get_token(
    authorization: str | None = Header(default=None)
) -> str:
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header is missing"
        )

    return authorization


async def get_current_user(
    token: Annotated[str, Depends(get_token)]
):
    return {
        "username": "nitin",
        "token": token
    }


@app.get("/profile")
async def get_profile(
    user: Annotated[dict, Depends(get_current_user)]
):
    return user
```

Request:

```text
GET /profile
Authorization: Bearer example-token
```

Example response:

```json
{
    "username": "nitin",
    "token": "Bearer example-token"
}
```

### How It Works

1. FastAPI receives the request.
2. The endpoint requires `get_current_user()`.
3. `get_current_user()` requires `get_token()`.
4. FastAPI resolves `get_token()` first.
5. Its result is passed into `get_current_user()`.
6. The resulting user data is passed to the endpoint.

**Important:** This is only an example of dependency chaining. It does not actually verify or decode a JWT. Real authentication must validate the token's signature, expiration, and relevant claims.

---

## 3. Dependencies Depending on Multiple Dependencies

A dependency can use more than one dependency.

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def get_page(page: int = 1):
    return page


def get_limit(limit: int = 10):
    return limit


def get_pagination(
    page: Annotated[int, Depends(get_page)],
    limit: Annotated[int, Depends(get_limit)]
):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/students")
async def get_students(
    pagination: Annotated[dict, Depends(get_pagination)]
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

Here, `get_pagination()` depends on both `get_page()` and `get_limit()`.

FastAPI resolves the dependencies and passes their results to `get_pagination()`.

---

## 4. Dependency Injection With `yield`

Sometimes a dependency needs to perform setup before an endpoint runs and cleanup afterward.

Examples include:

- Opening and closing a database session
- Acquiring and releasing a resource
- Creating and cleaning up a temporary resource

For this, we can use `yield` inside a dependency.

### Example

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def get_resource():
    print("Resource created")

    try:
        yield {"resource": "sample"}
    finally:
        print("Resource cleaned up")


@app.get("/resource")
def read_resource(
    resource: Annotated[dict, Depends(get_resource)]
):
    return resource
```

When the endpoint is called, the dependency:

1. Runs until it reaches `yield`.
2. Provides the yielded value to the endpoint.
3. Executes the cleanup code in `finally` when FastAPI finishes the dependency's lifecycle.

Example response:

```json
{
    "resource": "sample"
}
```

The `print()` statements appear in the server logs, not in the HTTP response.

**Remember:** `yield` dependencies are useful for managing resource lifecycles. Cleanup timing depends on the dependency scope and FastAPI's lifecycle handling.

---

## 5. `yield` Dependency With a Database Session

A common use case is managing a database session.

For example, using SQLAlchemy:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()

# Assume engine is configured for your database.
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/students")
def get_students(
    db: Annotated[Session, Depends(get_db)]
):
    # Use db to query the database.
    return {"message": "Database session available"}
```

`engine` must be configured before this example can run.

### Understanding the Code

- `SessionLocal()` creates a database session.
- `yield db` provides the session to the endpoint.
- `finally` ensures that `db.close()` is called when the dependency is cleaned up.

The endpoint does not need to create and close the session manually.

**Important:** Closing a session is not the same as committing a transaction. Database writes still need appropriate transaction handling.

---

## 6. Dependencies With `try`, `finally`, and Exceptions

The `finally` block runs whether the operation completes normally or raises an exception.

```python
def get_resource():
    resource = {"connected": True}

    try:
        yield resource
    finally:
        resource["connected"] = False
        print("Cleanup completed")
```

If the endpoint raises an exception after receiving the resource, the cleanup logic still runs as part of the dependency lifecycle.

This is one reason `try/finally` is useful for resource management.

---

## 7. Dependency Caching

FastAPI normally caches a dependency's result within a single request.

If the same dependency is required multiple times, FastAPI can reuse its result.

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def get_value():
    print("Dependency executed")
    return {"value": 100}


@app.get("/example")
async def example(
    first: Annotated[dict, Depends(get_value)],
    second: Annotated[dict, Depends(get_value)]
):
    return {
        "first": first,
        "second": second
    }
```

For a single request, the dependency normally executes once and its result is reused.

Example response:

```json
{
    "first": {
        "value": 100
    },
    "second": {
        "value": 100
    }
}
```

### Disabling the Cache

We can disable dependency caching for a particular declaration:

```python
Depends(get_value, use_cache=False)
```

For example:

```python
@app.get("/example")
async def example(
    first: Annotated[dict, Depends(get_value)],
    second: Annotated[
        dict,
        Depends(get_value, use_cache=False)
    ]
):
    return {
        "first": first,
        "second": second
    }
```

Here, the second declaration requests a fresh dependency execution rather than reusing the cached result.

**Remember:** Dependency caching is request-scoped. It is not a persistent application-wide cache like Redis.

---

## 8. Dependency Overrides

Dependency overrides allow us to replace a dependency with another implementation.

They are especially useful during testing.

For example, an endpoint depends on a function that returns the current user. During testing, we may want to provide a fake user instead of running real authentication.

### Application Code

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def get_current_user():
    return {
        "username": "real-user"
    }


@app.get("/profile")
async def get_profile(
    user: Annotated[dict, Depends(get_current_user)]
):
    return user
```

### Test Code

```python
from fastapi.testclient import TestClient

from app.main import app, get_current_user

client = TestClient(app)


def fake_current_user():
    return {
        "username": "test-user"
    }


app.dependency_overrides[get_current_user] = fake_current_user


def test_profile():
    response = client.get("/profile")

    assert response.status_code == 200
    assert response.json() == {
        "username": "test-user"
    }


def teardown_function():
    app.dependency_overrides = {}
```

The override tells FastAPI to use `fake_current_user()` whenever the application resolves `get_current_user()`.

### Important Points

- `app.dependency_overrides` is a dictionary.
- The original dependency is the key.
- The replacement dependency is the value.
- Clear overrides after testing so they do not affect other tests.

For larger test suites, fixtures are often a better way to manage overrides and cleanup.

---

## 9. Dependency Overrides With Pytest Fixtures

A fixture can manage dependency overrides safely.

```python
import pytest

from fastapi.testclient import TestClient

from app.main import app, get_current_user


def fake_current_user():
    return {"username": "test-user"}


@pytest.fixture
def client():
    app.dependency_overrides[get_current_user] = fake_current_user

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_profile(client):
    response = client.get("/profile")

    assert response.status_code == 200
    assert response.json() == {
        "username": "test-user"
    }
```

The fixture:

1. Registers the override.
2. Creates the test client.
3. Provides the client to the test.
4. Clears the overrides afterward.

This pattern helps isolate tests from real external services and authentication systems.

---

## 10. Subdependencies and Reuse

A dependency can be reused in other dependencies and endpoints.

For example:

```python
from typing import Annotated

from fastapi import Depends, FastAPI, Query

app = FastAPI()


def get_page(page: int = Query(default=1, ge=1)):
    return page


def get_limit(limit: int = Query(default=10, ge=1, le=100)):
    return limit


def get_pagination(
    page: Annotated[int, Depends(get_page)],
    limit: Annotated[int, Depends(get_limit)]
):
    return {
        "page": page,
        "limit": limit
    }


@app.get("/students")
async def get_students(
    pagination: Annotated[dict, Depends(get_pagination)]
):
    return pagination


@app.get("/teachers")
async def get_teachers(
    pagination: Annotated[dict, Depends(get_pagination)]
):
    return pagination
```

This lets us centralize validation and reuse it across endpoints.

However, avoid creating too many tiny dependencies when they make the code harder to understand. Extract dependencies when they represent reusable behavior or a clear responsibility.

---

## 11. When Should We Use Advanced Dependencies?

Use advanced dependencies when you need to:

- Resolve authentication and current-user information.
- Reuse common validation across endpoints.
- Manage database sessions.
- Acquire and clean up resources.
- Compose multiple dependencies.
- Replace real services with test implementations.
- Control repeated dependency execution.

For simple endpoints, a normal function may be sufficient. Use dependencies when they make shared logic clearer and easier to maintain.

---

## 12. Common Mistakes

### Mistake 1: Forgetting to Use `finally`

When managing resources, ensure cleanup happens even when an exception occurs.

```python
def get_resource():
    resource = create_resource()

    try:
        yield resource
    finally:
        resource.close()
```

`create_resource()` must be implemented for the specific resource being managed.

### Mistake 2: Assuming `yield` Commits Database Changes

`yield` manages resource setup and cleanup. It does not automatically commit database transactions.

### Mistake 3: Forgetting to Clear Test Overrides

Overrides can affect subsequent tests if they are not cleared.

### Mistake 4: Assuming Caching Is Global

FastAPI's default dependency cache is scoped to a request, not across all requests.

### Mistake 5: Using Dependencies for Everything

Not every function needs `Depends()`. Use dependencies when FastAPI needs to resolve shared functionality as part of request processing.

### Mistake 6: Assuming a Dependency Validates Authentication Automatically

A dependency only performs the logic you implement. Real authentication requires proper credential or token verification.

---

## 13. Interview Questions

### Q1. What is a nested dependency?

A dependency that uses one or more other dependencies.

### Q2. What is a `yield` dependency?

A dependency that yields a value to the endpoint and can perform cleanup when its lifecycle ends.

### Q3. Why use `yield` with a database session?

It allows the session to be created, provided to the endpoint, and closed reliably.

### Q4. Does `yield` automatically commit a transaction?

No. Transaction commits and rollbacks must be handled separately according to the application's database strategy.

### Q5. What is dependency caching?

FastAPI normally reuses the result of the same dependency within a request.

### Q6. How can dependency caching be disabled?

Use `Depends(dependency, use_cache=False)`.

### Q7. What are dependency overrides?

A way to replace dependencies with alternative implementations, especially during tests.

### Q8. What is `app.dependency_overrides`?

A dictionary that maps original dependency callables to replacement callables.

### Q9. Can a dependency depend on multiple other dependencies?

Yes. FastAPI resolves the dependency graph and supplies the results to the dependent function.

### Q10. What is the difference between a normal function and a dependency?

A normal function is called directly by application code. A dependency is resolved by FastAPI when processing the request through mechanisms such as `Depends()`.

---

## 14. Practice

### Practice 1: Nested Dependencies

Create:

- `get_token()`
- `get_current_user()`
- `/profile`

Make `get_current_user()` depend on `get_token()`.

### Practice 2: Pagination Dependencies

Create separate dependencies for `page` and `limit`.

Combine them into `get_pagination()` and reuse it in `/students` and `/teachers`.

### Practice 3: Resource Cleanup

Create a dependency using `yield`.

Print a setup message before `yield` and a cleanup message inside `finally`.

### Practice 4: Database Session

Write a `get_db()` dependency that creates a SQLAlchemy session, yields it, and closes it afterward.

You do not need to connect a real database yet; focus on understanding the lifecycle.

### Practice 5: Dependency Override

Create a `/profile` endpoint that depends on `get_current_user()`.

Write a test that overrides the dependency with a fake user.

### Practice 6: Dependency Caching

Use the same dependency twice in one endpoint.

Observe the number of executions, then try `use_cache=False`.

---

## Quick Revision

- Nested dependencies allow dependencies to depend on other dependencies.
- FastAPI resolves the dependency chain automatically.
- `yield` dependencies support resource setup and cleanup.
- Database sessions are a common use case for `yield`.
- Cleanup does not automatically commit database transactions.
- Dependency results are normally cached within a request.
- `use_cache=False` disables caching for a dependency declaration.
- `app.dependency_overrides` is useful for testing.
- Use dependencies to keep reusable logic separate from endpoint code.

---

## Next Lecture

### Lecture 12 — CRUD APIs

Topics:

- What CRUD means.
- Create, Read, Update, and Delete operations.
- Designing REST API endpoints.
- Using HTTP methods correctly.
- Request and response models.
- Implementing CRUD operations with in-memory data.
- Handling missing records.
- Status codes and API testing.
# FastAPI — Lecture 10: APIRouter

My personal notes for understanding **APIRouter and modular route organization** in FastAPI.

## 1. What Is APIRouter?

`APIRouter` is a FastAPI class used to group related API endpoints into separate modules.

Instead of defining every endpoint in `main.py`, we can create separate routers for different resources.

For example:
- `student.py` — student APIs
- `teacher.py` — teacher APIs
- `auth.py` — authentication APIs
- `fee.py` — fee management APIs

**Main benefit:** It keeps the application organized and makes route management easier.

---

## 2. Why Do We Need APIRouter?

Without `APIRouter`, we might write all endpoints in one file:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/students")
async def get_students():
    return {"students": []}


@app.get("/teachers")
async def get_teachers():
    return {"teachers": []}


@app.get("/fees")
async def get_fees():
    return {"fees": []}
```

As the application grows, this file becomes difficult to maintain.

With `APIRouter`, we can separate each resource into its own file.

---

## 3. Creating Your First Router

Suppose our project has this structure:

```text
fastapi_project/
└── app/
    ├── __init__.py
    ├── main.py
    └── routers/
        ├── __init__.py
        └── student.py
```

### Step 1: Create `app/routers/student.py`

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_students():
    return {
        "students": ["Nitin", "Rahul"]
    }


@router.get("/{student_id}")
async def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

Here:

- `APIRouter()` creates a router instance.
- `router` is used to register endpoints.
- `@router.get()` defines an endpoint on that router.

These endpoints are not registered with the main FastAPI application until we include the router.

---

## 4. Registering the Router

Create `app/main.py`:

```python
from fastapi import FastAPI
from app.routers import student

app = FastAPI()

app.include_router(student.router)


@app.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI"
    }
```

### Understanding `include_router()`

```python
app.include_router(student.router)
```

This registers all endpoints defined in `student.router` with the main application.

The resulting endpoints are:

```text
GET /
GET /
GET /{student_id}
```

The student router's paths are included exactly as defined because we have not added a prefix.

**Note:** The router's `GET /` and the application's `GET /` are both registered at `/`. Avoid this conflict in a real application by assigning a prefix to the student router.

---

## 5. Using a Prefix

A prefix adds a common path to every endpoint in a router.

Update `app/main.py`:

```python
from fastapi import FastAPI
from app.routers import student

app = FastAPI()

app.include_router(
    student.router,
    prefix="/students"
)
```

Our router contains:

```python
@router.get("/")
async def get_students():
    return {"students": ["Nitin", "Rahul"]}


@router.get("/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}
```

After applying the prefix, the resulting paths are:

```text
GET /students/
GET /students/{student_id}
```

For example:

```text
GET /students/
GET /students/10
```

The prefix is added to the route path. It does not change the Python function name.

**Remember:** If the router already defines a prefix, the final URL combines the router-level prefix and the prefix supplied to `include_router()`.

---

## 6. Using Tags

Tags group endpoints into sections in Swagger UI.

```python
app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)
```

Open:

```text
http://127.0.0.1:8000/docs
```

The student endpoints appear under the **Students** section.

Tags improve API documentation. They do not change the endpoint URL.

---

## 7. Creating Multiple Routers

Suppose we need student and teacher APIs.

### `app/routers/student.py`

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_students():
    return {"students": ["Nitin", "Rahul"]}


@router.get("/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}
```

### `app/routers/teacher.py`

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_teachers():
    return {"teachers": ["Amit", "Priya"]}


@router.get("/{teacher_id}")
async def get_teacher(teacher_id: int):
    return {"teacher_id": teacher_id}
```

### `app/main.py`

```python
from fastapi import FastAPI
from app.routers import student, teacher

app = FastAPI()

app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    teacher.router,
    prefix="/teachers",
    tags=["Teachers"]
)
```

Final endpoints:

```text
GET /students/
GET /students/10

GET /teachers/
GET /teachers/5
```

Each router manages its own resource.

---

## 8. Defining a Prefix Inside APIRouter

We can define the prefix directly when creating a router.

### `app/routers/student.py`

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
async def get_students():
    return {"students": []}


@router.get("/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id}
```

### `app/main.py`

```python
from fastapi import FastAPI
from app.routers import student

app = FastAPI()

app.include_router(student.router)
```

The resulting paths are:

```text
GET /students/
GET /students/{student_id}
```

This approach keeps the router's prefix and tags close to its endpoint definitions.

You can also supply a prefix or tags when including the router. If both locations specify a prefix, the prefixes are combined.

---

## 9. Router-Level Dependencies

Sometimes every endpoint in a router needs the same dependency.

For example, we may want to verify a request header before allowing access to any endpoint in an internal router.

We can define dependencies on `APIRouter`.

```python
from fastapi import APIRouter, Depends, Header, HTTPException


async def verify_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != "my-secret-key":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )


router = APIRouter(
    prefix="/internal",
    tags=["Internal"],
    dependencies=[Depends(verify_api_key)]
)


@router.get("/reports")
async def get_reports():
    return {"reports": []}


@router.get("/statistics")
async def get_statistics():
    return {"statistics": {}}
```

Both endpoints use the router-level dependency.

A request without the required header is rejected.

For example:

```text
GET /internal/reports
```

With the required header:

```text
X-API-Key: my-secret-key
```

the request passes this example's check.

**Important:** This is only a learning example. Do not hardcode real API keys in source code. Use environment-based configuration and an appropriate authentication mechanism in a real application.

Router-level dependencies are useful when a check must run for every endpoint in that router.

---

## 10. Dependencies at Different Levels

FastAPI supports dependencies at multiple levels.

### Application-Level Dependency

Applied across the application when configured through `FastAPI()`.

```python
app = FastAPI(
    dependencies=[Depends(verify_api_key)]
)
```

### Router-Level Dependency

Applied to all endpoints in one router.

```python
router = APIRouter(
    dependencies=[Depends(verify_api_key)]
)
```

### Endpoint-Level Dependency

Applied to a specific endpoint.

```python
@router.get(
    "/reports",
    dependencies=[Depends(verify_api_key)]
)
async def get_reports():
    return {"reports": []}
```

Use the appropriate level depending on where the dependency should apply.

---

## 11. `APIRouter` vs `FastAPI`

| `APIRouter` | `FastAPI` |
|---|---|
| Groups related endpoints | Creates the main application |
| Does not run as a standalone ASGI application | Is the ASGI application |
| Uses `@router.get()` and similar decorators | Uses `@app.get()` and similar decorators |
| Included using `app.include_router()` | Runs through an ASGI server such as Uvicorn |

Example:

```python
app = FastAPI()
router = APIRouter()

@router.get("/students")
async def get_students():
    return {"students": []}

app.include_router(router)
```

Here, `app` is the main application, while `router` groups the endpoint.

---

## 12. Common Mistakes

### Mistake 1: Forgetting to Include the Router

Creating a router alone does not register its endpoints with the application.

```python
app.include_router(student.router)
```

### Mistake 2: Forgetting the Prefix

If you expect `/students/10`, make sure the router has the correct prefix or the route explicitly includes `/students`.

### Mistake 3: Duplicate Routes

Registering multiple handlers for the same method and path can lead to confusing behavior. Use unique routes unless you intentionally need special routing behavior.

### Mistake 4: Incorrect Imports

For a project structure such as:

```text
app/
├── main.py
└── routers/
    └── student.py
```

you can import the router using:

```python
from app.routers import student
```

Run Uvicorn from the project root so the import paths resolve correctly.

### Mistake 5: Assuming Tags Change URLs

Tags only organize the generated API documentation. Prefixes change the URL paths.

---

## 13. Interview Questions

### Q1. What is `APIRouter`?

A FastAPI class used to group related endpoints and organize an application into separate modules.

### Q2. What does `include_router()` do?

It registers an `APIRouter`'s endpoints with the main FastAPI application.

### Q3. What is the purpose of a prefix?

A prefix adds a common path to all routes in a router.

### Q4. What is the purpose of tags?

Tags group related endpoints in Swagger UI and improve API documentation.

### Q5. Can we apply dependencies to an entire router?

Yes. Pass dependencies to `APIRouter(dependencies=[...])`.

### Q6. What is the difference between router-level and endpoint-level dependencies?

Router-level dependencies apply to all endpoints in the router. Endpoint-level dependencies apply to the specific endpoint where they are declared.

### Q7. Can an application have multiple routers?

Yes. An application can register multiple routers for different resources or features.

### Q8. Is `APIRouter` a replacement for `FastAPI`?

No. `FastAPI` creates the main application, and `APIRouter` organizes routes that are included in it.

---

## 14. Practice

Create an application with three routers:

- `student.py`
- `teacher.py`
- `fee.py`

Requirements:

1. Create a separate `APIRouter` in each file.
2. Add a list endpoint and a detail endpoint to each router.
3. Register all routers in `main.py`.
4. Use `/students`, `/teachers`, and `/fees` as prefixes.
5. Add tags so each resource has its own section in Swagger UI.
6. Add a dependency to the fee router that checks for a required header.
7. Run the application and test every endpoint through `/docs`.

Do not add database integration yet. Focus on understanding route organization, prefixes, tags, and dependencies.

---

## Quick Revision

- `APIRouter` groups related endpoints.
- `app.include_router()` registers a router with the application.
- `prefix` adds a common URL path.
- `tags` organize endpoints in Swagger UI.
- Router-level dependencies apply to all endpoints in that router.
- Endpoint-level dependencies apply to a specific endpoint.
- A FastAPI application can contain multiple routers.
- `APIRouter` improves organization but does not replace the main `FastAPI` application.

---

## Next Lecture

### Lecture 11 — Advanced Dependencies

Topics:

- Nested dependencies.
- Dependencies that depend on other dependencies.
- `yield` dependencies.
- Dependency cleanup.
- Dependency overrides for testing.
- Practical dependency patterns.
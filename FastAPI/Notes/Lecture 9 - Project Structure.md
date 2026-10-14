# FastAPI — Lecture 9: Project Structure

My personal notes for understanding how to organize a FastAPI application into separate files and folders.

## 1. Why Do We Need a Proper Project Structure?

When we start learning FastAPI, we usually write everything in one file, such as `main.py`.

For small applications, this is fine. But as an application grows, one file may contain:

- API endpoints
- Request and response schemas
- Database operations
- Business logic
- Authentication
- Configuration
- Dependencies

Keeping everything in one file makes the code difficult to maintain, test, and extend.

**Solution:** Separate the application into modules based on their responsibilities.

---

## 2. Starting With a Simple Structure

Initially, our project might look like this:

```text
fastapi_project/
└── main.py
```

Example `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI"}


@app.get("/students")
async def get_students():
    return {"students": ["Nitin", "Rahul"]}
```

This works, but as we add more endpoints and functionality, `main.py` can become difficult to manage.

---

## 3. Recommended Basic Project Structure

A better structure separates the application into different modules.

```text
fastapi_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── student.py
│   │   └── teacher.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── student.py
│   │   └── teacher.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   │
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── common.py
│   │
│   └── core/
│       ├── __init__.py
│       └── config.py
│
├── tests/
│   └── test_students.py
│
├── .env
├── .gitignore
└── requirements.txt
```

This is an example structure, not a mandatory FastAPI convention. The structure should match the application's size and complexity.

---

## 4. Understanding Each File and Folder

### `main.py`

The application's entry point.

Responsibilities:
- Create the FastAPI application.
- Register routers.
- Configure application-level middleware and lifecycle behavior when needed.

### `routers/`

Contains API endpoint definitions, grouped by feature or resource.

Examples:
- `student.py`
- `teacher.py`
- `auth.py`

### `schemas/`

Contains Pydantic models for validating request data and defining response structures.

Examples:
- `StudentCreate`
- `StudentResponse`
- `TeacherCreate`

### `services/`

Contains business logic.

Examples:
- Creating a student.
- Calculating fees.
- Processing admission rules.

### `dependencies/`

Contains reusable dependencies.

Examples:
- Current user.
- Common query parameters.
- Database session dependency.

### `core/`

Contains shared application configuration and core functionality.

Examples:
- Environment-based settings.
- Security configuration.
- Application-wide constants.

### `tests/`

Contains automated tests for API endpoints and application logic.

### `.env`

Contains local environment variables, such as database credentials and API keys.

Never commit secrets to GitHub.

### `requirements.txt`

Lists the Python packages required by the application.

---

## 5. What Is a Python Module?

A Python module is generally a Python file that can be imported into another Python file.

For example:

```text
app/
├── main.py
└── utils.py
```

`utils.py`:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

`main.py`:

```python
from utils import greet

print(greet("Nitin"))
```

Output:

```text
Hello, Nitin
```

This allows us to organize reusable functionality across files.

---

## 6. What Is a Python Package?

A Python package is a way to organize related modules into a directory hierarchy.

For example:

```text
app/
├── __init__.py
├── main.py
└── routers/
    ├── __init__.py
    └── student.py
```

The `routers` directory groups related modules.

An `__init__.py` file traditionally marks a directory as a regular Python package. Modern Python also supports namespace packages without it, but using `__init__.py` is common in application projects.

---

## 7. What Is `APIRouter`?

`APIRouter` allows us to group related endpoints in separate files instead of defining every route in `main.py`.

Import it from FastAPI:

```python
from fastapi import APIRouter
```

We will use it to separate student endpoints from the main application.

### Create `app/routers/student.py`

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

Here, `router` stores the student-related route definitions.

These endpoints are not available in the application until the router is included in the FastAPI app.

---

## 8. Registering a Router in `main.py`

Create `app/main.py`:

```python
from fastapi import FastAPI
from app.routers import student

app = FastAPI()

app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)


@app.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI"
    }
```

### Understanding `include_router()`

```python
app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)
```

- `student.router`: the router containing student endpoints.
- `prefix="/students"`: adds `/students` to the beginning of each route.
- `tags=["Students"]`: groups the endpoints under the Students section in Swagger UI.

The final endpoints are:

```text
GET /
GET /students/
GET /students/{student_id}
```

The router's original paths are combined with the prefix.

For example:

```python
@router.get("/{student_id}")
```

becomes:

```text
GET /students/{student_id}
```

---

## 9. Adding a Teacher Router

Create `app/routers/teacher.py`:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_teachers():
    return {
        "teachers": ["Amit", "Priya"]
    }


@router.get("/{teacher_id}")
async def get_teacher(teacher_id: int):
    return {
        "teacher_id": teacher_id
    }
```

Update `app/main.py`:

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


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI"}
```

Now the application contains separate route modules for students and teachers.

Example endpoints:

```text
GET /students/
GET /students/10
GET /teachers/
GET /teachers/5
```

Each resource has its own router file.

---

## 10. Separating Schemas From Routes

As the application grows, we should also separate Pydantic models from route definitions.

Create `app/schemas/student.py`:

```python
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

These models define the expected student data.

Update `app/routers/student.py`:

```python
from fastapi import APIRouter
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()

students = []


@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return new_student
```

This example uses an in-memory list for learning. Data will be lost when the application restarts, and this is not suitable for production storage.

The route handles HTTP requests, while the schema defines the data structure.

---

## 11. Separating Business Logic Into Services

Routes should not contain every business rule or database operation.

For example, create `app/services/student_service.py`:

```python
students = []


def create_student_record(name: str, age: int) -> dict:
    new_student = {
        "id": len(students) + 1,
        "name": name,
        "age": age
    }

    students.append(new_student)

    return new_student
```

Now update `app/routers/student.py`:

```python
from fastapi import APIRouter
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import create_student_record

router = APIRouter()


@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    return create_student_record(
        name=student.name,
        age=student.age
    )
```

### Why Separate Services?

- Business logic can be reused.
- Routes become easier to read.
- Logic can be tested independently.
- Changes are easier to maintain.

This is a simple example. In a real application, the service would usually work with a database repository or session.

---

## 12. Understanding the Request Flow

A typical request flow in this structure is:

```text
Client
  |
  v
FastAPI Application
  |
  v
Router
  |
  v
Request Validation (Pydantic)
  |
  v
Service / Business Logic
  |
  v
Database (when integrated)
  |
  v
Response
```

This is a conceptual flow. The exact sequence depends on the application's dependencies, middleware, and implementation.

---

## 13. Running the Application

From the project root, run:

```bash
uvicorn app.main:app --reload
```

Explanation:

- `app.main`: the Python module `main.py` inside the `app` package.
- `app`: the FastAPI application instance defined in `main.py`.
- `--reload`: restarts the development server when code changes.

Open:

```text
http://127.0.0.1:8000/docs
```

This opens Swagger UI, where we can inspect and test our endpoints.

If imports fail, check that you are running the command from the project root and that your package paths are correct.

---

## 14. Common Mistakes

### Mistake 1: Forgetting to Register a Router

Defining an `APIRouter` is not enough.

You must include it:

```python
app.include_router(student.router, prefix="/students")
```

Otherwise, its endpoints will not be registered in the application.

### Mistake 2: Using Incorrect Import Paths

For this structure:

```text
app/
├── main.py
└── routers/
    └── student.py
```

A suitable import is:

```python
from app.routers import student
```

Run Uvicorn from the project root so the `app` package can be imported correctly.

### Mistake 3: Putting Everything in `main.py`

Avoid placing all routes, schemas, business logic, and database operations in one file as the application grows.

### Mistake 4: Putting Business Logic Everywhere

Keep route handlers focused on handling HTTP requests. Move substantial business logic into service functions or appropriate modules.

### Mistake 5: Assuming This Structure Is Mandatory

FastAPI does not require a particular folder structure. Organize the application according to its size and complexity.

---

## 15. Interview Questions

### Q1. Why do we need a proper FastAPI project structure?

It improves readability, maintainability, testing, and separation of responsibilities.

### Q2. What is `APIRouter`?

`APIRouter` groups related endpoints so they can be maintained in separate modules and included in a FastAPI application.

### Q3. What does `app.include_router()` do?

It registers the routes defined in an `APIRouter` with the FastAPI application.

### Q4. What is the purpose of `prefix` in `include_router()`?

It adds a common URL prefix to every route in that router.

### Q5. Why separate schemas from routers?

Schemas define request and response data structures, while routers define API endpoints. Separating them makes the application easier to maintain.

### Q6. What is the purpose of a service layer?

A service layer contains reusable business logic, keeping route handlers focused on HTTP-related responsibilities.

### Q7. Does FastAPI enforce a specific project structure?

No. The developer chooses a structure suitable for the application's requirements.

### Q8. What is the difference between a module and a package?

A module is generally a Python file. A package organizes modules into a directory hierarchy.

---

## 16. Practice

Create a small FastAPI application with the following structure:

```text
fastapi_project/
└── app/
    ├── __init__.py
    ├── main.py
    ├── routers/
    │   ├── __init__.py
    │   ├── student.py
    │   └── teacher.py
    ├── schemas/
    │   ├── __init__.py
    │   └── student.py
    └── services/
        ├── __init__.py
        └── student_service.py
```

Requirements:

1. Create a home endpoint in `main.py`.
2. Create separate student and teacher routers.
3. Register both routers using `include_router()`.
4. Add a `StudentCreate` Pydantic model.
5. Create a service function that adds a student to an in-memory list.
6. Use the service function in the student router.
7. Add a response model to the create-student endpoint.
8. Run the application and test the endpoints through Swagger UI.

Do not add database integration yet. Focus on understanding imports, routers, schemas, and services.

---

## Quick Revision

- `main.py` creates and configures the FastAPI application.
- `APIRouter` groups related endpoints.
- `include_router()` registers routes with the application.
- `schemas/` contains Pydantic models.
- `services/` contains business logic.
- `dependencies/` contains reusable dependencies.
- `core/` contains shared configuration and core functionality.
- `tests/` contains automated tests.
- A proper project structure improves maintainability but is not imposed by FastAPI.

---

## Next Lecture

### Lecture 10 — APIRouter

Topics:

- Creating routers.
- Registering routers.
- URL prefixes.
- Tags in Swagger UI.
- Router-level dependencies.
- Organizing routes by feature.
- Common mistakes and interview questions.
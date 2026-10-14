# FastAPI — Lecture 12: CRUD APIs

My personal notes for understanding **CRUD operations and how to build REST APIs using FastAPI**.

## 1. What Is CRUD?

CRUD stands for four basic operations used to manage data in an application.

| Operation | Meaning | HTTP Method | Example |
|---|---|---|---|
| Create | Add new data | `POST` | Create a student |
| Read | Retrieve data | `GET` | Get all students |
| Update | Modify existing data | `PUT` / `PATCH` | Update student details |
| Delete | Remove data | `DELETE` | Delete a student |

Almost every backend application uses CRUD operations.

For example, in a School Management System:

- Create a student.
- Get all students.
- Get a particular student.
- Update student details.
- Delete a student.

---

## 2. What Is a REST API?

A REST API exposes resources through URLs and uses HTTP methods to perform operations on them.

For example:

```text
GET     /students
GET     /students/1
POST    /students
PUT     /students/1
PATCH   /students/1
DELETE  /students/1
```

Here, `students` is the resource.

The HTTP method tells the API what operation the client wants to perform.

**Important:** REST is an architectural style. Using HTTP methods and resource-based URLs helps us design APIs consistently.

---

## 3. Understanding HTTP Methods

### GET

Used to retrieve data.

```text
GET /students
GET /students/1
```

### POST

Used to create a new resource.

```text
POST /students
```

### PUT

Used to replace an existing resource representation.

```text
PUT /students/1
```

### PATCH

Used to partially update an existing resource.

```text
PATCH /students/1
```

### DELETE

Used to delete a resource.

```text
DELETE /students/1
```

**Remember:** `PUT` generally represents replacement, while `PATCH` represents partial modification. The exact behavior depends on how the endpoint is implemented.

---

## 4. Creating Our First CRUD API

For learning, we will use an in-memory list instead of a database.

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

students = [
    {
        "id": 1,
        "name": "Nitin",
        "age": 24
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23
    }
]


@app.get("/")
async def home():
    return {"message": "Student Management API"}
```

The `students` list stores our sample data.

**Important:** This data exists only in application memory. It is lost when the application restarts, and it is not suitable for production storage.

---

## 5. CREATE — POST API

The `POST` method is commonly used to create a resource.

### Step 1: Create a Request Model

We use Pydantic to validate incoming data.

```python
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)
```

Here:

- `name` must contain between 2 and 100 characters.
- `age` must be greater than `0` and less than or equal to `100`.

### Step 2: Create the Endpoint

```python
from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

students = []
next_student_id = 1


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)


@app.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    global next_student_id

    new_student = {
        "id": next_student_id,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)
    next_student_id += 1

    return new_student
```

Request:

```http
POST /students
Content-Type: application/json
```

Request body:

```json
{
    "name": "Amit",
    "age": 22
}
```

Response:

```json
{
    "id": 1,
    "name": "Amit",
    "age": 22
}
```

HTTP status code:

```text
201 Created
```

FastAPI validates the request body using `StudentCreate`.

**Note:** The counter is a simple learning solution. In a real application, a database should generate and manage unique IDs.

---

## 6. READ — GET All Students

The `GET` method retrieves data.

```python
@app.get("/students")
async def get_students():
    return students
```

Request:

```text
GET /students
```

Example response:

```json
[
    {
        "id": 1,
        "name": "Amit",
        "age": 22
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23
    }
]
```

The endpoint returns the current contents of the list.

If the list is empty, the response is:

```json
[]
```

---

## 7. READ — Get a Student by ID

We can use a path parameter to identify a particular student.

```python
from fastapi import HTTPException


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
```

Request:

```text
GET /students/1
```

Example response:

```json
{
    "id": 1,
    "name": "Amit",
    "age": 22
}
```

If the student does not exist:

```text
GET /students/999
```

Response:

```json
{
    "detail": "Student not found"
}
```

Status code:

```text
404 Not Found
```

**Remember:** A path parameter identifies the resource we want to retrieve.

---

## 8. UPDATE — PUT API

`PUT` is generally used to replace an existing resource representation.

For this example, we require both `name` and `age` when updating a student.

```python
from fastapi import HTTPException, status
from pydantic import BaseModel, Field


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)


@app.put("/students/{student_id}")
async def update_student(
    student_id: int,
    student_data: StudentUpdate
):
    for student in students:
        if student["id"] == student_id:
            student["name"] = student_data.name
            student["age"] = student_data.age

            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
```

Request:

```http
PUT /students/1
Content-Type: application/json
```

Request body:

```json
{
    "name": "Nitin Mishra",
    "age": 25
}
```

Response:

```json
{
    "id": 1,
    "name": "Nitin Mishra",
    "age": 25
}
```

If the student does not exist, the API returns `404 Not Found`.

### Important

In this example, `PUT` replaces all editable fields: `name` and `age`.

The student's `id` remains unchanged because it identifies the resource.

---

## 9. UPDATE — PATCH API

`PATCH` is used to modify only the fields supplied by the client.

For this operation, we create a separate model with optional fields.

```python
class StudentPatch(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    age: int | None = Field(
        default=None,
        gt=0,
        le=100
    )


@app.patch("/students/{student_id}")
async def patch_student(
    student_id: int,
    student_data: StudentPatch
):
    for student in students:
        if student["id"] == student_id:
            update_data = student_data.model_dump(
                exclude_unset=True
            )

            for field, value in update_data.items():
                if value is not None:
                    student[field] = value

            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
```

Request:

```http
PATCH /students/1
Content-Type: application/json
```

Request body:

```json
{
    "age": 26
}
```

Only the age changes. The name remains unchanged.

### Understanding `model_dump(exclude_unset=True)`

Suppose the client sends:

```json
{
    "age": 26
}
```

Then:

```python
student_data.model_dump(exclude_unset=True)
```

returns:

```python
{"age": 26}
```

It excludes fields that the client did not provide.

**Important:** `exclude_unset=True` distinguishes omitted fields from explicitly supplied fields. The example above intentionally ignores explicit `null` values; a production API should define its null-handling behavior clearly.

---

## 10. DELETE — Delete a Student

The `DELETE` method removes a resource.

```python
@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
```

Request:

```text
DELETE /students/1
```

Successful response:

```text
204 No Content
```

A `204` response must not contain a response body.

If the student does not exist, the API returns `404 Not Found`.

---

## 11. Important HTTP Status Codes

| Status Code | Meaning | Common Use |
|---|---|---|
| `200 OK` | Request succeeded | GET or successful update |
| `201 Created` | Resource created | Successful POST |
| `204 No Content` | Request succeeded without a response body | Successful DELETE |
| `400 Bad Request` | Request cannot be processed as sent | Application-specific request errors |
| `401 Unauthorized` | Authentication is missing or invalid | Authentication failures |
| `403 Forbidden` | Client is not allowed to perform the operation | Permission failures |
| `404 Not Found` | Resource does not exist | Missing student |
| `409 Conflict` | Request conflicts with current resource state | Duplicate or conflicting resource |
| `422 Unprocessable Entity` | Request validation failed | Invalid body or parameters |
| `500 Internal Server Error` | Unexpected server error | Unhandled application failure |

FastAPI automatically returns `422` for normal request validation failures.

We can set a success status code using the `status_code` parameter:

```python
from fastapi import status


@app.post(
    "/students",
    status_code=status.HTTP_201_CREATED
)
async def create_student(student: StudentCreate):
    ...
```

Using `status.HTTP_201_CREATED` is more readable than writing the numeric value directly.

---

## 12. Why Do We Use HTTPException?

`HTTPException` allows us to return an HTTP error response intentionally.

Example:

```python
from fastapi import HTTPException


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
```

If the student exists, the endpoint returns the student.

If the student does not exist, the endpoint raises an exception and FastAPI generates the corresponding error response.

We will cover error handling in more detail in a separate lecture.

---

## 13. Recommended CRUD Endpoint Design

A consistent resource-based API can look like this:

| Operation | Method | Endpoint |
|---|---|---|
| Create student | POST | `/students` |
| Get all students | GET | `/students` |
| Get one student | GET | `/students/{student_id}` |
| Replace student | PUT | `/students/{student_id}` |
| Partially update student | PATCH | `/students/{student_id}` |
| Delete student | DELETE | `/students/{student_id}` |

Prefer resource names such as `/students` instead of action-based paths such as `/createStudent` for conventional REST API design.

---

## 14. Request Models vs Response Models

Request models define what data the client can send.

Response models define the structure of data returned by the API.

Example:

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

Use the response model in the endpoint:

```python
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=201
)
async def create_student(student: StudentCreate):
    new_student = {
        "id": 1,
        "name": student.name,
        "age": student.age
    }

    return new_student
```

FastAPI validates and serializes the returned data according to the response model.

Response models also help document the API and control which fields are exposed.

---

## 15. Complete CRUD Example

The following example combines the CRUD operations in one file.

Create `main.py`:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Student CRUD API")

students = []
next_student_id = 1


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)


class StudentPatch(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    age: int | None = Field(
        default=None,
        gt=0,
        le=100
    )


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int


@app.get("/")
async def home():
    return {"message": "Student CRUD API"}


# CREATE
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_student(student_data: StudentCreate):
    global next_student_id

    new_student = {
        "id": next_student_id,
        "name": student_data.name,
        "age": student_data.age
    }

    students.append(new_student)
    next_student_id += 1

    return new_student


# READ ALL
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
async def get_students():
    return students


# READ ONE
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# REPLACE
@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
async def update_student(
    student_id: int,
    student_data: StudentUpdate
):
    for student in students:
        if student["id"] == student_id:
            student["name"] = student_data.name
            student["age"] = student_data.age
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# PARTIAL UPDATE
@app.patch(
    "/students/{student_id}",
    response_model=StudentResponse
)
async def patch_student(
    student_id: int,
    student_data: StudentPatch
):
    update_data = student_data.model_dump(
        exclude_unset=True
    )

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide at least one field to update"
        )

    if any(value is None for value in update_data.values()):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Fields cannot be null"
        )

    for student in students:
        if student["id"] == student_id:
            student.update(update_data)
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# DELETE
@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
```

### Run the Application

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can test all CRUD operations directly through the documentation interface.

**Limitations of this example:**

- Data is stored in memory and disappears after a restart.
- The ID counter is intended only for learning.
- There is no database, authentication, or authorization.
- Concurrent requests and multi-process deployments require proper persistent storage and ID management.

---

## 16. Common Mistakes

### Mistake 1: Using `POST` for Every Operation

Use HTTP methods consistently with the operation being performed.

### Mistake 2: Returning a Body With `204`

A `204 No Content` response must not contain a response body.

### Mistake 3: Not Checking Whether a Record Exists

When updating or deleting a resource, return an appropriate error if it does not exist.

### Mistake 4: Using the Same Model for Every Operation

Create, update, partial update, and response models often have different requirements.

### Mistake 5: Confusing PUT and PATCH

- `PUT`: replace the editable representation.
- `PATCH`: update only supplied fields.

### Mistake 6: Assuming an In-Memory List Is a Database

In-memory data is suitable for learning, but it is not persistent and is not a replacement for a database.

---

## 17. Interview Questions

### Q1. What does CRUD stand for?

Create, Read, Update, and Delete.

### Q2. Which HTTP method is used to create a resource?

Usually `POST`.

### Q3. What is the difference between PUT and PATCH?

`PUT` generally replaces a resource representation, while `PATCH` applies partial modifications.

### Q4. Which status code indicates successful creation?

`201 Created`.

### Q5. Which status code is commonly returned when a resource does not exist?

`404 Not Found`.

### Q6. Why use Pydantic models in CRUD APIs?

They validate incoming data and define clear request and response structures.

### Q7. Why use `response_model`?

It validates and serializes the returned data and documents the response structure.

### Q8. Why should we separate create and update schemas?

Create and update operations can require different fields and validation rules.

### Q9. Is an in-memory list suitable for production?

Generally, no. Its data is lost on restart, and it does not provide database persistence or reliable concurrent data management.

### Q10. What is idempotency?

An operation is idempotent when repeating the same request has the same intended effect as performing it once.

`GET`, `PUT`, and `DELETE` are defined as idempotent HTTP methods. `POST` is not generally idempotent.

---

## 18. Practice

Build a CRUD API for teachers.

Requirements:

1. Create a teacher using `POST /teachers`.
2. Retrieve all teachers using `GET /teachers`.
3. Retrieve one teacher using `GET /teachers/{teacher_id}`.
4. Replace teacher details using `PUT /teachers/{teacher_id}`.
5. Partially update teacher details using `PATCH /teachers/{teacher_id}`.
6. Delete a teacher using `DELETE /teachers/{teacher_id}`.
7. Create Pydantic request and response models.
8. Validate teacher names and ages.
9. Return `404` when the teacher does not exist.
10. Use suitable HTTP status codes.
11. Test successful and unsuccessful requests through Swagger UI.

Do not add database integration yet. Focus on understanding CRUD operations, request validation, response models, and error handling.

---

## Quick Revision

- CRUD means Create, Read, Update, and Delete.
- `POST` commonly creates resources.
- `GET` retrieves resources.
- `PUT` replaces a resource representation.
- `PATCH` partially updates a resource.
- `DELETE` removes a resource.
- Pydantic models validate request data.
- Response models define the expected response structure.
- `HTTPException` handles expected HTTP errors.
- Use `201` for successful creation, `404` for missing resources, and `204` for successful deletion without a body.
- In-memory storage is temporary; real applications generally use a database.

---

## Next Lecture

### Lecture 13 — SQLAlchemy Basics

Topics:

- What is SQLAlchemy?
- ORM concepts.
- ORM vs raw SQL.
- Connecting FastAPI to a database.
- Creating a database engine.
- Creating a session factory.
- Defining database models.
- Creating tables.
- Understanding database sessions.
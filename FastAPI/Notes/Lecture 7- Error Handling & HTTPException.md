# FastAPI — Lecture 7: Error Handling & HTTPException

## 1. What Is Error Handling?

Error handling means managing errors properly when something goes wrong in an application.

For example, in a Student Management API:

- A student does not exist.
- The client sends invalid data.
- The user is not authenticated.
- The user does not have permission.
- An unexpected server error occurs.

Instead of returning confusing responses, we should return meaningful HTTP status codes and error messages.

Example:

```json
{
    "detail": "Student not found"
}
```

---

## 2. Why Do We Need Error Handling?

Suppose we create an API to fetch a student:

```text
GET /students/100
```

If student `100` does not exist, we should not return a successful response containing incorrect data.

Instead, we should return:

```text
404 Not Found
```

with a meaningful message.

The expected flow is:

```text
Client Request
      ↓
FastAPI Endpoint
      ↓
Check Business Conditions
      ↓
Error Occurs?
      ↓
Return Appropriate HTTP Error
```

---

## 3. What Is HTTPException?

FastAPI provides `HTTPException` to raise HTTP errors from an endpoint or other application code.

Import it:

```python
from fastapi import FastAPI, HTTPException
```

Basic syntax:

```python
raise HTTPException(
    status_code=404,
    detail="Resource not found"
)
```

Here:

- `status_code` specifies the HTTP status code.
- `detail` contains the error message or details.

When this exception is raised, FastAPI stops the normal execution of that request handler and generates an HTTP error response.

---

## 4. Basic Example

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": 1,
        "name": "Nitin"
    }
```

### Request 1

```text
GET /students/1
```

Response:

```json
{
    "id": 1,
    "name": "Nitin"
}
```

Status code:

```text
200 OK
```

### Request 2

```text
GET /students/100
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

**Important:** This example uses a fixed condition. In a real application, we would check whether the requested student exists in the database.

---

## 5. Why Use `raise` Instead of `return`?

Consider:

```python
return {
    "detail": "Student not found"
}
```

This only returns a Python dictionary. Unless configured otherwise, FastAPI treats it as a normal successful response.

Now consider:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

This generates an HTTP error response with status code `404`.

Remember:

```text
return
  ↓
Returns data normally

raise HTTPException
  ↓
Stops normal execution and raises an HTTP error
```

---

## 6. Common HTTP Error Status Codes

| Status Code | Meaning | Example |
|---|---|---|
| 400 | Bad Request | Invalid business request |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Student does not exist |
| 405 | Method Not Allowed | Unsupported HTTP method for a route |
| 409 | Conflict | Duplicate resource or conflicting state |
| 422 | Validation Error | Invalid request parameters or body |
| 500 | Internal Server Error | Unexpected server failure |

You do not need to memorize every HTTP status code immediately. Focus on understanding when the commonly used codes apply.

---

## 7. Handling 400 — Bad Request

Use `400` when the request cannot be processed because of a client-side problem that is not better represented by another status code.

Example:

```python
@app.get("/students")
def get_students(age: int):

    if age < 0:
        raise HTTPException(
            status_code=400,
            detail="Age cannot be negative"
        )

    return {
        "age": age
    }
```

Request:

```text
GET /students?age=-5
```

Response:

```json
{
    "detail": "Age cannot be negative"
}
```

Status code:

```text
400 Bad Request
```

Note: FastAPI's automatic validation handles invalid types. Here, we are checking a business condition.

---

## 8. Handling 401 — Unauthorized

`401 Unauthorized` generally indicates that authentication is missing or invalid.

Example:

```python
@app.get("/profile")
def get_profile():

    is_authenticated = False

    if not is_authenticated:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    return {
        "message": "Profile data"
    }
```

Response:

```json
{
    "detail": "Authentication required"
}
```

This example demonstrates the error-handling concept only. The authentication check is a placeholder, not a real security implementation.

We will implement authentication properly in later lectures.

---

## 9. Handling 403 — Forbidden

`403 Forbidden` means the server refuses to allow an operation because the caller lacks the required permission.

Example:

```python
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    is_admin = False

    if not is_admin:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to delete students"
        )

    return {
        "message": "Student deleted"
    }
```

Response:

```json
{
    "detail": "You do not have permission to delete students"
}
```

Remember:

```text
401 → Authentication problem
403 → Permission problem
```

The permission check above is illustrative. Real authorization must use trusted user identity and permissions.

---

## 10. Handling 404 — Not Found

This is one of the most common errors in backend development.

Example:

```python
students = {
    1: "Nitin",
    2: "Rahul",
    3: "Aman"
}


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student_id,
        "name": students[student_id]
    }
```

Request:

```text
GET /students/10
```

Response:

```json
{
    "detail": "Student not found"
}
```

This example uses an in-memory dictionary instead of a database.

---

## 11. Handling 409 — Conflict

`409 Conflict` is useful when a request conflicts with the current state of a resource.

For example, a student email address must be unique.

```python
students = {
    "nitin@example.com": {
        "id": 1,
        "name": "Nitin"
    }
}


@app.post("/students")
def create_student(email: str):

    if email in students:
        raise HTTPException(
            status_code=409,
            detail="Student email already exists"
        )

    students[email] = {
        "id": len(students) + 1,
        "name": "New Student"
    }

    return {
        "message": "Student created"
    }
```

Request:

```text
POST /students?email=nitin@example.com
```

Response:

```json
{
    "detail": "Student email already exists"
}
```

Status code:

```text
409 Conflict
```

This example is for learning only. A real application should enforce uniqueness in the database as well.

---

## 12. Understanding 422 Validation Errors

FastAPI automatically validates request parameters and Pydantic request models.

Example:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

Request:

```text
GET /students/abc
```

The endpoint expects an integer, but receives `"abc"`.

FastAPI returns a validation error, commonly with status code:

```text
422 Unprocessable Entity
```

You generally do not need to manually raise `HTTPException` for ordinary type-validation errors.

FastAPI handles these automatically.

---

## 13. Understanding 500 — Internal Server Error

`500` indicates an unexpected server-side failure.

Example:

```python
@app.get("/calculate")
def calculate():
    result = 10 / 0

    return {
        "result": result
    }
```

The division by zero causes an unexpected error.

FastAPI returns a server error response.

**Important:** Do not expose internal stack traces, database credentials, secrets, or other sensitive implementation details to API clients.

Handle errors appropriately and log diagnostic information securely on the server.

---

## 14. Custom Error Messages

You can provide meaningful messages through `detail`.

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Student with the requested ID does not exist"
)
```

Another example:

```python
raise HTTPException(
    status_code=400,
    detail="The requested operation is not valid"
)
```

A useful error message should explain the problem without exposing sensitive information.

---

## 15. Using Status Constants

Instead of writing numeric status codes, you can use FastAPI's `status` constants.

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "id": student_id,
        "name": "Nitin"
    }
```

Common constants:

```python
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_401_UNAUTHORIZED
status.HTTP_403_FORBIDDEN
status.HTTP_404_NOT_FOUND
status.HTTP_409_CONFLICT
status.HTTP_422_UNPROCESSABLE_ENTITY
status.HTTP_500_INTERNAL_SERVER_ERROR
```

Using named constants makes the intent of your code clearer.

---

## 16. Adding Headers to HTTPException

You can also include headers in an HTTP error response.

```python
raise HTTPException(
    status_code=401,
    detail="Authentication required",
    headers={
        "WWW-Authenticate": "Bearer"
    }
)
```

This header is commonly used with bearer-token authentication challenges.

Authentication-specific behavior will be covered later.

---

## 17. What Is a Global Exception Handler?

Sometimes you want to handle a particular type of exception consistently across your entire application.

FastAPI supports custom exception handlers.

For example, you can customize how an application responds to a specific exception type.

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class StudentNotFoundError(Exception):
    pass


@app.exception_handler(StudentNotFoundError)
async def student_not_found_handler(
    request: Request,
    exc: StudentNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc)
        }
    )


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 1:
        raise StudentNotFoundError("Student not found")

    return {
        "id": 1,
        "name": "Nitin"
    }
```

When `StudentNotFoundError` is raised, the registered handler generates the response.

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

This approach is useful when a particular application error should be handled consistently across multiple endpoints.

---

## 18. HTTPException vs Custom Exception Handler

These solve different problems.

### HTTPException

Use it when you want to raise an HTTP error directly.

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

### Custom Exception Handler

Use it when you want to define how a particular exception type should be converted into an HTTP response.

```python
@app.exception_handler(StudentNotFoundError)
async def student_not_found_handler(request, exc):
    ...
```

Remember:

```text
HTTPException
    ↓
Raise an HTTP error

Custom Exception Handler
    ↓
Define how a specific exception is handled
```

You do not need to create custom exception classes for every error. Use them when they provide a clear benefit.

---

## 19. Raising HTTPException from a Helper Function

Error handling does not have to be inside the endpoint itself.

Example:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: "Nitin",
    2: "Rahul"
}


def find_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@app.get("/students/{student_id}")
def get_student(student_id: int):

    student_name = find_student(student_id)

    return {
        "id": student_id,
        "name": student_name
    }
```

Here:

```text
Endpoint
   ↓
find_student()
   ↓
Student found?
   ↓
Return student / Raise HTTPException
```

This helps keep endpoint functions cleaner.

---

## 20. Complete Example

Create `main.py`:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

students = {
    1: {
        "id": 1,
        "name": "Nitin",
        "age": 25
    },
    2: {
        "id": 2,
        "name": "Rahul",
        "age": 24
    }
}


@app.get("/")
def home():
    return {
        "message": "Student Management API"
    }


@app.get("/students")
def get_students():
    return {
        "students": list(students.values())
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return students[student_id]


@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student_id: int, name: str, age: int):

    if student_id in students:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student ID already exists"
        )

    if age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Age cannot be negative"
        )

    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    students[student_id] = student

    return student


@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    del students[student_id]

    return None
```

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

**Note:** The example uses an in-memory dictionary and simple query parameters for creation. Data will reset when the application restarts. We will learn proper request models and database integration in later lectures.

---

## 21. Common Mistakes

### Mistake 1 — Using `return` Instead of `raise`

Incorrect when an HTTP error is intended:

```python
return {
    "detail": "Student not found"
}
```

Correct:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

### Mistake 2 — Using the Wrong Status Code

Do not return `404` for every error.

```text
400 → Invalid request
401 → Authentication problem
403 → Permission problem
404 → Resource not found
409 → State conflict
422 → Request validation error
500 → Unexpected server failure
```

Choose the status code that accurately describes the problem.

### Mistake 3 — Exposing Sensitive Information

Avoid returning:

```json
{
    "detail": "Database password abc123 is incorrect"
}
```

Return a safe message instead:

```json
{
    "detail": "Unable to process the request"
}
```

Record useful diagnostic details in secure server-side logs.

### Mistake 4 — Catching Every Exception Without Handling It Properly

Avoid hiding all errors with a generic response that makes debugging impossible.

Handle expected errors explicitly and log unexpected failures appropriately.

### Mistake 5 — Using `HTTPException` for Everything

Use `HTTPException` for HTTP errors. Use normal return values for successful operations and custom exception handlers when consistent application-wide handling is useful.

---

## 22. Interview Questions

### Q1. What is `HTTPException` in FastAPI?

`HTTPException` is used to raise an HTTP error with a specific status code and detail message.

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

### Q2. What is the difference between `return` and `raise HTTPException`?

`return` normally returns a successful response unless a different response is explicitly configured.

`raise HTTPException` stops normal processing and generates an HTTP error response.

### Q3. What is the difference between 401 and 403?

- `401`: Authentication is missing or invalid.
- `403`: The request is understood, but the caller lacks permission.

### Q4. When should we return 404?

When the requested resource cannot be found.

### Q5. What is a 422 error in FastAPI?

FastAPI commonly uses `422` for request validation errors, such as an invalid type or a missing required field.

### Q6. What is a global exception handler?

A handler registered with `@app.exception_handler()` that defines how a particular exception type is converted into an HTTP response.

### Q7. Can we raise `HTTPException` inside a helper function?

Yes. It can be raised inside endpoint functions, helper functions, and other application code.

### Q8. What is the difference between an HTTPException and a custom exception?

`HTTPException` directly represents an HTTP error. A custom exception represents an application-specific error, which can be translated into an HTTP response using an exception handler.

---

## 23. Quick Revision

```text
HTTPException
      ↓
Raise an HTTP error
      ↓
status_code + detail
```

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

Remember:

```text
400 → Bad Request
401 → Authentication problem
403 → Permission denied
404 → Resource not found
409 → Conflict
422 → Validation error
500 → Internal server error
```

Also remember:

```text
Expected application error
          ↓
Handle explicitly

Unexpected server error
          ↓
Log securely and return a safe response
```

---

## 24. Practice

Build a small Student Management API using an in-memory dictionary.

### Requirements

1. Create `GET /students` to return all students.
2. Create `GET /students/{student_id}` to return one student.
3. Return `404` when a student does not exist.
4. Create a student endpoint that returns `409` if the ID already exists.
5. Reject negative ages with `400`.
6. Delete a student and return `204`.
7. Use meaningful error messages.
8. Test successful and unsuccessful requests using Swagger UI.

### Test Cases

| Scenario | Expected Result |
|---|---|
| Fetch an existing student | `200 OK` |
| Fetch a missing student | `404 Not Found` |
| Create a duplicate student ID | `409 Conflict` |
| Send a negative age | `400 Bad Request` |
| Delete an existing student | `204 No Content` |
| Send a non-integer path parameter | `422` validation error |

Do not use a database yet. Focus on applying error handling correctly.

---

## Next Lecture

### Lecture 8 — Dependency Injection: Basics

We will learn:

- What is dependency injection?
- Why do we need dependencies?
- The `Depends()` function
- Creating reusable dependency functions
- Sharing common logic between endpoints
- Dependencies with parameters
- How FastAPI executes dependencies
- Practical examples
- Interview questions
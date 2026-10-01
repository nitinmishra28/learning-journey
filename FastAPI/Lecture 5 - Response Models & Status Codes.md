# FastAPI — Lecture 5: Response Models & Status Codes

## 1. What is a Response Model?

A **response model** defines the structure of data that our API should return to the client.

In the previous lecture, we learned about **request models**.

```text
Client
   ↓
Request Body
   ↓
Pydantic Request Model
   ↓
FastAPI
   ↓
Response Model
   ↓
Client
```

Example:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

This tells FastAPI:

> The API response should contain `id`, `name`, and `age`.

---

# 2. Why Do We Need Response Models?

Suppose our database contains:

```text
id
name
email
password
age
```

We should **not** return the password to the client.

Without a response model, it can be easy to accidentally return extra data.

A response model allows us to control exactly what the API returns.

```text
Database
   ↓
id
name
email
password
age
   ↓
Response Model
   ↓
id
name
email
age
   ↓
Client
```

---

# 3. Creating a Response Model

Use `BaseModel` from Pydantic.

```python
from pydantic import BaseModel


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

Now we can use it with:

```python
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": "Nitin",
        "age": 25
    }
```

---

# 4. What is `response_model`?

`response_model` tells FastAPI:

> Validate and serialize the endpoint's returned data according to this model.

Example:

```python
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": "Nitin",
        "age": 25
    }
```

Here:

```text
response_model=StudentResponse
              ↓
Expected response structure
```

---

# 5. Response Model Filtering

Suppose our function returns:

```python
return {
    "id": 1,
    "name": "Nitin",
    "age": 25,
    "password": "secret123"
}
```

But our response model is:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

The response will contain only:

```json
{
    "id": 1,
    "name": "Nitin",
    "age": 25
}
```

The password is not included.

This is one of the important reasons to use response models.

---

# 6. Request Model vs Response Model

This is an important interview topic.

### Request Model

Defines what the client can send.

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
```

Used here:

```python
@app.post("/students")
def create_student(student: StudentCreate):
    ...
```

### Response Model

Defines what the API returns.

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

Used here:

```python
@app.post(
    "/students",
    response_model=StudentResponse
)
def create_student(student: StudentCreate):
    ...
```

---

# 7. Why Use Separate Request and Response Models?

Suppose the client sends:

```json
{
    "name": "Nitin",
    "age": 25,
    "email": "nitin@example.com",
    "password": "secret123"
}
```

The request model can accept the password:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str
```

But the response should not return it.

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
```

This gives us:

```text
Request
   ↓
StudentCreate
   ↓
Database
   ↓
StudentResponse
   ↓
Client
```

---

# 8. Complete Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):

    return {
        "id": 1,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "password": student.password
    }
```

Even though the function returns:

```text
password
```

the response model filters it out.

Response:

```json
{
    "id": 1,
    "name": "Nitin",
    "age": 25,
    "email": "nitin@example.com"
}
```

---

# 9. Response Validation

FastAPI also validates the returned data against the response model.

Example:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
```

If the endpoint returns:

```python
return {
    "id": 1,
    "name": "Nitin",
    "age": "hello"
}
```

the response does not match the expected schema.

FastAPI/Pydantic will detect the invalid response data.

This helps catch bugs in our backend code.

---

# 10. Returning a Pydantic Model

We can also explicitly return a Pydantic model.

```python
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):

    return StudentResponse(
        id=student_id,
        name="Nitin",
        age=25
    )
```

However, in many FastAPI applications, returning a dictionary or ORM object and allowing FastAPI to serialize it is also common.

---

# 11. List Response Models

Sometimes an endpoint returns a list of objects.

Example:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
```

Use:

```python
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students():

    return [
        {
            "id": 1,
            "name": "Nitin"
        },
        {
            "id": 2,
            "name": "Rahul"
        }
    ]
```

Response:

```json
[
    {
        "id": 1,
        "name": "Nitin"
    },
    {
        "id": 2,
        "name": "Rahul"
    }
]
```

---

# 12. Status Codes

An HTTP status code tells the client what happened with the request.

Examples:

```text
200 → Success
201 → Created
204 → No Content
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
422 → Validation Error
500 → Internal Server Error
```

---

# 13. 200 OK

`200 OK` means:

> The request was successfully processed.

Example:

```python
@app.get("/students")
def get_students():
    return {
        "message": "Students retrieved"
    }
```

By default, successful GET requests commonly return:

```text
200 OK
```

---

# 14. 201 Created

`201 Created` means:

> A new resource was successfully created.

For example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.post("/students", status_code=201)
def create_student():
    return {
        "message": "Student created"
    }
```

Now the response status is:

```text
201 Created
```

instead of the default successful response status.

---

# 15. 204 No Content

`204 No Content` means:

> The request was successful, but there is no response body.

Common example:

```text
DELETE /students/10
```

If the student was successfully deleted, the API may return:

```text
204 No Content
```

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    return None
```

A `204` response should not contain a response body.

---

# 16. 400 Bad Request

`400 Bad Request` means:

> The request is invalid or cannot be processed because of a client-side request problem.

Example situations:

```text
Invalid request format
Invalid parameter combination
Invalid business input
```

We will learn how to explicitly return HTTP errors using `HTTPException` in the next lecture.

---

# 17. 401 Unauthorized

`401 Unauthorized` generally means:

> Authentication is required or the provided authentication credentials are invalid.

Example:

```text
Client
   ↓
GET /profile
   ↓
No valid authentication
   ↓
401 Unauthorized
```

We will cover authentication and JWT later.

---

# 18. 403 Forbidden

`403 Forbidden` means:

> The server understands the request, but the client is not allowed to perform the operation.

Example:

```text
Logged-in user
      ↓
DELETE /users/10
      ↓
User does not have required permission
      ↓
403 Forbidden
```

Important distinction:

```text
401 → Authentication problem
403 → Permission/authorization problem
```

---

# 19. 404 Not Found

`404 Not Found` means:

> The requested resource was not found.

Example:

```text
GET /students/999
```

If student `999` doesn't exist:

```text
404 Not Found
```

---

# 20. 422 Unprocessable Entity

FastAPI commonly returns `422` for **request validation errors**.

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

Expected:

```text
student_id → int
```

Received:

```text
abc
```

FastAPI can return a validation error with status:

```text
422
```

The exact validation behavior can depend on the request and FastAPI/Pydantic version.

---

# 21. 500 Internal Server Error

`500 Internal Server Error` means:

> Something went wrong on the server while processing the request.

Example:

```python
@app.get("/students")
def get_students():
    result = 10 / 0
    return result
```

The division by zero causes a server-side error.

The client should generally receive a server error rather than details of internal implementation.

---

# 22. Setting Status Code in FastAPI

Use:

```python
status_code=
```

Example:

```python
@app.post("/students", status_code=201)
def create_student():
    return {
        "message": "Student created"
    }
```

You can also use the constant from FastAPI:

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.post(
    "/students",
    status_code=status.HTTP_201_CREATED
)
def create_student():
    return {
        "message": "Student created"
    }
```

Using `status.HTTP_201_CREATED` can make the code easier to understand.

---

# 23. Common Status Codes to Remember

For interviews and real-world development, remember these first:

| Status Code | Meaning | Common Use |
|---|---|---|
| 200 | OK | Successful GET/update |
| 201 | Created | Resource created |
| 204 | No Content | Successful delete/no body |
| 400 | Bad Request | Invalid request |
| 401 | Unauthorized | Authentication required/invalid |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Resource doesn't exist |
| 422 | Validation Error | Invalid request data |
| 500 | Internal Server Error | Server-side failure |

---

# 24. Complete Example — CRUD Style

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class StudentCreate(BaseModel):
    name: str
    age: int
    email: str


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str


@app.get(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def get_student(student_id: int):

    return {
        "id": student_id,
        "name": "Nitin",
        "age": 25,
        "email": "nitin@example.com"
    }


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):

    return {
        "id": 1,
        "name": student.name,
        "age": student.age,
        "email": student.email
    }


@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    return None
```

---

# 25. Response Model and Status Code Together

In a real API, you commonly use both:

```python
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
```

This tells FastAPI:

```text
response_model
      ↓
What data should be returned

status_code
      ↓
What HTTP status should be returned
```

---

# 26. Common Mistakes

### Mistake 1 — Returning Sensitive Data

Don't return:

```json
{
    "id": 1,
    "name": "Nitin",
    "password": "secret123"
}
```

when the client doesn't need the password.

Use a response model:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
```

---

### Mistake 2 — Using 200 for Everything

Don't blindly use:

```text
200
```

for every operation.

For resource creation:

```text
201 Created
```

can communicate the result more accurately.

For a successful operation with no response body:

```text
204 No Content
```

may be appropriate.

---

### Mistake 3 — Confusing 401 and 403

Remember:

```text
401 → Authentication
403 → Authorization / Permission
```

---

### Mistake 4 — Using 404 for Validation Errors

If the request data itself is invalid, `404` is usually not appropriate.

`404` means the requested resource was not found.

Validation errors are a different problem.

---

# 27. Interview Questions

### Q1. What is `response_model` in FastAPI?

`response_model` defines the expected structure of the API response.

Example:

```python
@app.get(
    "/students",
    response_model=StudentResponse
)
def get_student():
    ...
```

It is used for response validation, serialization, filtering, and API documentation.

---

### Q2. Why should we use separate request and response models?

Because the data required from the client may be different from the data we want to return.

For example:

```text
Request
 ↓
name
email
password

Response
 ↓
id
name
email
```

This helps protect sensitive fields and keeps API contracts clear.

---

### Q3. What is the difference between 200 and 201?

```text
200 OK
   ↓
Request succeeded

201 Created
   ↓
A new resource was created
```

---

### Q4. What is the difference between 401 and 403?

```text
401
 ↓
Authentication is missing/invalid

403
 ↓
Authentication may be present, but permission is denied
```

---

### Q5. What is 404?

`404 Not Found` means the requested resource could not be found.

---

### Q6. What is 422 in FastAPI?

FastAPI commonly uses `422 Unprocessable Entity` for request validation errors.

---

### Q7. What is 204?

`204 No Content` means the request succeeded but the response contains no body.

---

### Q8. Can `response_model` filter fields?

Yes.

Example:

```python
class StudentResponse(BaseModel):
    id: int
    name: str
```

If the endpoint returns additional fields, the response model can restrict the serialized response to the defined fields.

---

# 28. Quick Revision

## Request Model

```text
Client
  ↓
Request Body
  ↓
Request Model
  ↓
FastAPI
```

Defines:

> What data can come into the API?

---

## Response Model

```text
FastAPI
  ↓
Response Model
  ↓
Client
```

Defines:

> What data should go out of the API?

---

## Status Code

```text
200 → Success
201 → Created
204 → No Content
400 → Bad Request
401 → Authentication problem
403 → Permission problem
404 → Resource not found
422 → Validation error
500 → Server error
```

---

# 29. Practice

Create a Student API with:

### Request Model

```text
StudentCreate

name
age
email
password
```

### Response Model

```text
StudentResponse

id
name
age
email
```

Create:

```text
POST /students
```

Use:

```text
201 Created
```

Make sure the response does **not** contain:

```text
password
```

---

### Additional Practice

Create:

```text
GET /students/{student_id}
```

Use:

```text
response_model=StudentResponse
```

Then create:

```text
DELETE /students/{student_id}
```

Use:

```text
204 No Content
```

Test everything through:

```text
http://127.0.0.1:8000/docs
```

---

## Next Lecture

### Lecture 6 — Headers, Cookies & Forms

We will learn:

- What are HTTP headers?
- Reading headers in FastAPI
- Custom headers
- What are cookies?
- Reading cookies
- Setting cookies
- Forms
- When to use headers vs cookies vs request body
- Interview questions
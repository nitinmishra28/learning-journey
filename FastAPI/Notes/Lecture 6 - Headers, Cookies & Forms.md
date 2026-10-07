# FastAPI — Lecture 6: Headers, Cookies & Forms

## 1. What Are HTTP Headers?

HTTP headers are additional pieces of information sent along with an HTTP request or response.

They provide **metadata** about the request or response.

Example:

```text
GET /students

Headers:
Authorization: Bearer token
Content-Type: application/json
Accept: application/json
```

Think of it as:

```text
Request
│
├── URL
├── Method
├── Headers
└── Body
```

Headers are commonly used for:

- Authentication
- Content type
- Client information
- Request tracking
- Caching
- Custom application metadata

---

# 2. Common HTTP Headers

Some headers you will commonly see:

| Header | Purpose |
|---|---|
| `Content-Type` | Tells the server what type of data is being sent |
| `Accept` | Tells the server what response format the client accepts |
| `Authorization` | Sends authentication credentials/token |
| `User-Agent` | Information about the client |
| `Host` | Server/host information |
| `Cookie` | Sends cookies to the server |

Example:

```text
Authorization: Bearer eyJ...
Content-Type: application/json
Accept: application/json
```

---

# 3. Reading Headers in FastAPI

FastAPI provides the `Header` function.

```python
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/students")
def get_students(user_agent: str | None = Header(default=None)):
    return {
        "user_agent": user_agent
    }
```

Now FastAPI reads the:

```text
User-Agent
```

header and passes its value to:

```python
user_agent
```

---

# 4. Why Use `Header`?

Consider:

```python
user_agent: str | None = Header(default=None)
```

FastAPI understands:

```text
user_agent
     ↓
HTTP Header
```

Instead of treating it as a query parameter.

Without `Header()`:

```python
@app.get("/students")
def get_students(user_agent: str):
    ...
```

FastAPI would treat `user_agent` as a query parameter.

---

# 5. Header Name Conversion

FastAPI automatically converts underscores in Python parameter names to hyphens in HTTP header names.

Example:

```python
@app.get("/students")
def get_students(
    user_agent: str | None = Header(default=None)
):
    return {
        "user_agent": user_agent
    }
```

The Python variable is:

```text
user_agent
```

but the HTTP header is:

```text
User-Agent
```

FastAPI handles this conversion.

---

# 6. Custom Headers

We can also read custom headers.

Example:

```python
@app.get("/students")
def get_students(
    x_client_id: str | None = Header(default=None)
):
    return {
        "client_id": x_client_id
    }
```

Client sends:

```text
X-Client-Id: abc123
```

FastAPI maps:

```text
X-Client-Id
     ↓
x_client_id
```

---

# 7. Required Headers

A header can also be required.

Example:

```python
@app.get("/students")
def get_students(
    x_api_key: str = Header(...)
):
    return {
        "api_key": x_api_key
    }
```

The client must send:

```text
X-Api-Key: abc123
```

If it is missing, FastAPI returns a validation error.

However, authentication headers should normally be handled using FastAPI's security utilities rather than manually building an authentication system around a custom header. We will cover authentication later.

---

# 8. Reading Multiple Headers

We can read multiple headers.

```python
@app.get("/students")
def get_students(
    user_agent: str | None = Header(default=None),
    x_client_id: str | None = Header(default=None)
):
    return {
        "user_agent": user_agent,
        "client_id": x_client_id
    }
```

Possible request:

```text
User-Agent: Chrome
X-Client-Id: client-123
```

Response:

```json
{
    "user_agent": "Chrome",
    "client_id": "client-123"
}
```

---

# 9. `Header` with `alias`

Sometimes the Python variable name should be different from the actual HTTP header name.

Use `alias`.

```python
@app.get("/students")
def get_students(
    client_id: str | None = Header(
        default=None,
        alias="X-Client-ID"
    )
):
    return {
        "client_id": client_id
    }
```

The client sends:

```text
X-Client-ID: abc123
```

Python receives it as:

```python
client_id
```

---

# 10. Request Headers vs Query Parameters

This is important.

### Query Parameter

```text
GET /students?class_id=10
```

The data is part of the URL.

### Header

```text
GET /students

X-Client-ID: abc123
```

The data is sent in the HTTP headers.

Simple rule:

```text
Query Parameter
    ↓
Usually request-specific filters/options

Header
    ↓
Request metadata / credentials / client information
```

---

# 11. What Are Cookies?

A **cookie** is a small piece of data stored by the client, usually a browser, and sent back to the server with later requests.

Simple flow:

```text
Server
  ↓
Set Cookie
  ↓
Browser stores cookie
  ↓
Browser sends cookie
  ↓
Server
```

Example:

```text
session_id=abc123
```

---

# 12. Cookies in FastAPI

FastAPI provides `Cookie` to read cookies.

```python
from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/profile")
def get_profile(
    session_id: str | None = Cookie(default=None)
):
    return {
        "session_id": session_id
    }
```

If the client sends:

```text
Cookie: session_id=abc123
```

FastAPI gives:

```python
session_id = "abc123"
```

---

# 13. Setting a Cookie

To set a cookie, use `Response`.

```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/login")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123"
    )

    return {
        "message": "Login successful"
    }
```

The server sends a response containing a `Set-Cookie` header.

The browser can then store the cookie.

---

# 14. Reading a Cookie

```python
from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/profile")
def profile(
    session_id: str | None = Cookie(default=None)
):
    return {
        "session_id": session_id
    }
```

If the browser sends:

```text
Cookie: session_id=abc123
```

the response can be:

```json
{
    "session_id": "abc123"
}
```

---

# 15. Deleting a Cookie

Use:

```python
response.delete_cookie()
```

Example:

```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/logout")
def logout(response: Response):
    response.delete_cookie("session_id")

    return {
        "message": "Logged out"
    }
```

---

# 16. Important Cookie Options

When setting cookies, you may see options such as:

```python
response.set_cookie(
    key="session_id",
    value="abc123",
    httponly=True,
    secure=True,
    samesite="lax"
)
```

Important options:

### `httponly`

```text
httponly=True
```

Prevents normal JavaScript access to the cookie through `document.cookie`.

This is useful for cookies containing sensitive session information.

---

### `secure`

```text
secure=True
```

The browser should send the cookie only over HTTPS.

For local HTTP development, this can affect whether the browser sends the cookie.

---

### `samesite`

Controls cross-site cookie behavior.

Common values include:

```text
lax
strict
none
```

Cookie security becomes especially important when dealing with authentication.

We will revisit this in the authentication/security lectures.

---

# 17. Headers vs Cookies

Both are sent as part of HTTP requests, but their purposes differ.

### Headers

Usually used for:

```text
Authorization
Content-Type
Client information
Request metadata
```

Example:

```text
Authorization: Bearer token
```

### Cookies

Usually used for:

```text
Session information
Browser-based state
Authentication/session cookies
```

Example:

```text
session_id=abc123
```

---

# 18. What Are Forms?

An HTML form is a way for a client/browser to submit form data to a server.

Example:

```html
<form>
    <input name="username">
    <input name="password">
</form>
```

The submitted data may look like:

```text
username=Nitin
password=secret123
```

This is different from sending JSON.

---

# 19. JSON vs Form Data

JSON request:

```json
{
    "username": "Nitin",
    "password": "secret123"
}
```

Form request:

```text
username=Nitin&password=secret123
```

Typical content types:

```text
JSON
→ application/json

Form data
→ application/x-www-form-urlencoded

File upload
→ multipart/form-data
```

---

# 20. Using Forms in FastAPI

FastAPI provides `Form`.

```python
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
def login(
    username: str = Form(),
    password: str = Form()
):
    return {
        "username": username
    }
```

The client sends form data such as:

```text
username=Nitin
password=secret123
```

---

# 21. Installing Form Support

Depending on your FastAPI setup, form handling requires `python-multipart`.

Install it with:

```bash
pip install python-multipart
```

Without the required multipart package, FastAPI will report an error when using form-related functionality.

---

# 22. Why Are Forms Important?

Forms are commonly used for:

- HTML form submissions
- Login forms
- File uploads
- Multipart requests

For example, OAuth2 password-based flows commonly use form data.

We will use this knowledge later when implementing authentication.

---

# 23. JSON Body vs Form Data

This distinction is important.

### JSON

```python
@app.post("/students")
def create_student(student: Student):
    ...
```

Client sends:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Content type:

```text
application/json
```

### Form

```python
@app.post("/login")
def login(
    username: str = Form(),
    password: str = Form()
):
    ...
```

Client sends form fields.

Content type:

```text
application/x-www-form-urlencoded
```

---

# 24. Complete Example

```python
from fastapi import FastAPI, Header, Cookie, Form, Response

app = FastAPI()


@app.get("/headers")
def read_headers(
    user_agent: str | None = Header(default=None)
):
    return {
        "user_agent": user_agent
    }


@app.get("/profile")
def profile(
    session_id: str | None = Cookie(default=None)
):
    return {
        "session_id": session_id
    }


@app.get("/login")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123",
        httponly=True
    )

    return {
        "message": "Login successful"
    }


@app.post("/login-form")
def login_form(
    username: str = Form(),
    password: str = Form()
):
    return {
        "username": username
    }
```

---

# 25. When Should I Use What?

Use a **path parameter** when:

```text
You are identifying a resource.
```

Example:

```text
/students/10
```

Use a **query parameter** when:

```text
You are filtering/searching/paginating.
```

Example:

```text
/students?class_id=10
```

Use a **request body** when:

```text
You are sending structured data to the API.
```

Example:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Use a **header** when:

```text
You are sending request metadata or credentials.
```

Example:

```text
Authorization: Bearer token
```

Use a **cookie** when:

```text
You need browser-managed state/session information.
```

Example:

```text
session_id=abc123
```

Use **form data** when:

```text
The client submits HTML-style form data or a multipart request.
```

---

# 26. Common Mistakes

## Mistake 1 — Putting Everything in Headers

Don't use headers for normal business data like:

```text
student_name
student_age
student_address
```

Use a request body for structured resource data.

---

## Mistake 2 — Putting Sensitive Data in Query Parameters

Avoid:

```text
/login?username=Nitin&password=secret123
```

Query parameters are part of the URL and may appear in logs, browser history, proxies, or monitoring systems.

Use an appropriate authentication/request mechanism instead.

---

## Mistake 3 — Using JSON When an Endpoint Expects Form Data

If your endpoint uses:

```python
Form()
```

the client must send form data, not a normal JSON body.

---

## Mistake 4 — Assuming Cookies Are Automatically Secure

Cookies need appropriate security settings.

For sensitive session cookies, understand options such as:

```text
HttpOnly
Secure
SameSite
```

Don't treat cookies as automatically secure just because they are cookies.

---

# 27. Interview Questions

### Q1. What are HTTP headers?

Headers are metadata sent with HTTP requests and responses.

Examples:

```text
Content-Type
Authorization
Accept
User-Agent
```

---

### Q2. How do you read a header in FastAPI?

Using `Header`.

```python
from fastapi import Header

@app.get("/students")
def get_students(
    user_agent: str | None = Header(default=None)
):
    ...
```

---

### Q3. How do you read a cookie?

Using `Cookie`.

```python
from fastapi import Cookie

@app.get("/profile")
def profile(
    session_id: str | None = Cookie(default=None)
):
    ...
```

---

### Q4. How do you set a cookie?

Using `Response`.

```python
from fastapi import Response

@app.get("/login")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123"
    )

    return {"message": "Login successful"}
```

---

### Q5. How do you delete a cookie?

```python
response.delete_cookie("session_id")
```

---

### Q6. What is the difference between headers and cookies?

Headers are general HTTP metadata and can carry things such as authorization information.

Cookies are client-stored values that browsers can automatically send back to the server.

---

### Q7. How do you receive form data in FastAPI?

Using `Form`.

```python
from fastapi import Form

@app.post("/login")
def login(
    username: str = Form(),
    password: str = Form()
):
    ...
```

---

### Q8. What package is required for form handling?

```bash
pip install python-multipart
```

---

### Q9. What is the difference between JSON and form data?

JSON:

```text
Content-Type: application/json
```

Example:

```json
{
    "username": "Nitin",
    "password": "secret123"
}
```

Form data:

```text
Content-Type: application/x-www-form-urlencoded
```

Example:

```text
username=Nitin&password=secret123
```

---

# 28. Quick Revision

```text
PATH PARAMETER
    ↓
Identify a resource

/students/10
```

```text
QUERY PARAMETER
    ↓
Filter / Search / Pagination

/students?class_id=10
```

```text
REQUEST BODY
    ↓
Send structured data

{
    "name": "Nitin",
    "age": 25
}
```

```text
HEADER
    ↓
Request metadata / credentials

Authorization: Bearer token
```

```text
COOKIE
    ↓
Browser-managed state/session

session_id=abc123
```

```text
FORM
    ↓
Form-based request data

username=Nitin
password=secret123
```

---

# 29. Practice

Create the following APIs.

### 1. Read a custom header

Create:

```text
GET /client
```

Read:

```text
X-Client-ID
```

and return it.

---

### 2. Set a cookie

Create:

```text
GET /login
```

Set:

```text
session_id=abc123
```

with:

```text
httponly=True
```

---

### 3. Read the cookie

Create:

```text
GET /profile
```

Read:

```text
session_id
```

and return it.

---

### 4. Delete the cookie

Create:

```text
GET /logout
```

Delete:

```text
session_id
```

---

### 5. Form Login

Create:

```text
POST /login-form
```

Accept:

```text
username
password
```

using `Form()`.

---

### Important

Don't build JWT authentication yet.

The goal of this lecture is only to understand:

```text
Headers
Cookies
Forms
```

Authentication and authorization will be covered later.

---

## Next Lecture

### Lecture 7 — Error Handling & HTTPException

We will learn:

- Why API errors need to be handled
- `HTTPException`
- `status_code`
- Custom error messages
- Raising exceptions
- 404 errors
- 400 errors
- 401 and 403 errors
- Global exception handlers
- Custom exception handling
- Interview questions
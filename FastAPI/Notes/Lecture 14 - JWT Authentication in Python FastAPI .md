# JWT Authentication in Python FastAPI — Complete Guide

> **Goal:** Understand JWT authentication from beginner to advanced level, implement secure authentication APIs in FastAPI, and prepare for backend developer interviews.

## Table of Contents

1. What is Authentication and Authorization?
2. What is JWT?
3. Why Do We Need JWT?
4. How JWT Works Internally
5. JWT Structure: Header, Payload, Signature
6. Encoding vs Encryption vs Hashing
7. Important JWT Terminology
8. Access Token vs Refresh Token
9. JWT vs Session-Based Authentication
10. OAuth2 and JWT in FastAPI
11. `Annotated`, `Depends`, and `OAuth2PasswordBearer`
12. Password Hashing with Argon2
13. Project Setup
14. Complete JWT Authentication Implementation
15. How to Protect APIs
16. `get_current_user()` Explained
17. Role-Based Access Control
18. Refresh Token Implementation
19. Logout and Token Revocation
20. Database Integration with SQLAlchemy
21. JWT Security Best Practices
22. Common Errors and Debugging
23. Testing Authentication APIs
24. JWT Authentication Flow Diagram
25. Production-Ready Architecture
26. Common Interview Questions and Answers
27. Practical Exercises
28. Quick Revision Cheat Sheet
29. Further Learning Resources

---

# 1. What Is Authentication and Authorization?

These are two different concepts that are frequently asked about in backend interviews.

## 1.1 Authentication

Authentication answers:

**Who are you?**

It verifies the identity of a user.

Example:

A user enters:

- Email: `admin@school.com`
- Password: `mypassword`

The backend verifies the credentials and determines whether the user is legitimate.

## 1.2 Authorization

Authorization answers:

**What are you allowed to do?**

After authentication, the backend checks what actions the user can perform.

For example, in a School Management System:

| Role | Permissions |
|---|---|
| Admin | Manage students, teachers, fees and reports |
| Teacher | View assigned classes and update attendance |
| Student | View their profile, attendance and results |

A student may be authenticated successfully but must not be allowed to delete a teacher's account.

### Interview answer

Authentication verifies identity, whereas authorization determines permissions. JWT can carry identity and authorization-related claims, but the backend must still enforce access rules.

---

# 2. What Is JWT?

JWT stands for **JSON Web Token**.

It is a compact, URL-safe token format used to transfer claims between parties. In web applications, it is commonly used to represent an authenticated user's identity and permissions.

After successful login, the backend can generate a JWT and return it to the client.

The client sends that token with subsequent requests to protected APIs.

Example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

The backend verifies the token before allowing access.

### Important points

- JWT is a token format, not an authentication system by itself.
- JWTs are commonly signed, not encrypted.
- A valid signature does not automatically mean a user is authorized to perform every action.
- JWTs can be used without storing session state on the server, but applications may still store refresh tokens, revocation records, or other authentication state.

---

# 3. Why Do We Need JWT?

Suppose you build a School Management System with React as the frontend and FastAPI as the backend.

Your application has APIs such as:

```text
POST /auth/login
GET  /students
POST /students
GET  /teachers
GET  /admin/reports
```

You need a mechanism to identify users on every protected request.

One option is traditional session-based authentication. Another is token-based authentication using JWT.

A typical JWT flow looks like this:

1. User submits login credentials.
2. FastAPI verifies the credentials.
3. FastAPI creates an access token.
4. Frontend receives the token.
5. Frontend sends the token with protected API requests.
6. FastAPI validates the token and checks the user's permissions.
7. The API returns the requested data.

JWT is especially useful when multiple clients need to access the same backend, such as a web application, mobile application, and other services.

---

# 4. How JWT Works Internally

A JWT typically contains three parts separated by dots.

```text
HEADER.PAYLOAD.SIGNATURE
```

Example:

```text
xxxxx.yyyyy.zzzzz
```

Each part serves a different purpose.

1. Header: identifies the token type and signing algorithm.
2. Payload: contains claims such as the subject and expiration time.
3. Signature: helps verify that the signed content has not been modified.

Let's examine each part.

# 5. JWT Structure

## 5.1 Header

The header contains metadata about the token.

Example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Here:

- `alg` identifies the signing algorithm.
- `typ` identifies the token type.

`HS256` means HMAC using SHA-256.

The header is Base64URL-encoded before being included in the token.

## 5.2 Payload

The payload contains claims.

Example:

```json
{
  "sub": "user_101",
  "role": "admin",
  "iss": "school-api",
  "aud": "school-web",
  "iat": 1793000000,
  "exp": 1793000900
}
```

Explanation:

| Claim | Meaning |
|---|---|
| `sub` | Subject, usually the user's unique identifier |
| `role` | Application-specific role claim |
| `iss` | Issuer of the token |
| `aud` | Intended audience |
| `iat` | Issued-at timestamp |
| `exp` | Expiration timestamp |
| `nbf` | Optional time before which the token must not be accepted |
| `jti` | Optional unique token identifier |

Registered claims such as `sub`, `exp`, `iat`, `iss`, and `aud` have standardized meanings. `role` is a custom claim.

**Security warning:** The payload is not secret just because it is inside a JWT. Anyone possessing a normal signed JWT can generally decode its header and payload. Never place passwords, password hashes, API secrets, or confidential student information in the payload.

## 5.3 Signature

The signature is used to verify the integrity and authenticity of the signed token.

Conceptually, with HS256:

```text
signature = HMAC-SHA256(
    secret_key,
    base64url(header) + "." + base64url(payload)
)
```

The final JWT is:

```text
encoded_header.encoded_payload.encoded_signature
```

If someone changes the payload, the signature verification fails unless they can produce a valid signature using the trusted key.

### Why is the signature important?

Suppose the token contains:

```json
{
  "sub": "student_101",
  "role": "student"
}
```

An attacker changes the role to:

```json
{
  "sub": "student_101",
  "role": "admin"
}
```

The attacker cannot simply change the payload and still obtain a valid signature. The backend must verify the signature before trusting the claims.

However, a signed token can still be stolen and replayed. Signature verification alone does not prevent token theft.

---

# 6. Encoding vs Encryption vs Hashing

These three terms are different.

## 6.1 Encoding

Encoding transforms data into another representation.

Example:

```text
Hello → SGVsbG8=
```

Encoding is reversible and does not provide security by itself.

JWT uses Base64URL encoding for its header and payload.

## 6.2 Encryption

Encryption protects confidentiality by transforming readable data into ciphertext using cryptographic keys.

Only a party with the appropriate decryption key can recover the protected content.

A standard signed JWT is not encrypted. Encrypted JWTs can use the JWE format.

## 6.3 Hashing

Hashing transforms data into a fixed-size digest. Password storage should use a password-hashing algorithm such as Argon2, bcrypt, or scrypt, with suitable parameters.

Password hashing is designed to make guessing attacks expensive. It is not the same as ordinary fast hashing such as SHA-256.

### Interview question

**Is JWT encrypted?**

Not necessarily. A common JWT is signed and Base64URL-encoded, not encrypted. Anyone holding it can usually decode its payload, so sensitive information must not be stored in it.

---

# 7. Important JWT Terminology

### Signing key / secret key

The cryptographic key used to sign tokens or verify signatures, depending on the algorithm.

### Algorithm

The cryptographic algorithm used to sign the JWT, such as HS256 or RS256.

### Claims

Statements about the subject or token, such as user ID, issuer, audience and expiry.

### Expiration

The time after which the token must no longer be accepted.

### Bearer token

A credential presented by the client. Whoever possesses a bearer token may be able to use it, so it must be protected.

### Token verification

The process of validating the signature and the required claims, including expiration, issuer, and audience when configured.

### Stateless authentication

A design where the server does not need to look up a server-side session for every access-token request. It does not mean every aspect of authentication must be stateless.

---

# 8. Access Token vs Refresh Token

These are two different tokens that often work together.

## 8.1 Access token

The access token is sent with API requests to access protected resources.

Example:

```text
GET /students

Authorization: Bearer <access_token>
```

Access tokens should generally have a short lifetime.

Example lifetime: 15 minutes.

## 8.2 Refresh token

A refresh token is used to obtain a new access token without asking the user to log in again.

Example:

```text
POST /auth/refresh
```

Refresh tokens normally have a longer lifetime and require stronger lifecycle controls.

Example lifetime: several days, according to the application's risk requirements.

### Comparison

| Feature | Access token | Refresh token |
|---|---|---|
| Main purpose | Access protected APIs | Obtain new access tokens |
| Lifetime | Short | Longer |
| Sent with normal API requests | Yes | No |
| Stored or managed carefully | Yes | Yes, especially carefully |
| Can be revoked | Yes, with additional controls | Yes, through session/token state |

A refresh token should never be accepted as an access token.

For a production application, refresh tokens are commonly rotated on use and tracked in a server-side store. Reuse of an already rotated refresh token can be treated as a possible compromise.

---

# 9. JWT vs Session-Based Authentication

| Feature | Session-based | JWT-based |
|---|---|---|
| Server-side session state | Usually required | Not required for basic access-token validation |
| Client stores | Session identifier | Access token |
| Revocation | Often straightforward by invalidating the session | Requires additional mechanisms for immediate revocation |
| Scaling | Shared session store may be needed | Access tokens can be verified locally by multiple services |
| Token size | Usually small session identifier | Often larger |
| Best use | Traditional web applications | APIs and distributed clients, among other uses |

Neither approach is automatically more secure. Security depends on the implementation, storage, transport, expiration, revocation, and threat model.

---

# 10. OAuth2 and JWT in FastAPI

OAuth2 is an authorization framework. JWT is a token format.

They are related, but they are not the same thing.

FastAPI provides security utilities to help implement OAuth2-style authentication flows.

Important components include:

- `OAuth2PasswordBearer`
- `OAuth2PasswordRequestForm`
- `Depends`
- `Annotated`
- `HTTPBearer`

## 10.1 OAuth2PasswordBearer

Example:

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)
```

This tells FastAPI how to extract a bearer token from the request's `Authorization` header and documents the OAuth2 security scheme in OpenAPI.

It does not generate, decode, or validate JWTs by itself.

## 10.2 OAuth2PasswordRequestForm

Example:

```python
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

@app.post("/auth/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    username = form_data.username
    password = form_data.password
```

It reads form-encoded username and password fields.

It expects `application/x-www-form-urlencoded`, not a JSON request body.

**Important modern OAuth2 note:** The password grant represented by `OAuth2PasswordRequestForm` is a legacy OAuth2 flow and is not recommended for new OAuth2 authorization systems. It remains useful for learning FastAPI's traditional first-party username/password JWT tutorial pattern. For delegated login through an external identity provider, prefer an appropriate modern OAuth2 flow, commonly Authorization Code with PKCE, or OpenID Connect.

## 10.3 Depends

`Depends` tells FastAPI to resolve a dependency and provide its result to the endpoint.

```python
from typing import Annotated
from fastapi import Depends

def get_message():
    return "Hello"

@app.get("/")
async def home(
    message: Annotated[str, Depends(get_message)]
):
    return {"message": message}
```

FastAPI calls `get_message()` and supplies its return value as `message`.

## 10.4 Annotated

`Annotated` attaches metadata to a Python type.

```python
from typing import Annotated
from fastapi import Depends

Token = Annotated[str, Depends(oauth2_scheme)]
```

You can then use:

```python
@app.get("/protected")
async def protected_route(token: Token):
    return {"received_token": True}
```

The alias describes the type and the dependency that supplies it.

---

# 11. Project Setup

We will implement a small JWT authentication application using FastAPI, PyJWT and Argon2 password hashing.

## 11.1 Project structure

```text
fastapi-jwt/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── security.py
│   ├── dependencies.py
│   └── schemas.py
│
├── .env
├── .gitignore
└── requirements.txt
```

For learning, we will keep the initial example compact. In a production application, user and session data should be stored in a database, not only in an in-memory dictionary.

## 11.2 Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

## 11.3 Install dependencies

Create `requirements.txt`:

```text
fastapi
uvicorn[standard]
PyJWT
pwdlib[argon2]
python-multipart
python-dotenv
```

Install:

```bash
pip install -r requirements.txt
```

`python-multipart` is needed for the form-based login example.

## 11.4 Configure environment variables

Generate a strong random signing secret, for example using:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Place the generated value in `.env`:

```dotenv
JWT_SECRET_KEY=replace_with_generated_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
```

Never commit a real `.env` file to Git.

Add to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

Load configuration from environment variables. For production, use your deployment platform's secrets manager or equivalent secure configuration mechanism.

---

# 12. Complete JWT Authentication Implementation

This example demonstrates:

1. Password hashing.
2. Login verification.
3. JWT creation.
4. JWT signature and claim validation.
5. Protected endpoints.
6. Current-user lookup.
7. Role-based access control.

For simplicity, the users are in memory. Replace the demo user store with a database before using this design in a real application.

## 12.1 Create `app/security.py`

```python
import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv
from pwdlib import PasswordHash

load_dotenv()

SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15")
)

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    subject: str,
    role: str,
    expires_delta: timedelta | None = None
) -> str:
    now = datetime.now(timezone.utc)

    if expires_delta is None:
        expires_delta = timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    payload = {
        "sub": subject,
        "role": role,
        "iat": now,
        "exp": now + expires_delta,
        "iss": "school-api",
        "aud": "school-web",
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
```

### Explanation

`hash_password()` hashes a password before storage.

`verify_password()` checks a login password against its stored hash.

`create_access_token()` creates a signed JWT containing the user's ID, role, issue time, expiry time, issuer and audience.

PyJWT serializes the datetime claims into the appropriate JWT NumericDate representation.

The signing secret must remain private. All services verifying HS256 tokens must have access to the same secret, so asymmetric signing may be preferable in distributed systems.

## 12.2 Create `app/schemas.py`

```python
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    username: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

These models define the shape of the API responses.

## 12.3 Create `app/dependencies.py`

```python
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.security import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            issuer="school-api",
            audience="school-web",
            options={
                "require": [
                    "sub",
                    "exp",
                    "iat",
                    "iss",
                    "aud",
                ]
            },
        )

        user_id = payload.get("sub")

        if not isinstance(user_id, str) or not user_id:
            raise credentials_exception

    except jwt.InvalidTokenError:
        raise credentials_exception

    # Demo only: replace this lookup with a database query.
    from app.main import USERS

    user = USERS.get(user_id)

    if user is None:
        raise credentials_exception

    return user


CurrentUser = Annotated[dict, Depends(get_current_user)]
```

### What happens here?

`OAuth2PasswordBearer` extracts the bearer token.

`jwt.decode()` verifies the signature and validates the configured expiration, issuer and audience claims.

The code requires specific claims to be present and checks that the subject identifies a user.

Finally, the backend looks up the user. This is important because a token may remain cryptographically valid after the user is disabled or deleted.

The example uses an in-memory dictionary to keep the first implementation simple. Avoid importing a global user store from `main.py` in a larger application; inject a database-backed user repository instead.

## 12.4 Create `app/main.py`

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import CurrentUser
from app.schemas import TokenResponse, UserResponse
from app.security import (
    create_access_token,
    hash_password,
    verify_password,
)

app = FastAPI(title="School JWT Authentication")


# DEMO ONLY:
# Replace this in-memory store with a database.
USERS = {
    "user_101": {
        "id": "user_101",
        "username": "admin",
        "role": "admin",
        "hashed_password": hash_password("AdminPass123!"),
        "disabled": False,
    },
    "user_102": {
        "id": "user_102",
        "username": "teacher",
        "role": "teacher",
        "hashed_password": hash_password("TeacherPass123!"),
        "disabled": False,
    },
    "user_103": {
        "id": "user_103",
        "username": "student",
        "role": "student",
        "hashed_password": hash_password("StudentPass123!"),
        "disabled": False,
    },
}


def authenticate_user(username: str, password: str):
    for user in USERS.values():
        if user["username"] == username:
            if user["disabled"]:
                return None

            if not verify_password(
                password,
                user["hashed_password"]
            ):
                return None

            return user

    return None


@app.get("/")
async def home():
    return {"message": "School API is running"}


@app.post("/auth/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        subject=user["id"],
        role=user["role"],
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@app.get("/users/me", response_model=UserResponse)
async def read_current_user(user: CurrentUser):
    if user["disabled"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled",
        )

    return {
        "id": user["id"],
        "username": user["username"],
        "role": user["role"],
    }


@app.get("/students")
async def get_students(user: CurrentUser):
    return {
        "message": "Student list",
        "requested_by": user["username"],
    }


@app.get("/admin/reports")
async def get_admin_reports(user: CurrentUser):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return {
        "message": "Sensitive admin reports",
    }
```

**Important limitations of this demo:**

- The user database is in memory.
- Demo passwords are hardcoded and must never be used in production.
- There is no refresh-token system, logout revocation, rate limiting or account recovery.
- The example role check illustrates authorization, but real permissions should be enforced consistently across all sensitive endpoints.

## 12.5 Run the application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI provides a convenient way to test the login and protected endpoints.

---

# 13. How to Test JWT Authentication

## Step 1: Log in

Send a request to:

```text
POST /auth/login
```

The request body is form-encoded:

```text
username=admin
password=AdminPass123!
```

Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=AdminPass123%21"
```

Expected response:

```json
{
  "access_token": "<signed-jwt>",
  "token_type": "bearer"
}
```

The real token will be a long string.

## Step 2: Access a protected endpoint

```bash
curl "http://127.0.0.1:8000/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Expected response:

```json
{
  "id": "user_101",
  "username": "admin",
  "role": "admin"
}
```

## Step 3: Test an unauthorized request

Try the same endpoint without a token.

Expected result:

```text
401 Unauthorized
```

## Step 4: Test role-based authorization

Log in as the teacher and request:

```text
GET /admin/reports
```

Expected result:

```text
403 Forbidden
```

The teacher's token can be valid, but the teacher does not have permission to access the admin endpoint.

---

# 14. How Does `get_current_user()` Work?

This is one of the most important concepts for FastAPI interviews.

Consider:

```python
@app.get("/users/me")
async def read_current_user(user: CurrentUser):
    return user
```

`CurrentUser` is an `Annotated` alias for a dictionary supplied by `Depends(get_current_user)`.

The request goes through these steps:

1. FastAPI receives the request.
2. `OAuth2PasswordBearer` extracts the bearer token.
3. `get_current_user()` receives the token.
4. PyJWT verifies the token signature.
5. PyJWT checks the expiration and configured claims.
6. The backend extracts `sub`, the user identifier.
7. The backend looks up the user.
8. If the token or user is invalid, the request is rejected.
9. Otherwise, FastAPI injects the user into the endpoint.

The key idea is that **the endpoint does not need to manually decode the JWT every time**.

FastAPI's dependency system handles this reusable authentication logic.

---

# 15. Role-Based Access Control (RBAC)

RBAC means Role-Based Access Control.

The application assigns roles to users, and those roles determine the actions they may perform.

Example roles:

```text
admin
teacher
student
```

## 15.1 Create a reusable role dependency

In a separate `authorization.py` module:

```python
from typing import Annotated, Callable

from fastapi import Depends, HTTPException, status

from app.dependencies import get_current_user


def require_role(*allowed_roles: str) -> Callable:
    def role_checker(
        user: Annotated[dict, Depends(get_current_user)]
    ):
        if user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )

        return user

    return role_checker
```

Use it in an endpoint:

```python
from typing import Annotated
from fastapi import Depends

from app.authorization import require_role


@app.get("/admin/dashboard")
async def admin_dashboard(
    user: Annotated[
        dict,
        Depends(require_role("admin"))
    ]
):
    return {
        "message": "Welcome to the admin dashboard",
        "username": user["username"],
    }
```

Now the endpoint allows only users with the admin role.

### 401 vs 403

- `401 Unauthorized`: The request lacks valid authentication credentials.
- `403 Forbidden`: The user is authenticated but does not have permission for the requested action.

An application may choose to return a generic 401 for invalid credentials and a 403 for insufficient permissions.

**Production consideration:** Roles embedded in a JWT can become stale if permissions change before the token expires. For sensitive operations, consider fetching current permissions from the database or using a short token lifetime with appropriate revocation controls.

---

# 16. Refresh Token Implementation

A refresh-token flow allows a user to obtain a new access token without repeatedly entering a password.

The general flow is:

1. User logs in.
2. Server returns an access token and a refresh token.
3. Client uses the access token for normal API calls.
4. When the access token expires, the client submits the refresh token.
5. Server validates the refresh token and its session state.
6. Server issues a new access token and rotates the refresh token.
7. The old refresh token is invalidated.

## 16.1 Why should refresh tokens be different?

A refresh token has a different purpose from an access token.

Use separate token types and validation rules. For example:

```json
{
  "sub": "user_101",
  "type": "refresh",
  "exp": 1793600000
}
```

A refresh token must be accepted only by the refresh endpoint, not by protected resource APIs.

## 16.2 Recommended production design

For a robust implementation, maintain a server-side refresh-session record containing fields such as:

```text
session_id
user_id
refresh_token_hash
issued_at
expires_at
revoked_at
replaced_by_session_id
```

Store a hash of the refresh token or otherwise use secure opaque-token storage rather than keeping reusable bearer credentials in plaintext.

On refresh:

- Verify the refresh token's cryptographic validity, if it is a JWT.
- Validate its type, issuer, audience, subject and expiration.
- Verify that the corresponding session is active.
- Rotate the refresh token atomically.
- Revoke the previous token.
- Detect reuse of a previously rotated token.
- Revoke the relevant token family or session if compromise is suspected.

For many applications, an opaque random refresh token backed by a database is simpler to revoke and rotate safely than a self-contained refresh JWT.

**Do not treat a refresh token as valid merely because its signature is correct.** Its server-side session state must also be checked.

---

# 17. Logout and Token Revocation

JWT access tokens are often self-contained. If the server validates them locally without consulting a database, logging out does not automatically invalidate a token already issued.

This is an important distinction between JWT-based authentication and server-managed sessions.

Common approaches include:

### Approach 1: Short-lived access tokens

Use a short expiration so a stolen token becomes unusable relatively quickly.

This limits the exposure window but does not provide immediate revocation.

### Approach 2: Revoke refresh sessions

On logout, revoke the refresh session or token family. The client cannot use that session to obtain new access tokens.

An already-issued access token may still work until expiration unless additional checks exist.

### Approach 3: Access-token denylist

Track revoked access-token identifiers, such as `jti`, until their expiration.

Every relevant request must check the denylist. This adds server-side state and a database or cache lookup.

### Approach 4: Session-version or account-state checks

Keep an authentication version, session identifier, or account status in the database and validate it when required.

This can support account disablement and session invalidation, but it changes the performance and statefulness trade-offs.

### Logout checklist

- Revoke the refresh session.
- Clear client-side authentication state.
- Clear the refresh-token cookie if cookies are used.
- Prevent refresh-token reuse.
- Decide whether immediate access-token revocation is required.
- Invalidate server-side sessions or denylist entries when necessary.

---

# 18. Database Integration with SQLAlchemy

The in-memory user dictionary in our example is only for learning.

A real application should store users in a database, such as PostgreSQL, and use a proper user model.

A simplified user table could contain:

```text
users
-----
id
username
email
hashed_password
role
is_active
created_at
updated_at
```

A refresh-session table could contain:

```text
refresh_sessions
----------------
id
user_id
token_hash
expires_at
revoked_at
created_at
```

## 18.1 User model example

A simplified SQLAlchemy model:

```python
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255)
    )

    role: Mapped[str] = mapped_column(
        String(30),
        default="student"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
```

This model is illustrative; actual applications should include migrations, constraints, error handling and appropriate role/tenant relationships.

## 18.2 Database dependency

A typical SQLAlchemy session dependency looks like:

```python
from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

Then inject the database session:

```python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

DbSession = Annotated[Session, Depends(get_db)]
```

An endpoint can use:

```python
@app.get("/students")
def get_students(db: DbSession):
    # Query the database here.
    return {"message": "Database session injected"}
```

Use your actual SQLAlchemy query logic and return Pydantic response models in a real implementation.

## 18.3 How database-backed JWT authentication should work

1. Query the user by username or email.
2. Verify the submitted password against the stored password hash.
3. Check that the account is active.
4. Generate the access token using the user's immutable identifier.
5. During protected requests, validate the JWT.
6. Look up the user using the JWT subject.
7. Check account status and permissions.
8. Perform the requested operation.

For a multi-tenant school SaaS, also verify that the user belongs to the tenant associated with the requested school and that the resource being accessed belongs to the same tenant.

Never rely only on a client-supplied tenant ID or role.

---

# 19. JWT Security Best Practices

This section is particularly important for production systems and interviews.

## 19.1 Use strong signing keys

Use a cryptographically random key generated by a secure random-number generator.

Do not use:

```python
SECRET_KEY = "123456"
```

Do not hardcode secrets in source code or commit them to Git.

## 19.2 Allow only trusted algorithms

Always configure the accepted algorithms explicitly:

```python
jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)
```

Never choose the accepted verification algorithm based solely on the untrusted `alg` header supplied by the token.

If you use RSA or another asymmetric algorithm, verify using the expected public key and the exact configured algorithm.

## 19.3 Validate claims

Depending on your architecture, validate:

- Signature
- Expiration (`exp`)
- Issuer (`iss`)
- Audience (`aud`)
- Not-before (`nbf`), when used
- Subject (`sub`)
- Token type and required application-specific claims

Requiring important claims to be present helps prevent accepting tokens that are missing required security information.

## 19.4 Use short-lived access tokens

A shorter lifetime limits how long a stolen access token can be used.

Choose the lifetime based on your application's risk, user experience and refresh mechanism.

## 19.5 Never store passwords in JWTs

Do not include passwords, password hashes, API keys or sensitive personal information in JWT claims.

## 19.6 Use HTTPS

HTTPS protects credentials and tokens while they travel between the client and server.

Do not transmit authentication credentials over plain HTTP in production.

## 19.7 Protect tokens in the frontend

Browser storage has trade-offs.

- `localStorage`: persists across browser restarts, but JavaScript-accessible tokens can be stolen through successful XSS.
- `sessionStorage`: has similar JavaScript-accessibility risks, with a shorter storage lifetime.
- `HttpOnly` cookies: are not readable by JavaScript, reducing direct token theft through XSS, but cookie-based authentication needs CSRF protection and careful cookie configuration.

There is no universally best storage option for every application. Select a design based on the threat model.

## 19.8 Configure cookies correctly

For a cookie-based refresh-token design, consider:

```text
HttpOnly
Secure
SameSite
Path
Expires / Max-Age
```

The `Secure` attribute requires HTTPS. `HttpOnly` prevents ordinary JavaScript access to the cookie. `SameSite` helps mitigate some cross-site request scenarios but is not a complete substitute for CSRF protection.

## 19.9 Rate-limit login attempts

Rate limiting, monitoring and appropriate throttling help reduce brute-force attacks and credential stuffing.

Avoid returning detailed error messages that reveal whether a particular username exists.

## 19.10 Validate account status

A valid JWT should not automatically allow access to a deleted, disabled, suspended or otherwise unauthorized account.

## 19.11 Keep claims minimal

Store only what is needed for token validation and authorization. Keep sensitive or frequently changing information in the database.

## 19.12 Use asymmetric signing where appropriate

With HS256, every service verifying a token needs the shared secret. Any service that possesses that secret can also issue valid tokens.

With RS256, a trusted issuer signs with a private key and services can verify with a public key.

Asymmetric signing is useful when many services need to verify tokens but should not be able to issue them.

---

# 20. Common JWT Errors and Debugging

## Error 1: `401 Unauthorized`

Possible causes:

- Missing token.
- Invalid signature.
- Expired token.
- Wrong issuer or audience.
- Missing required claims.
- Malformed token.
- User no longer exists or is inactive.

Check that the client sends:

```text
Authorization: Bearer <token>
```

## Error 2: `403 Forbidden`

The request may be authenticated, but the user's role or permissions do not allow the requested operation.

Check your role dependency and resource-level authorization.

## Error 3: `422 Unprocessable Entity`

Common causes include missing or incorrectly formatted request fields.

For `OAuth2PasswordRequestForm`, send:

```text
Content-Type: application/x-www-form-urlencoded
```

Do not send the login fields as JSON when using this form dependency.

## Error 4: `ModuleNotFoundError`

Install the required package in the active virtual environment.

For example:

```bash
pip install PyJWT
pip install "pwdlib[argon2]"
pip install python-multipart
```

## Error 5: `Signature verification failed`

Possible causes:

- The wrong secret or public key.
- A modified token.
- A token signed by another service.
- Incorrect algorithm configuration.

Do not solve this by disabling signature verification.

## Error 6: `ExpiredSignatureError`

The access token has expired.

Use the refresh flow if the session remains valid, or require the user to authenticate again.

## Error 7: `InvalidAudienceError` or `InvalidIssuerError`

The token's issuer or audience does not match your configured values.

Ensure the issuer and audience used during issuance match the values required during verification.

## Error 8: A token works after logout

This may be expected if the system uses self-contained access tokens without immediate revocation.

If immediate invalidation is required, implement a denylist, session check, token-version mechanism or another revocation strategy.

---

# 21. Testing Authentication APIs

You should test both successful and unsuccessful authentication scenarios.

Example using FastAPI's `TestClient`:

```python
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "AdminPass123!",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["token_type"] == "bearer"
    assert "access_token" in body


def test_login_invalid_password():
    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_protected_route_without_token():
    response = client.get("/users/me")

    assert response.status_code == 401
```

Install the testing dependencies:

```bash
pip install pytest httpx
```

Run:

```bash
pytest
```

These tests use the demo application's hardcoded users. A production test suite should use an isolated test database and test fixtures.

### Additional test cases

- Valid token accesses the endpoint.
- Expired token is rejected.
- Tampered token is rejected.
- Wrong issuer is rejected.
- Wrong audience is rejected.
- Missing required claims are rejected.
- Deleted or disabled users are rejected.
- Students cannot access admin endpoints.
- Revoked refresh tokens cannot be reused.
- Invalid credentials do not disclose sensitive information.

---

# 22. JWT Authentication Flow Diagram

```mermaid
flowchart TD
    A[User submits login credentials] --> B[FastAPI login endpoint]
    B --> C[Fetch user from database]
    C --> D{Password valid and account active?}
    D -- No --> E[Return 401 Unauthorized]
    D -- Yes --> F[Create signed access JWT]
    F --> G[Return token to client]
    G --> H[Client requests protected API]
    H --> I[Extract Bearer token]
    I --> J[Verify signature and claims]
    J --> K{Token valid?}
    K -- No --> L[Return 401 Unauthorized]
    K -- Yes --> M[Load user and check permissions]
    M --> N{Authorized?}
    N -- No --> O[Return 403 Forbidden]
    N -- Yes --> P[Execute endpoint]
```

The JWT is not a replacement for password verification during login, user lookup where required, or authorization checks.

---

# 23. Production-Ready Architecture

For a larger FastAPI application, separate authentication responsibilities into modules.

```text
app/
├── main.py
├── core/
│   └── config.py
├── models/
│   ├── user.py
│   └── refresh_session.py
├── schemas/
│   ├── auth.py
│   └── user.py
├── api/
│   └── routes/
│       ├── auth.py
│       ├── users.py
│       └── students.py
├── services/
│   └── auth_service.py
├── repositories/
│   └── user_repository.py
├── security/
│   ├── password.py
│   ├── jwt.py
│   └── dependencies.py
└── database.py
```

### Responsibilities

| Component | Responsibility |
|---|---|
| `core/config.py` | Load application configuration and secrets |
| `models/` | SQLAlchemy database models |
| `schemas/` | Pydantic request and response models |
| `api/routes/` | HTTP endpoints |
| `services/` | Authentication and business logic |
| `repositories/` | Database queries |
| `security/jwt.py` | Token creation and validation |
| `security/password.py` | Password hashing and verification |
| `security/dependencies.py` | Current-user and authorization dependencies |
| `database.py` | Database engine and session configuration |

This separation improves maintainability and testing. It also avoids circular imports, such as importing the application module from an authentication dependency.

For a multi-tenant SaaS, authorization should check both the user's permissions and the tenant/resource relationship.

---

# 24. Common JWT Interview Questions and Answers

## Q1. What is JWT?

JWT is a compact, URL-safe format for carrying claims between parties. It is commonly used for token-based authentication and authorization.

## Q2. What are the three parts of JWT?

Header, payload and signature.

## Q3. Is JWT encrypted?

Not by default. Common signed JWTs use encoding and a digital signature or MAC, not encryption.

## Q4. Can we change the JWT payload?

You can alter the text, but the signature verification should fail when the modified token is validated.

## Q5. What is the difference between JWT and OAuth2?

JWT is a token format. OAuth2 is an authorization framework that defines flows and how clients obtain and use authorization credentials.

## Q6. What is the difference between authentication and authorization?

Authentication verifies identity. Authorization determines permitted actions.

## Q7. What is `OAuth2PasswordBearer`?

A FastAPI security utility that extracts a bearer token from the request and defines the OAuth2 bearer scheme for API documentation. It does not itself validate a JWT.

## Q8. What is `OAuth2PasswordRequestForm`?

A FastAPI dependency that parses form-encoded username and password fields and related OAuth2 form parameters.

## Q9. What is `Depends`?

FastAPI's dependency injection mechanism. It resolves a dependency and supplies its result to an endpoint or another dependency.

## Q10. What is `Annotated`?

A Python typing feature that attaches metadata to a type without replacing the underlying type.

## Q11. Why do we use access tokens?

To authorize requests to protected resources without resubmitting the user's password for every request.

## Q12. Why do we need refresh tokens?

To obtain new access tokens while a longer-lived session remains valid, reducing how often the user must log in again.

## Q13. What happens when a JWT expires?

The backend should reject it. The client can use a valid refresh session to obtain a new access token or ask the user to log in again.

## Q14. Can we log out by deleting a JWT from the frontend?

Deleting the local copy stops that client from sending it, but it does not invalidate a stolen or copied token. Server-side revocation is required for stronger logout guarantees.

## Q15. Where should the JWT secret be stored?

In protected environment configuration or a secrets manager, never in frontend code or a public repository.

## Q16. What is the difference between HS256 and RS256?

HS256 uses a shared secret for signing and verification. RS256 uses a private key for signing and a corresponding public key for verification.

## Q17. Why should JWTs have an expiration time?

Expiration limits how long a token remains usable if it is stolen or exposed.

## Q18. What is the purpose of the `sub` claim?

It identifies the subject of the token, typically the user ID.

## Q19. What is the purpose of `exp`?

It specifies the expiration time after which the token must no longer be accepted.

## Q20. What is the purpose of `aud`?

It identifies the intended audience. A service should reject a token that is not intended for it.

## Q21. What is the purpose of `iss`?

It identifies the token issuer, allowing the recipient to verify that the token came from an expected authority.

## Q22. Why do we use password hashing?

To avoid storing plaintext passwords and to make offline password guessing more expensive if the password database is compromised.

## Q23. Why is SHA-256 not recommended for password storage by itself?

It is a fast general-purpose hash, which makes large-scale password guessing easier. Password-specific algorithms such as Argon2 are designed to be more expensive.

## Q24. What is RBAC?

Role-Based Access Control. Permissions are associated with roles, and users are granted access based on their assigned roles.

## Q25. Why do we need `get_current_user()`?

It centralizes token validation and user resolution so protected endpoints can reuse the same authentication logic.

## Q26. What is the difference between 401 and 403?

401 means valid authentication credentials are missing or unavailable. 403 means the request is understood but the user is not permitted to perform the action.

## Q27. Can JWT be revoked?

A self-contained JWT does not have built-in revocation. Revocation requires mechanisms such as a denylist, session checks, token versions or short expiration times.

## Q28. What is token rotation?

Replacing a refresh token with a new one and invalidating the old token, helping detect reuse and limit the impact of token theft.

## Q29. Why should refresh tokens not be sent with every API request?

They are long-lived credentials used to establish new access tokens. Exposing them unnecessarily increases the consequences of theft.

## Q30. Is JWT always better than sessions?

No. Both have trade-offs. JWT can simplify distributed API authentication, while sessions can make revocation and centralized state management easier.

## Q31. What is the biggest security mistake in JWT implementation?

Common serious mistakes include accepting untrusted algorithms, skipping claim validation, exposing tokens, using weak keys, or treating token validity as sufficient authorization.

## Q32. How do you secure JWT authentication in a multi-tenant SaaS?

Use strong signing keys, validate tokens, enforce current account status and permissions, verify tenant/resource ownership on every relevant operation, protect refresh sessions, and use HTTPS and appropriate rate limits.

---

# 25. Practical Exercises

Complete these exercises to strengthen your understanding.

### Beginner

- [ ] Create a FastAPI project.
- [ ] Generate a JWT with a subject and expiration.
- [ ] Decode and verify the token.
- [ ] Implement a login endpoint.
- [ ] Hash passwords using Argon2.
- [ ] Create a protected `/users/me` endpoint.

### Intermediate

- [ ] Add an SQLAlchemy user model.
- [ ] Create a database-backed login endpoint.
- [ ] Add `get_current_user()`.
- [ ] Add reusable role-based dependencies.
- [ ] Return correct 401 and 403 responses.
- [ ] Test invalid, expired and tampered tokens.

### Advanced

- [ ] Implement refresh-token rotation.
- [ ] Store refresh-session records in PostgreSQL.
- [ ] Implement logout and session revocation.
- [ ] Add login rate limiting.
- [ ] Implement account disablement and permission checks.
- [ ] Add secure cookie-based refresh handling and CSRF protection where applicable.
- [ ] Add tenant-aware authorization.
- [ ] Configure key rotation and asymmetric signing where appropriate.

---

# 26. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| JWT | Compact token format containing claims |
| Header | Algorithm and token metadata |
| Payload | Claims |
| Signature | Integrity and authenticity verification |
| `sub` | Subject/user identifier |
| `exp` | Expiration time |
| `iss` | Issuer |
| `aud` | Intended audience |
| `OAuth2PasswordBearer` | Extracts bearer token |
| `OAuth2PasswordRequestForm` | Parses login form fields |
| `Depends` | Dependency injection |
| `Annotated` | Type plus metadata |
| Argon2 | Password hashing |
| Access token | Used to access protected resources |
| Refresh token | Used to renew access tokens |
| RBAC | Permissions based on roles |
| 401 | Authentication credentials are invalid or missing |
| 403 | Insufficient permission |
| HTTPS | Protects credentials in transit |
| Revocation | Requires additional state or a revocation strategy |

---

# 27. Further Learning Resources

Use the official documentation for current APIs and implementation details:

1. FastAPI security tutorial: https://fastapi.tiangolo.com/tutorial/security/
2. FastAPI OAuth2 with JWT: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
3. PyJWT documentation: https://pyjwt.readthedocs.io/
4. Python typing — `Annotated`: https://docs.python.org/3/library/typing.html#typing.Annotated
5. OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700
6. JSON Web Token specification (RFC 7519): https://www.rfc-editor.org/rfc/rfc7519

---

# Final Summary

The complete JWT authentication process can be remembered in this order:

**Register → Hash Password → Store User → Login → Verify Password → Generate Access Token → Send Bearer Token → Validate JWT → Load User → Check Permissions → Access Protected API.**

For production applications, extend the flow with refresh-token rotation, session revocation, account-status checks, rate limiting, secure token storage and tenant-aware authorization.

For your School Management SaaS, implement authentication as a reusable module first, then integrate it with PostgreSQL, student and teacher APIs, and role-based access control. This will give you a strong foundation for both real backend development and FastAPI interviews.

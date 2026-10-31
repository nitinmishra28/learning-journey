# Lecture 14 — PostgreSQL Integration with FastAPI

## 1. Introduction

In this lecture, we will learn how to integrate PostgreSQL with FastAPI using SQLAlchemy.

In previous lectures, we learned:
- SQLAlchemy basics
- Database models
- Database sessions
- CRUD operations
- Dependency injection for database connections

Now we will connect our FastAPI application to PostgreSQL.

### What is PostgreSQL?

PostgreSQL is an open-source relational database management system (RDBMS).

It stores data in tables consisting of rows and columns.

Example:

**students table**

| id | name | email | age |
|---|---|---|---|
| 1 | Rahul | rahul@gmail.com | 20 |
| 2 | Amit | amit@gmail.com | 22 |

### Why PostgreSQL?

- Open-source and reliable.
- Supports complex SQL queries.
- Supports relationships and transactions.
- Provides strong data integrity.
- Supports JSON and JSONB data types.
- Suitable for scalable backend applications.

---

## 2. PostgreSQL vs SQLite

| Feature | SQLite | PostgreSQL |
|---|---|---|
| Database type | File-based | Client-server |
| Setup | Very simple | Requires database setup |
| Concurrency | Limited write concurrency | Better concurrent access |
| Scalability | Small applications | Small to large applications |
| Relationships | Supported | Supported |
| JSON support | Basic | Advanced JSONB support |
| Production usage | Specific use cases | Common production choice |

**Important:** SQLite is useful for learning and lightweight applications. PostgreSQL is a strong choice for production backend systems.

---

## 3. Install PostgreSQL

Install PostgreSQL on your system.

Official website:

https://www.postgresql.org/download/

During installation, configure:
- Username: `postgres`
- Password: Your database password
- Port: `5432`
- Database: `school_management`

You can manage PostgreSQL using:
- pgAdmin
- psql command-line tool
- DBeaver

### Verify PostgreSQL

```bash
psql --version
```

Connect to PostgreSQL:

```bash
psql -U postgres
```

---

## 4. Create a Database

Connect to PostgreSQL and execute:

```sql
CREATE DATABASE school_management;
```

List databases:

```sql
\l
```

Connect to the database:

```sql
\c school_management
```

List tables:

```sql
\dt
```

---

## 5. Install Required Python Packages

Install SQLAlchemy and PostgreSQL driver.

```bash
pip install sqlalchemy psycopg2-binary
```

Packages:

| Package | Purpose |
|---|---|
| sqlalchemy | ORM for database operations |
| psycopg2-binary | PostgreSQL database driver |

**Note:** `psycopg2-binary` is used here for a synchronous SQLAlchemy connection. Async PostgreSQL connections will be covered separately if needed.

---

## 6. Understand the PostgreSQL Connection URL

SQLAlchemy requires a database connection URL.

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/school_management"
```

Let's understand its structure:

```text
postgresql://username:password@host:port/database_name
```

| Component | Description |
|---|---|
| postgresql | Database dialect |
| postgres | Database username |
| password | Database password |
| localhost | Database host |
| 5432 | PostgreSQL default port |
| school_management | Database name |

---

## 7. Project Structure

Let's organize our FastAPI application.

```text
school_management/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── student.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 8. Configure Environment Variables

Never hardcode database credentials directly in your source code.

Install python-dotenv:

```bash
pip install python-dotenv
```

Create `.env`:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/school_management
```

Add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
.venv/
```

Load the environment variable:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
```

**Important:** Never push your actual database password to GitHub.

---

## 9. Create Database Connection

Create `app/database/connection.py`.

```python
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

### Understand Each Component

**1. create_engine()**

```python
engine = create_engine(DATABASE_URL)
```

- Creates the SQLAlchemy database engine.
- Manages the connection to PostgreSQL.
- Acts as the interface between SQLAlchemy and the database.

**2. sessionmaker()**

```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

- Creates a factory for database sessions.
- Each request can get its own database session.
- `autocommit=False` means transactions are not automatically committed.
- `autoflush=False` disables automatic flushing before queries.
- `bind=engine` connects sessions to our database engine.

**3. declarative_base()**

```python
Base = declarative_base()
```

- Creates the base class for our SQLAlchemy models.
- All database models inherit from this Base.
- SQLAlchemy uses these models to understand database tables.

---

## 10. Create a Database Model

Create `app/models/student.py`.

```python
from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
```

### Understand the Model

| Field | Description |
|---|---|
| `__tablename__` | Name of the database table |
| `id` | Primary key |
| `name` | Student name |
| `email` | Unique email address |
| `age` | Student age |

The `Student` class represents the `students` table in PostgreSQL.

---

## 11. Create Database Tables

Import your models before calling `Base.metadata.create_all()`.

Create `app/main.py`.

```python
from fastapi import FastAPI

from app.database.connection import engine, Base
from app.models.student import Student

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "FastAPI connected with PostgreSQL"}
```

### What does create_all() do?

```python
Base.metadata.create_all(bind=engine)
```

- Checks the tables registered with SQLAlchemy Base.
- Creates tables that do not already exist.
- Does not automatically update existing tables when your model changes.

**Important:** `create_all()` is useful for initial learning and simple setups. For managing schema changes in real projects, we will use Alembic migrations in upcoming lectures.

---

## 12. Create Database Dependency

Add the following function to `app/database/connection.py`.

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

### Why do we need get_db()?

- Creates a new database session.
- Provides the session to the API endpoint.
- Keeps the session available while the endpoint executes.
- Closes the session after the request completes.

We will use FastAPI's `Depends()` to inject this session into API endpoints.

---

## 13. Create CRUD APIs

Create `app/routes/student.py`.

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.student import Student

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/")
def create_student(
    name: str,
    email: str,
    age: int,
    db: Session = Depends(get_db)
):

    student = Student(
        name=name,
        email=email,
        age=age
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


@router.get("/")
def get_students(db: Session = Depends(get_db)):

    return db.query(Student).all()


@router.get("/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = name
    student.age = age

    db.commit()
    db.refresh(student)

    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
```

**Note:** These endpoints use query parameters for simplicity. In a proper application, use Pydantic request schemas for create and update operations.

---

## 14. Register the Router

Update `app/main.py`.

```python
from fastapi import FastAPI

from app.routes.student import router as student_router

app = FastAPI()

app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "School Management API is running"}
```

---

## 15. Run the Application

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Test the following APIs:

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students/` | Create student |
| GET | `/students/` | Get all students |
| GET | `/students/{student_id}` | Get student by ID |
| PUT | `/students/{student_id}` | Update student |
| DELETE | `/students/{student_id}` | Delete student |

---

## 16. Important SQLAlchemy Database Operations

| Operation | Purpose |
|---|---|
| `db.add()` | Add an object to the session |
| `db.commit()` | Commit the transaction |
| `db.refresh()` | Refresh object with database values |
| `db.query()` | Start a query |
| `db.filter()` | Apply filtering conditions |
| `db.first()` | Return the first matching record |
| `db.all()` | Return all matching records |
| `db.delete()` | Mark an object for deletion |
| `db.rollback()` | Roll back the current transaction |
| `db.close()` | Close the session |

---

## 17. Important Concepts to Remember

### Engine vs Session

| Engine | Session |
|---|---|
| Manages database connectivity | Manages database operations |
| Created using `create_engine()` | Created using `sessionmaker()` |
| Usually shared by the application | Usually created per request |

### Commit vs Flush

**Commit:**

```python
db.commit()
```

Permanently commits the current transaction to the database.

**Flush:**

```python
db.flush()
```

Sends pending changes to the database within the current transaction without committing it.

### Refresh

```python
db.refresh(student)
```

Reloads the object with the latest values from the database.

### Rollback

```python
db.rollback()
```

Reverts uncommitted changes when a transaction fails.

---

## 18. Common Mistakes

1. Using the wrong PostgreSQL username or password.
2. Connecting to the wrong database or port.
3. Forgetting to install the PostgreSQL driver.
4. Forgetting to import models before `create_all()`.
5. Not closing database sessions.
6. Forgetting to call `commit()` after database modifications.
7. Committing transactions without handling errors.
8. Hardcoding database credentials in Python files.
9. Expecting `create_all()` to modify existing tables.
10. Sharing one SQLAlchemy session across concurrent requests.

---

## 19. Interview Questions

**Q1. Why do we use PostgreSQL with FastAPI?**

PostgreSQL is a relational database that provides transactions, data integrity, relationships and advanced SQL capabilities.

**Q2. What is SQLAlchemy?**

SQLAlchemy is a Python SQL toolkit and ORM that allows us to interact with databases using Python objects and SQL expressions.

**Q3. What is create_engine()?**

It creates the SQLAlchemy engine, which manages database connectivity.

**Q4. What is sessionmaker()?**

It creates a factory used to generate database sessions.

**Q5. What is the difference between Engine and Session?**

Engine manages database connectivity, while Session manages ORM operations and transactions.

**Q6. What is Base in SQLAlchemy?**

Base is the declarative base class from which ORM models inherit.

**Q7. What is the purpose of Depends(get_db)?**

It injects a database session into an API endpoint and allows us to manage the session lifecycle.

**Q8. What is the difference between commit() and flush()?**

Flush sends pending changes to the database without committing the transaction. Commit permanently commits the transaction.

**Q9. What is the purpose of create_all()?**

It creates database tables that do not already exist based on registered SQLAlchemy models.

**Q10. Why do we need Alembic?**

Alembic manages database schema changes through version-controlled migrations. We will cover it in detail in upcoming lectures.

---

## 20. Practical Assignment

Build a small Student Management API using FastAPI and PostgreSQL.

Requirements:

- Connect FastAPI with PostgreSQL.
- Create a `students` table.
- Implement Create Student API.
- Implement Get All Students API.
- Implement Get Student by ID API.
- Implement Update Student API.
- Implement Delete Student API.
- Use SQLAlchemy ORM.
- Use `Depends()` for database session management.
- Store database credentials in `.env`.
- Test all APIs using Swagger UI.

### Expected Learning Outcome

After completing this lecture, you should understand:

- How PostgreSQL works with FastAPI.
- How to configure SQLAlchemy for PostgreSQL.
- How to create database models and tables.
- How to manage database sessions.
- How to perform CRUD operations.
- How FastAPI Dependency Injection works with database sessions.

---

## 21. What's Next?

**Lecture 15 — SQLAlchemy Relationships**

We will learn how to connect multiple database tables using relationships:

- One-to-One
- One-to-Many
- Many-to-Many
- Foreign Keys
- `relationship()`
- `back_populates`
- Lazy Loading vs Eager Loading

After that, we will cover **Alembic Database Migrations** in Lectures 16 and 17.
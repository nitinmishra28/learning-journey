# FastAPI — Lecture 13: SQLAlchemy Basics

My personal notes for understanding **SQLAlchemy ORM and database integration with FastAPI**.

## 1. What Is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM) that allows us to interact with relational databases using Python.

It supports databases such as:
- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server (through suitable database drivers and dialects)

Instead of writing SQL for every operation, we can use Python classes and objects to work with database tables and records.

**Example:** We can create a `Student` Python class and map it to a `students` database table.

---

## 2. What Is an ORM?

ORM stands for **Object Relational Mapping**.

It maps Python objects and classes to relational database tables and rows.

For example, consider this database table:

| id | name | age |
|---:|---|---:|
| 1 | Nitin | 24 |
| 2 | Rahul | 23 |

Using SQLAlchemy ORM, we can represent a student using a Python object.

```python
student = Student(name="Nitin", age=24)
```

The ORM maps this object to a row in the database.

### Without ORM — Raw SQL

```sql
INSERT INTO students (name, age)
VALUES ('Nitin', 24);
```

### With ORM

```python
student = Student(name="Nitin", age=24)

db.add(student)
db.commit()
db.refresh(student)
```

Both approaches can insert data into a database. SQLAlchemy ORM provides a Python-oriented way to manage database operations.

**Important:** ORM does not mean SQL is never used. SQLAlchemy generates SQL for ORM operations, and we can also execute SQL directly when needed.

---

## 3. Installing SQLAlchemy

For this lecture, we will use SQLite because it does not require a separate database server.

Install the packages:

```bash
pip install fastapi uvicorn sqlalchemy
```

For PostgreSQL, install a suitable driver as well. For example, with the Psycopg 3 driver:

```bash
pip install "psycopg[binary]"
```

For MySQL, one possible driver is PyMySQL:

```bash
pip install pymysql
```

We will use SQLite first to understand SQLAlchemy concepts. The same basic ORM workflow can be applied to other supported relational databases, with appropriate connection configuration and drivers.

---

## 4. Understanding the Project Structure

We can organize our application like this:

```text
fastapi_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
└── requirements.txt
```

Responsibilities:

- `main.py` — FastAPI application and endpoints.
- `database.py` — database engine, session factory, and session dependency.
- `models.py` — SQLAlchemy ORM models.

For a larger application, we can later separate routers, schemas, services, and repositories into additional modules.

---

## 5. Creating the Database Connection

Create `app/database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./school.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()
```

### Understanding the Code

**1. `DATABASE_URL`**

```python
DATABASE_URL = "sqlite:///./school.db"
```

This tells SQLAlchemy to use a SQLite database file named `school.db` in the current working directory.

**2. `create_engine()`**

```python
engine = create_engine(...)
```

The engine manages the database connectivity infrastructure and connections.

**3. `SessionLocal`**

```python
SessionLocal = sessionmaker(...)
```

This creates a factory that we use to create database sessions.

**4. `Base`**

```python
Base = declarative_base()
```

This is the base class used by our ORM model classes in this example.

**Note:** This lecture uses SQLAlchemy's traditional declarative API. SQLAlchemy 2.x also supports the newer `DeclarativeBase` approach, which we can use in later projects.

---

## 6. Understanding the Database URL

For SQLite:

```python
DATABASE_URL = "sqlite:///./school.db"
```

For PostgreSQL using Psycopg 3:

```python
DATABASE_URL = "postgresql+psycopg://username:password@localhost:5432/school_db"
```

For MySQL using PyMySQL:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/school_db"
```

General structure:

```text
dialect+driver://username:password@host:port/database_name
```

The exact URL depends on the database and driver.

**Security:** Do not hardcode production database credentials. Store them in environment-based configuration and keep secrets out of Git.

---

## 7. Creating a Database Model

Create `app/models.py`:

```python
from sqlalchemy import Column, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
```

### Understanding the Code

**`class Student(Base)`**

Defines an ORM model mapped to a database table.

**`__tablename__`**

```python
__tablename__ = "students"
```

Specifies the database table name.

**`id`**

```python
id = Column(Integer, primary_key=True, index=True)
```

Defines an integer primary key.

**`name`**

```python
name = Column(String(100), nullable=False)
```

Defines a required string column with a maximum length of 100 characters in databases that enforce that length.

**`age`**

```python
age = Column(Integer, nullable=False)
```

Defines a required integer column.

The Python class represents the table structure. Individual instances represent records.

---

## 8. Creating the Database Tables

Defining a model does not automatically create its table.

We need to create the tables explicitly.

In `app/main.py`:

```python
from fastapi import FastAPI

from app.database import engine, Base
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "FastAPI with SQLAlchemy"}
```

### Understanding `create_all()`

```python
Base.metadata.create_all(bind=engine)
```

SQLAlchemy checks the registered metadata and creates tables that do not already exist.

The `models` module is imported so that the `Student` model is registered before `create_all()` runs.

**Important:** `create_all()` creates missing tables; it does not manage ongoing schema changes like a migration tool. For production schema changes, Alembic is commonly used.

---

## 9. What Is a Database Session?

A SQLAlchemy session manages ORM objects and database interactions within a unit of work.

Example:

```python
db = SessionLocal()
```

A session helps us:

- Query records.
- Add new records.
- Update records.
- Delete records.
- Commit transactions.
- Roll back failed transactions.

Example:

```python
student = Student(name="Nitin", age=24)

db.add(student)
db.commit()
db.refresh(student)
```

### Important Session Methods

| Method | Purpose |
|---|---|
| `db.add()` | Adds an object to the session |
| `db.add_all()` | Adds multiple objects |
| `db.commit()` | Commits the current transaction |
| `db.refresh()` | Reloads an object's state from the database |
| `db.rollback()` | Rolls back the current transaction |
| `db.close()` | Closes the session and releases its resources |
| `db.delete()` | Marks a persistent object for deletion |

**Remember:** `db.add()` does not necessarily write the record to the database immediately. `commit()` commits the transaction.

---

## 10. Creating a Database Session Dependency

We should not create a database session manually in every endpoint without ensuring proper cleanup.

Add this to `app/database.py`:

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

### How It Works

1. `SessionLocal()` creates a session.
2. `yield db` provides the session to the endpoint.
3. The endpoint performs database operations.
4. The `finally` block closes the session when the dependency lifecycle ends.

FastAPI can inject this session using `Depends()`.

Example:

```python
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db


@app.get("/example")
def example(
    db: Annotated[Session, Depends(get_db)]
):
    return {"message": "Database session available"}
```

This endpoint only demonstrates session injection; it does not query the database.

**Important:** Closing a session is not the same as committing a transaction. We will handle transaction management in the CRUD examples.

---

## 11. Creating a Student Using SQLAlchemy

Now we can create an endpoint that inserts a student into the database.

Update `app/main.py`:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Student

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/students")
def create_student(
    name: str,
    age: int,
    db: Annotated[Session, Depends(get_db)]
):
    student = Student(
        name=name,
        age=age
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }
```

Request:

```text
POST /students?name=Nitin&age=24
```

Example response:

```json
{
    "id": 1,
    "name": "Nitin",
    "age": 24
}
```

### Understanding the Flow

**Step 1: Create an ORM object**

```python
student = Student(name=name, age=age)
```

**Step 2: Add it to the session**

```python
db.add(student)
```

**Step 3: Commit the transaction**

```python
db.commit()
```

**Step 4: Refresh the object**

```python
db.refresh(student)
```

Refreshing allows SQLAlchemy to load values generated or changed by the database, such as an automatically generated primary key.

This example uses query parameters for simplicity. In a proper CRUD API, we generally accept creation data through a Pydantic request body model.

---

## 12. Reading Students From the Database

Use SQLAlchemy's `select()` and `Session.scalars()` to retrieve records.

Add this endpoint:

```python
from sqlalchemy import select


@app.get("/students")
def get_students(
    db: Annotated[Session, Depends(get_db)]
):
    statement = select(Student)

    students = db.scalars(statement).all()

    return [
        {
            "id": student.id,
            "name": student.name,
            "age": student.age
        }
        for student in students
    ]
```

This returns all students currently stored in the table.

### Understanding the Query

```python
statement = select(Student)
```

Builds a SQLAlchemy query that selects student records.

```python
students = db.scalars(statement).all()
```

Executes the query and returns the ORM objects.

For larger datasets, use filtering and pagination rather than retrieving every record.

---

## 13. Updating a Student

We can retrieve a student by ID and update its attributes.

```python
from fastapi import HTTPException
from sqlalchemy import select


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    db: Annotated[Session, Depends(get_db)]
):
    statement = select(Student).where(
        Student.id == student_id
    )

    student = db.scalar(statement)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = name
    student.age = age

    db.commit()
    db.refresh(student)

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }
```

### Understanding the Flow

1. Find the student by ID.
2. Return `404` if the student does not exist.
3. Change the ORM object's attributes.
4. Commit the transaction.
5. Return the updated data.

SQLAlchemy tracks changes to persistent ORM objects and includes those changes in the next flush or commit.

---

## 14. Deleting a Student

```python
from fastapi import HTTPException
from sqlalchemy import select


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    statement = select(Student).where(
        Student.id == student_id
    )

    student = db.scalar(statement)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }
```

### Understanding the Flow

```python
db.delete(student)
db.commit()
```

- `db.delete(student)` marks the object for deletion.
- `db.commit()` commits the deletion to the database.

This example returns a JSON message. A production REST API could instead return `204 No Content` without a response body.

---

## 15. What Happens When a Database Operation Fails?

If a database operation fails during a transaction, the session may need a rollback before it can be used again.

Example:

```python
try:
    db.add(student)
    db.commit()
except Exception:
    db.rollback()
    raise
```

Here:

- `db.commit()` attempts to commit the transaction.
- `db.rollback()` rolls back the failed transaction.
- `raise` propagates the original exception.

This is a basic pattern. Production applications should handle expected database errors appropriately, log unexpected errors, and avoid exposing sensitive internal details to API clients.

---

## 16. SQLAlchemy ORM vs Raw SQL

| SQLAlchemy ORM | Raw SQL |
|---|---|
| Uses Python classes and objects | Uses SQL statements directly |
| Maps classes to database tables | Works directly with tables and SQL |
| Tracks object changes through a session | Requires explicit SQL execution |
| Can reduce repetitive SQL code | Provides direct control over SQL |
| Generates SQL for ORM operations | SQL is written explicitly |

Both approaches are useful.

ORMs are convenient for common CRUD operations, relationships, and object-oriented application code. Raw SQL can be useful for complex queries or database-specific operations.

---

## 17. SQLAlchemy 2.x Note

The examples above use SQLAlchemy's traditional declarative API:

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

SQLAlchemy 2.x also supports a modern declarative style:

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

Models can then use `Mapped` and `mapped_column()` for more explicit type annotations.

Example:

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    age: Mapped[int]
```

Both approaches are valid. The modern style is worth learning for new SQLAlchemy 2.x projects.

---

## 18. Common Mistakes

### Mistake 1: Forgetting to Import Models Before `create_all()`

SQLAlchemy can only create tables for models registered in the metadata.

Import your model modules before calling:

```python
Base.metadata.create_all(bind=engine)
```

### Mistake 2: Forgetting to Commit

Changes may remain uncommitted if you do not call:

```python
db.commit()
```

### Mistake 3: Not Closing Sessions

Use a `yield` dependency with a `finally` block to ensure the session is closed.

### Mistake 4: Confusing Engine and Session

- `Engine`: manages database connectivity.
- `Session`: manages ORM operations and a unit of work.
- `sessionmaker`: creates session instances.

### Mistake 5: Assuming `create_all()` Is a Migration Tool

`create_all()` creates missing tables. It does not reliably alter existing tables to match changed model definitions.

Use a migration tool such as Alembic for ongoing schema changes.

### Mistake 6: Hardcoding Database Credentials

Use environment variables or secure configuration for database URLs and credentials.

---

## 19. Interview Questions

### Q1. What is SQLAlchemy?

A Python SQL toolkit and ORM used to interact with relational databases.

### Q2. What is ORM?

Object Relational Mapping maps Python classes and objects to database tables and rows.

### Q3. What is an SQLAlchemy engine?

The engine manages database connectivity and provides connections for database operations.

### Q4. What is a SQLAlchemy session?

A session manages ORM objects, queries, and transaction-related work.

### Q5. What is `sessionmaker()`?

It creates a configurable factory for producing SQLAlchemy session instances.

### Q6. What is `Base`?

In the traditional declarative API, `Base` is the base class from which ORM models inherit so their table definitions can be registered in metadata.

### Q7. What does `Base.metadata.create_all()` do?

It creates tables that are missing from the database based on the registered metadata.

### Q8. What is the purpose of `db.add()`?

It adds an object to the session so it can be persisted during a flush or commit.

### Q9. What is the purpose of `db.commit()`?

It commits the current database transaction.

### Q10. What is the purpose of `db.refresh()`?

It reloads an ORM object's state from the database.

### Q11. Why use a `yield` dependency for a database session?

It provides a session to the endpoint and ensures the session is closed during dependency cleanup.

### Q12. Does SQLAlchemy ORM eliminate SQL?

No. SQLAlchemy generates SQL for ORM operations, and developers can also execute SQL directly.

---

## 20. Practice

Create a FastAPI application with SQLAlchemy and SQLite.

Requirements:

1. Create `database.py` with an engine, session factory, and `Base`.
2. Create a `Student` model with `id`, `name`, and `age`.
3. Create the database table.
4. Implement `get_db()` using `yield`.
5. Create a student endpoint.
6. Retrieve all students.
7. Retrieve a student by ID.
8. Update a student's details.
9. Delete a student.
10. Return `404` when a student does not exist.
11. Test the APIs using Swagger UI.
12. Restart the application and confirm that database records persist.

For now, focus on understanding the engine, models, sessions, and ORM operations. Request schemas, database migrations, and more advanced transaction handling can be covered in later lectures.

---

## Quick Revision

- SQLAlchemy is a Python SQL toolkit and ORM.
- ORM maps Python objects to relational database records.
- `create_engine()` configures database connectivity.
- `sessionmaker()` creates a session factory.
- `Base` registers ORM models through metadata.
- `create_all()` creates missing tables.
- `db.add()` adds objects to the session.
- `db.commit()` commits changes.
- `db.refresh()` reloads object state.
- `db.rollback()` rolls back a failed transaction.
- Use `yield` dependencies to manage session cleanup.
- Use Alembic for database schema migrations.

---

## Next Lecture

### Lecture 14 — PostgreSQL Integration With FastAPI

Topics:

- Connecting FastAPI to PostgreSQL.
- Installing a PostgreSQL driver.
- Configuring the database URL.
- Managing environment variables.
- Creating SQLAlchemy engines and sessions.
- Defining models and tables.
- Testing the connection.
- Common connection errors.
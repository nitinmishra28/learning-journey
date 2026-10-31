# Lecture 16 — Alembic Database Migrations

## 1. Introduction

In previous lectures, we learned how to:
- Connect FastAPI with PostgreSQL.
- Create SQLAlchemy models.
- Define database relationships.
- Perform CRUD operations.

Now let's understand an important problem.

### What happens when our database model changes?

Suppose we have a Student model:

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
```

Our application is running, and the `students` table already exists.

Now we want to add a new column:

```python
age = Column(Integer)
```

We have updated our Python model, but the existing PostgreSQL table does not automatically get updated.

This is where **Alembic** comes into the picture.

---

## 2. What Is Database Migration?

Database migration means managing changes to the database schema over time.

Schema changes include:

- Creating a new table.
- Adding a new column.
- Removing a column.
- Modifying a column.
- Adding or removing constraints.
- Creating indexes.
- Changing relationships between tables.

### Example

Initial database table:

| id | name | email |
|---|---|---|
| 1 | Rahul | rahul@gmail.com |

After adding an `age` column:

| id | name | email | age |
|---|---|---|---|
| 1 | Rahul | rahul@gmail.com | 22 |

A migration allows us to apply this change to the existing database while preserving existing records.

---

## 3. What Is Alembic?

Alembic is a database migration tool for SQLAlchemy.

It helps developers manage database schema changes through version-controlled migration scripts.

### Why do we need Alembic?

Without Alembic:
- We may manually execute SQL ALTER TABLE commands.
- Database changes become difficult to track.
- Different environments may have different database schemas.
- Rolling back changes becomes difficult.

With Alembic:
- Database changes are stored in migration files.
- We can track schema changes over time.
- We can upgrade the database.
- We can downgrade the database.
- We can maintain consistent schemas across environments.

**Important:** Alembic manages database schema migrations. It does not automatically migrate or transform all existing application data.

---

## 4. Install Alembic

Install Alembic:

```bash
pip install alembic
```

Verify installation:

```bash
alembic --version
```

---

## 5. Initialize Alembic

Run this command from your project root directory:

```bash
alembic init alembic
```

This creates the following structure:

```text
school_management/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── alembic.ini
│
├── app/
│   ├── database/
│   │   └── connection.py
│   │
│   ├── models/
│   │   └── student.py
│   │
│   └── main.py
│
└── .env
```

### Understand the Files

| File/Folder | Purpose |
|---|---|
| `alembic.ini` | Main Alembic configuration |
| `env.py` | Migration environment configuration |
| `versions/` | Stores migration scripts |
| `script.py.mako` | Template used to generate migration files |
| `README` | Alembic environment information |

---

## 6. Configure Database URL

Open `alembic.ini`.

You may find:

```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```

We can configure the database URL here, but for our project, we will load it from `.env` instead.

This avoids hardcoding database credentials.

### Example .env

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/school_management
```

---

## 7. Understand env.py

The `env.py` file is one of the most important Alembic files.

It controls how Alembic connects to the database and discovers SQLAlchemy models.

Open:

```text
alembic/env.py
```

Find:

```python
target_metadata = None
```

We need to replace it with our SQLAlchemy model metadata.

### Updated env.py Configuration

Add the following imports near the top:

```python
import os

from dotenv import load_dotenv

from app.database.connection import Base
from app.models.student import Student

load_dotenv()

config.set_main_option(
    "sqlalchemy.url",
    os.getenv("DATABASE_URL")
)

target_metadata = Base.metadata
```

Keep the remaining Alembic-generated functions in `env.py`.

### What is target_metadata?

```python
target_metadata = Base.metadata
```

It tells Alembic where to find our SQLAlchemy table definitions.

Alembic compares:

- SQLAlchemy model metadata.
- Existing database schema.

It uses this comparison to generate migration operations.

**Important:** Import every model before setting up migrations. Otherwise, Alembic may not detect all your tables.

As your project grows, you should use a central model import module to register all models.

---

## 8. What Is Autogenerate?

Autogenerate is a feature that detects differences between SQLAlchemy models and the existing database schema.

For example:

Existing model:

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
```

Updated model:

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
```

We have added an `email` column.

Alembic can detect this change and generate a migration script.

Command:

```bash
alembic revision --autogenerate -m "add email column to students"
```

This creates a new migration file inside:

```text
alembic/versions/
```

Example:

```text
alembic/versions/
    a1b2c3d4_add_email_column_to_students.py
```

**Important:** Autogenerate creates a proposed migration. Always review the generated migration before applying it.

---

## 9. Understand Migration Files

A generated migration file generally contains:

```python
from alembic import op
import sqlalchemy as sa

revision = "a1b2c3d4"
down_revision = None

def upgrade():
    pass

def downgrade():
    pass
```

Let's understand the important parts.

### revision

```python
revision = "a1b2c3d4"
```

Unique identifier of the migration.

### down_revision

```python
down_revision = None
```

Identifies the previous migration.

It establishes the migration history.

### upgrade()

```python
def upgrade():
    pass
```

Contains operations that apply the schema changes.

### downgrade()

```python
def downgrade():
    pass
```

Contains operations that reverse the migration.

---

## 10. Understanding Upgrade and Downgrade

### Upgrade

Upgrade applies migration changes to the database.

Example:

```python
def upgrade():
    op.add_column(
        "students",
        sa.Column("email", sa.String(length=100), nullable=True)
    )
```

This adds an `email` column to the students table.

### Downgrade

Downgrade reverses the migration.

```python
def downgrade():
    op.drop_column("students", "email")
```

This removes the email column.

**Important:** Downgrading a migration that drops or modifies data can result in data loss. Always understand the consequences before running it.

---

## 11. Apply Migration

After generating and reviewing the migration file, execute:

```bash
alembic upgrade head
```

### What does head mean?

`head` represents the latest migration revision in the migration history.

This command applies all pending migrations up to the latest revision.

---

## 12. Check Migration History

Check the current migration history:

```bash
alembic history
```

Check the current database revision:

```bash
alembic current
```

These commands help us understand which migrations exist and which revision has been applied to the database.

---

## 13. Rollback a Migration

Suppose we want to undo the latest migration.

Run:

```bash
alembic downgrade -1
```

This moves the database back by one migration revision.

To move to a specific revision:

```bash
alembic downgrade a1b2c3d4
```

To downgrade all the way to the base:

```bash
alembic downgrade base
```

**Warning:** Downgrading can remove columns, tables, or data. Use it carefully, especially in production.

---

## 14. Creating an Empty Migration

Sometimes Alembic cannot automatically detect a change or we need custom SQL operations.

Create an empty migration:

```bash
alembic revision -m "custom database migration"
```

Example:

```python
from alembic import op

revision = "b2c3d4e5"
down_revision = "a1b2c3d4"

def upgrade():
    op.execute(
        "UPDATE students SET age = 18 WHERE age IS NULL"
    )

def downgrade():
    pass
```

This is useful when we need custom data transformation logic.

Remember that a downgrade should reverse the operation where a safe and meaningful reversal is possible.

---

## 15. Important Alembic Commands

| Command | Purpose |
|---|---|
| `alembic init alembic` | Initialize Alembic |
| `alembic revision -m "message"` | Create an empty migration |
| `alembic revision --autogenerate -m "message"` | Generate migration from detected schema changes |
| `alembic upgrade head` | Apply all pending migrations |
| `alembic downgrade -1` | Roll back one migration |
| `alembic downgrade base` | Roll back all migrations |
| `alembic current` | Show current database revision |
| `alembic history` | Show migration history |
| `alembic heads` | Show current migration heads |
| `alembic show head` | Show latest migration details |

---

## 16. Complete Migration Workflow

Whenever we change a SQLAlchemy model, follow this workflow:

**Step 1:** Update the SQLAlchemy model.

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)
```

**Step 2:** Generate migration.

```bash
alembic revision --autogenerate -m "add email and age"
```

**Step 3:** Review the generated migration file.

Check:
- Correct table name.
- Correct column names.
- Correct data types.
- Nullable constraints.
- Default values.
- Foreign Keys and indexes.

**Step 4:** Apply migration.

```bash
alembic upgrade head
```

**Step 5:** Verify the database schema.

```sql
\d students
```

This command works in the PostgreSQL `psql` terminal.

---

## 17. Alembic vs create_all()

We used this earlier:

```python
Base.metadata.create_all(bind=engine)
```

But why do we need Alembic?

| create_all() | Alembic |
|---|---|
| Creates missing tables | Manages schema changes |
| Does not update existing table structures | Can add, alter and remove schema objects |
| No migration history | Maintains migration history |
| No built-in rollback workflow | Supports upgrade and downgrade |
| Useful for simple initial setup | Suitable for structured application development |

**Important:** Do not rely on `create_all()` to manage schema changes in a production application. Use Alembic migrations.

---

## 18. Common Mistakes

1. Forgetting to set `target_metadata`.
2. Forgetting to import SQLAlchemy models in `env.py`.
3. Running migrations from the wrong project directory.
4. Forgetting to configure the database URL.
5. Applying migrations without reviewing generated scripts.
6. Assuming autogenerate detects every database change.
7. Deleting migration files that have already been applied.
8. Running downgrade without understanding possible data loss.
9. Using `create_all()` alongside migrations without understanding their interaction.
10. Forgetting to commit migration files to Git.

---

## 19. Interview Questions

**Q1. What is Alembic?**

Alembic is a database migration tool used with SQLAlchemy to manage database schema changes.

**Q2. Why do we need database migrations?**

They allow us to track and apply database schema changes over time without manually recreating the database.

**Q3. What is autogenerate in Alembic?**

It compares SQLAlchemy model metadata with the existing database schema and generates a proposed migration.

**Q4. What is env.py?**

It configures the migration environment, database connection and target metadata.

**Q5. What is target_metadata?**

It points Alembic to SQLAlchemy model metadata so it can detect schema changes.

**Q6. What is the difference between upgrade and downgrade?**

Upgrade applies migrations, while downgrade reverses migrations.

**Q7. What is head in Alembic?**

It represents the latest migration revision.

**Q8. What is down_revision?**

It identifies the previous migration in the migration history.

**Q9. Does Alembic autogenerate detect every change?**

No. Autogenerate has limitations. Developers must review generated migrations and manually handle unsupported or complex changes.

**Q10. What is the difference between create_all() and Alembic?**

`create_all()` creates missing tables but does not manage existing schema changes. Alembic provides version-controlled schema migrations.

**Q11. Can Alembic perform data migrations?**

Yes. We can write custom Python or SQL operations inside migration scripts to update or transform existing data.

**Q12. Why should migration files be committed to Git?**

They maintain a shared migration history so different environments and developers can apply consistent database changes.

---

## 20. Practical Assignment

Implement Alembic in our School Management SaaS project.

### Task 1 — Setup

- Install Alembic.
- Initialize Alembic.
- Configure PostgreSQL connection.
- Connect Alembic with SQLAlchemy metadata.
- Import all models.

### Task 2 — First Migration

Create a Student model with:

- id
- name
- email

Generate and apply the first migration.

### Task 3 — Schema Changes

Add the following columns:

- age
- phone_number
- address

Generate and apply another migration.

### Task 4 — Rollback

- Roll back the latest migration.
- Check the database schema.
- Apply the migration again.

### Task 5 — Data Migration

Write a custom migration to update existing student records.

Example:

```sql
UPDATE students
SET age = 18
WHERE age IS NULL;
```

Understand how schema migrations and data migrations differ.

---

## 21. Expected Learning Outcome

After completing this lecture, you should understand:

- What database migrations are.
- Why Alembic is needed.
- How to initialize Alembic.
- How Alembic connects with SQLAlchemy.
- What `env.py` and `target_metadata` do.
- How autogenerate works.
- How migration files are structured.
- How to upgrade and downgrade migrations.
- How to manage schema changes safely.
- How to write basic data migrations.

---

## 22. What's Next?

**Lecture 17 — Alembic Advanced Migration Workflow**

We will cover:

- Adding and modifying columns.
- Renaming columns.
- Adding and removing tables.
- Foreign Key migrations.
- Index migrations.
- Nullable and non-nullable column changes.
- Default values.
- Handling existing records during migrations.
- Migration conflicts.
- Multiple migration heads and merge revisions.
- Production migration best practices.

We will practice these operations using our School Management SaaS database.
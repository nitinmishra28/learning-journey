# Lecture 17 — Alembic Advanced Migration Workflow

## 1. Introduction

In the previous lecture, we learned:

- What is Alembic?
- Why database migrations are needed.
- Alembic initialization.
- `alembic.ini` and `env.py`.
- `target_metadata`.
- Autogenerate migrations.
- Upgrade and downgrade.
- Migration history.

Now we will learn how to manage complex database changes.

### What We Will Learn

- Adding and removing columns.
- Modifying column types.
- Renaming columns.
- Creating and dropping tables.
- Adding Foreign Keys.
- Creating indexes.
- Handling nullable and non-nullable columns.
- Adding default values.
- Data migrations.
- Migration conflicts.
- Multiple migration heads.
- Production migration best practices.

---

## 2. Adding a New Column

Suppose our existing Student model contains:

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
```

Now we want to add an `age` column.

### Step 1: Update the Model

```python
age = Column(Integer, nullable=True)
```

### Step 2: Generate Migration

```bash
alembic revision --autogenerate -m "add age column"
```

### Step 3: Review Migration

```python
def upgrade():
    op.add_column(
        "students",
        sa.Column("age", sa.Integer(), nullable=True)
    )


def downgrade():
    op.drop_column("students", "age")
```

### Step 4: Apply Migration

```bash
alembic upgrade head
```

Now the age column will be available in PostgreSQL.

---

## 3. Removing a Column

Suppose we no longer need the `age` column.

Generate a migration:

```bash
alembic revision --autogenerate -m "remove age column"
```

Migration:

```python
def upgrade():
    op.drop_column("students", "age")


def downgrade():
    op.add_column(
        "students",
        sa.Column("age", sa.Integer(), nullable=True)
    )
```

Apply:

```bash
alembic upgrade head
```

**Important:** Dropping a column also removes its stored values. A downgrade that recreates the column cannot automatically restore the deleted data.

---

## 4. Modifying a Column

Suppose we initially created:

```python
name = Column(String(50))
```

Now we want to increase its length to 150.

Updated model:

```python
name = Column(String(150))
```

Generate migration:

```bash
alembic revision --autogenerate -m "increase student name length"
```

Example migration:

```python
def upgrade():
    op.alter_column(
        "students",
        "name",
        existing_type=sa.String(length=50),
        type_=sa.String(length=150),
        existing_nullable=True
    )


def downgrade():
    op.alter_column(
        "students",
        "name",
        existing_type=sa.String(length=150),
        type_=sa.String(length=50),
        existing_nullable=True
    )
```

**Note:** Reducing a column's size may fail or truncate data if existing values exceed the new limit. Check existing data before applying such changes.

---

## 5. Renaming a Column

Suppose we want to rename:

```text
name → full_name
```

Updated SQLAlchemy model:

```python
full_name = Column(String(100))
```

Generate a migration and review it carefully.

Alembic autogenerate may interpret a rename as dropping the old column and adding a new one.

For a real rename, manually write:

```python
def upgrade():
    op.alter_column(
        "students",
        "name",
        new_column_name="full_name",
        existing_type=sa.String(length=100)
    )


def downgrade():
    op.alter_column(
        "students",
        "full_name",
        new_column_name="name",
        existing_type=sa.String(length=100)
    )
```

This preserves the existing column data.

---

## 6. Creating a New Table

Suppose we want to create a Teachers table.

SQLAlchemy model:

```python
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
```

Generate migration:

```bash
alembic revision --autogenerate -m "create teachers table"
```

Example migration:

```python
def upgrade():
    op.create_table(
        "teachers",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("email", sa.String(100), nullable=False),
        sa.UniqueConstraint("email")
    )


def downgrade():
    op.drop_table("teachers")
```

Apply:

```bash
alembic upgrade head
```

---

## 7. Adding a Foreign Key

Suppose each student belongs to a department.

### Department Model

```python
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
```

### Student Model

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )
```

Generate migration:

```bash
alembic revision --autogenerate -m "add department foreign key"
```

Example migration:

```python
def upgrade():
    op.add_column(
        "students",
        sa.Column("department_id", sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        "fk_students_department_id",
        "students",
        "departments",
        ["department_id"],
        ["id"]
    )


def downgrade():
    op.drop_constraint(
        "fk_students_department_id",
        "students",
        type_="foreignkey"
    )

    op.drop_column("students", "department_id")
```

**Important:** The referenced department table must exist before creating the Foreign Key.

If students already exist, consider whether they need a department assigned before making the Foreign Key column non-nullable.

---

## 8. Creating an Index

An index helps the database find records more efficiently for suitable queries.

Suppose we frequently search students by email.

Create an index:

```python
op.create_index(
    "ix_students_email",
    "students",
    ["email"],
    unique=False
)
```

Remove the index:

```python
op.drop_index(
    "ix_students_email",
    table_name="students"
)
```

Complete migration:

```python
def upgrade():
    op.create_index(
        "ix_students_email",
        "students",
        ["email"],
        unique=False
    )


def downgrade():
    op.drop_index(
        "ix_students_email",
        table_name="students"
    )
```

**Note:** Indexes improve some read queries but consume storage and can increase the cost of INSERT, UPDATE and DELETE operations.

---

## 9. Nullable vs Non-Nullable Columns

This is an important concept when working with existing production databases.

### Nullable Column

```python
email = Column(String(100), nullable=True)
```

Allows NULL values.

### Non-Nullable Column

```python
email = Column(String(100), nullable=False)
```

Does not allow NULL values.

### Problem with Existing Records

Suppose we have 10,000 existing students.

Now we add:

```python
phone = Column(String(15), nullable=False)
```

Existing records do not have phone numbers.

The migration may fail because PostgreSQL cannot populate a required value for existing records automatically.

### Safe Migration Strategy

Use multiple steps.

**Step 1: Add a nullable column.**

```python
def upgrade():
    op.add_column(
        "students",
        sa.Column("phone", sa.String(15), nullable=True)
    )
```

**Step 2: Populate existing records.**

```python
def upgrade():
    op.execute(
        "UPDATE students SET phone = 'UNKNOWN' WHERE phone IS NULL"
    )
```

**Step 3: Make the column non-nullable.**

```python
def upgrade():
    op.alter_column(
        "students",
        "phone",
        existing_type=sa.String(15),
        nullable=False
    )
```

These operations should be placed in the correct order across migrations, or combined into one carefully ordered migration.

**Production tip:** For large databases, use a staged migration and backfill strategy rather than updating millions of records in one operation.

---

## 10. Adding Default Values

Suppose every new student should have an active status by default.

SQLAlchemy model:

```python
status = Column(
    String(20),
    nullable=False,
    default="active"
)
```

There is an important difference between Python-side defaults and database-side defaults.

### Python-Side Default

```python
default="active"
```

SQLAlchemy applies the default when it inserts a record through the ORM.

### Database-Side Default

```python
server_default="active"
```

The database applies the default when an INSERT statement does not provide a value.

Migration example:

```python
def upgrade():
    op.add_column(
        "students",
        sa.Column(
            "status",
            sa.String(20),
            nullable=False,
            server_default="active"
        )
    )


def downgrade():
    op.drop_column("students", "status")
```

For production systems, consider whether the database default should remain permanently or only be used to populate existing records during migration.

---

## 11. Data Migrations

Schema migrations change database structure.

Data migrations change existing records.

### Example

Suppose we have a status column:

| id | name | status |
|---|---|---|
| 1 | Rahul | NULL |
| 2 | Amit | NULL |
| 3 | Priya | active |

We want to update NULL statuses to `active`.

Migration:

```python
from alembic import op

def upgrade():
    op.execute(
        """
        UPDATE students
        SET status = 'active'
        WHERE status IS NULL
        """
    )


def downgrade():
    pass
```

### Schema Migration vs Data Migration

| Schema Migration | Data Migration |
|---|---|
| Changes database structure | Changes existing records |
| Adds columns | Updates values |
| Removes tables | Transforms data |
| Adds Foreign Keys | Converts old values into new values |

**Important:** A data migration should be designed carefully. A downgrade may not be possible if the original values cannot be reconstructed.

---

## 12. Understanding Migration Conflicts

Suppose two developers are working on the same project.

Developer A creates migration:

```text
a1b2_add_student_email.py
```

Developer B creates migration:

```text
c3d4_add_teacher_phone.py
```

Both migrations may have the same `down_revision`.

This creates two migration branches.

These are called multiple migration heads.

Check heads:

```bash
alembic heads
```

If multiple heads exist, Alembic may require a merge revision.

### Merge Migration

```bash
alembic merge heads -m "merge migration branches"
```

This creates a migration that joins the branches.

Apply the migrations:

```bash
alembic upgrade head
```

**Important:** Multiple heads are not necessarily an error. They represent separate migration branches that need to be coordinated.

---

## 13. Understanding Migration Revision History

Each migration has:

```python
revision = "c3d4e5f6"
down_revision = "a1b2c3d4"
```

Think of migration history as a chain.

```text
Initial Migration
       |
       v
Add Students Table
       |
       v
Add Email Column
       |
       v
Add Department Foreign Key
       |
       v
Latest Migration
```

Each migration points to its parent through `down_revision`.

This allows Alembic to determine the order in which migrations should be applied.

---

## 14. Production Migration Best Practices

1. Always review autogenerated migration files.
2. Commit migration files to Git.
3. Never delete migrations that have already been applied in shared environments.
4. Test migrations on a development or staging database first.
5. Take database backups before risky production migrations.
6. Avoid destructive schema changes without a data migration plan.
7. Use nullable columns when adding fields to tables containing existing records.
8. Use staged migrations for large database changes.
9. Avoid running migrations independently from multiple application instances at the same time.
10. Keep migrations small and focused.
11. Make downgrade operations meaningful wherever possible.
12. Use expand-and-contract migrations for changes that must remain compatible with running application versions.

### Expand-and-Contract Strategy

Suppose we want to rename `name` to `full_name`.

Instead of immediately deleting the old column:

**Expand:**
- Add the new column.
- Keep the old column.
- Backfill existing data.

**Transition:**
- Update application code to use the new column.
- Ensure old and new application versions remain compatible if deployments overlap.

**Contract:**
- Remove the old column after it is no longer needed.

This reduces deployment risk.

---

## 15. Important Alembic Commands

| Command | Purpose |
|---|---|
| `alembic revision -m "message"` | Create an empty migration |
| `alembic revision --autogenerate -m "message"` | Generate migration automatically |
| `alembic upgrade head` | Upgrade to latest revision |
| `alembic upgrade +1` | Upgrade one revision |
| `alembic downgrade -1` | Downgrade one revision |
| `alembic downgrade base` | Downgrade all revisions |
| `alembic current` | Show current revision |
| `alembic history` | Show migration history |
| `alembic heads` | Show all migration heads |
| `alembic merge heads` | Merge multiple heads |
| `alembic stamp head` | Mark database at a revision without running its migration |

**Warning:** `stamp` does not execute migration operations. Use it only when the actual database schema already matches the revision being stamped.

---

## 16. Common Mistakes

1. Assuming autogenerate always detects column renames.
2. Making existing columns non-nullable without handling NULL records.
3. Dropping columns without considering stored data.
4. Forgetting to create referenced tables before adding Foreign Keys.
5. Adding indexes without understanding query patterns.
6. Forgetting to review generated migration scripts.
7. Ignoring multiple migration heads.
8. Running destructive migrations directly in production.
9. Using `server_default` and `default` interchangeably.
10. Assuming downgrade always restores deleted data.

---

## 17. Interview Questions

**Q1. What is the difference between schema and data migration?**

Schema migration changes database structure, while data migration changes existing records.

**Q2. How do you rename a column using Alembic?**

Use `op.alter_column()` with the `new_column_name` argument.

**Q3. Why can adding a non-nullable column fail?**

Existing rows do not have a value for the new column, and NULL is not allowed.

**Q4. How do you add a Foreign Key using Alembic?**

Use `op.create_foreign_key()`.

**Q5. How do you create an index?**

Use `op.create_index()`.

**Q6. What is a migration head?**

It is a migration revision that has no child revision in its branch.

**Q7. What are multiple heads?**

They occur when multiple migration branches exist independently.

**Q8. How do you merge multiple migration heads?**

Use `alembic merge heads`.

**Q9. What is alembic stamp?**

It updates Alembic's recorded database revision without executing migration operations.

**Q10. How do you safely rename a column in production?**

Use a staged migration: add the new column, backfill data, update application code, and remove the old column after it is no longer needed.

**Q11. What is server_default?**

It defines a default value at the database level.

**Q12. Why should we review autogenerated migrations?**

Autogenerate may not correctly identify renames, complex constraints, data transformations or every schema change.

---

## 18. Practical Assignment

Implement advanced migrations in our School Management SaaS project.

### Task 1 — Column Operations

- Add `phone_number` to students.
- Modify the length of `name`.
- Rename `phone_number` to `mobile_number`.
- Remove an unnecessary column.

### Task 2 — Table Operations

- Create a Departments table.
- Create a Teachers table.
- Add Foreign Keys between related tables.

### Task 3 — Constraints and Indexes

- Add a unique constraint on student email.
- Create an index on student name.
- Add a Foreign Key constraint.

### Task 4 — Existing Data

- Add a nullable column.
- Populate existing records.
- Change it to non-nullable.
- Test the downgrade.

### Task 5 — Migration History

- Create two separate migration branches in a practice environment.
- Understand multiple heads.
- Merge the branches.
- Apply the merged migration.

---

## 19. Expected Learning Outcome

After completing this lecture, you should understand:

- How to perform advanced schema changes.
- How to rename columns without losing data.
- How to create and remove tables.
- How to manage Foreign Keys and indexes.
- How to handle nullable and non-nullable columns.
- How to write data migrations.
- How migration conflicts happen.
- How to merge multiple migration heads.
- How to plan safe production migrations.

---

## 20. What's Next?

**Lecture 18 — Database Sessions, Transactions & Connection Management**

We will cover:

- What is a database transaction?
- ACID properties.
- Commit and rollback.
- Transaction boundaries.
- Session lifecycle.
- Connection pooling.
- SQLAlchemy session management.
- Handling database errors.
- Managing transactions in FastAPI endpoints.

These concepts are essential for building reliable production APIs.
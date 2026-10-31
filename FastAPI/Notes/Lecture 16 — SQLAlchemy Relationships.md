# Lecture 15 — SQLAlchemy Relationships

## 1. Introduction

In real-world applications, data is stored in multiple related tables instead of keeping everything in one table.

For example, in our School Management System, we may have:

- Students
- Courses
- Teachers
- Departments

These tables are connected through relationships.

SQLAlchemy provides relationships to connect database models and access related records using Python objects.

### What We Will Learn

- What are database relationships?
- What is a Foreign Key?
- One-to-One relationship
- One-to-Many relationship
- Many-to-Many relationship
- SQLAlchemy `relationship()`
- `back_populates`
- Lazy Loading
- Eager Loading
- Practical implementation with FastAPI

---

## 2. What Is a Foreign Key?

A Foreign Key is a column in one table that references the Primary Key of another table.

It establishes a relationship between two database tables.

### Example

**departments table**

| id | department_name |
|---|---|
| 1 | Computer Science |
| 2 | Mathematics |

**students table**

| id | name | department_id |
|---|---|---|
| 1 | Rahul | 1 |
| 2 | Amit | 1 |
| 3 | Priya | 2 |

Here:

- `departments.id` is the Primary Key.
- `students.department_id` is the Foreign Key.
- `students.department_id` references `departments.id`.

SQLAlchemy implementation:

```python
from sqlalchemy import Column, Integer, String, ForeignKey

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )
```

**Important:** A Foreign Key creates a database-level relationship between tables.

---

## 3. Types of Database Relationships

There are three major types of relationships.

1. One-to-One
2. One-to-Many
3. Many-to-Many

---

## 4. One-to-One Relationship

One record in Table A is associated with exactly one record in Table B, and vice versa.

### Example: Student and Student Profile

One student has one profile.

One profile belongs to one student.

**students table**

| id | name |
|---|---|
| 1 | Rahul |
| 2 | Amit |

**student_profiles table**

| id | address | student_id |
|---|---|---|
| 1 | Bangalore | 1 |
| 2 | Delhi | 2 |

### SQLAlchemy Implementation

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    profile = relationship(
        "StudentProfile",
        back_populates="student",
        uselist=False
    )


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True)
    address = Column(String(200))

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True
    )

    student = relationship(
        "Student",
        back_populates="profile"
    )
```

### Understanding Important Properties

**1. relationship()**

```python
profile = relationship("StudentProfile")
```

It allows us to access the related StudentProfile object through the Student model.

**2. uselist=False**

```python
uselist=False
```

It tells SQLAlchemy that the relationship should return a single object instead of a list.

**3. unique=True**

```python
student_id = Column(
    Integer,
    ForeignKey("students.id"),
    unique=True
)
```

It ensures that one student ID cannot be associated with multiple profile records.

### Accessing Related Data

```python
student = db.query(Student).first()

print(student.profile.address)
```

---

## 5. One-to-Many Relationship

One record in Table A can be associated with multiple records in Table B.

However, each record in Table B belongs to one record in Table A.

### Example: Department and Students

One department can have multiple students.

One student belongs to one department.

**departments table**

| id | name |
|---|---|
| 1 | Computer Science |
| 2 | Mathematics |

**students table**

| id | name | department_id |
|---|---|---|
| 1 | Rahul | 1 |
| 2 | Amit | 1 |
| 3 | Priya | 2 |

### SQLAlchemy Implementation

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    students = relationship(
        "Student",
        back_populates="department"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )
```

### Understanding the Relationship

In the Department model:

```python
students = relationship(
    "Student",
    back_populates="department"
)
```

It returns a collection of students belonging to that department.

In the Student model:

```python
department = relationship(
    "Department",
    back_populates="students"
)
```

It returns the department associated with that student.

### Accessing Related Data

Get all students of a department:

```python
department = db.query(Department).first()

for student in department.students:
    print(student.name)
```

Get the department of a student:

```python
student = db.query(Student).first()

print(student.department.name)
```

---

## 6. Many-to-Many Relationship

Multiple records in Table A can be associated with multiple records in Table B.

### Example: Students and Courses

- One student can enroll in multiple courses.
- One course can have multiple students.

We need a third table called an association table.

### Database Structure

**students table**

| id | name |
|---|---|
| 1 | Rahul |
| 2 | Amit |

**courses table**

| id | course_name |
|---|---|
| 1 | Python |
| 2 | FastAPI |

**student_courses table**

| student_id | course_id |
|---|---|
| 1 | 1 |
| 1 | 2 |
| 2 | 1 |

The `student_courses` table connects students and courses.

### SQLAlchemy Implementation

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

student_courses = Table(
    "student_courses",
    Base.metadata,

    Column(
        "student_id",
        Integer,
        ForeignKey("students.id"),
        primary_key=True
    ),

    Column(
        "course_id",
        Integer,
        ForeignKey("courses.id"),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String(100))

    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses"
    )
```

### Understanding secondary

```python
secondary=student_courses
```

It tells SQLAlchemy to use the association table to connect Student and Course.

### Accessing Related Data

Get all courses of a student:

```python
student = db.query(Student).first()

for course in student.courses:
    print(course.course_name)
```

Get all students enrolled in a course:

```python
course = db.query(Course).first()

for student in course.students:
    print(student.name)
```

---

## 7. What Is back_populates?

`back_populates` connects two relationship attributes on related SQLAlchemy models.

Example:

```python
class Department(Base):

    students = relationship(
        "Student",
        back_populates="department"
    )


class Student(Base):

    department = relationship(
        "Department",
        back_populates="students"
    )
```

Here:

- `Department.students` represents the collection of students.
- `Student.department` represents the student's department.

Both relationship attributes refer to each other.

**Important:** `back_populates` synchronizes the ORM relationship between both sides.

---

## 8. ForeignKey vs relationship()

These two are different and work together.

| ForeignKey | relationship() |
|---|---|
| Defines database-level references | Defines ORM-level relationships |
| Used inside a column | Used as a model attribute |
| Maintains referential integrity | Allows object-based navigation |
| References another table's column | Connects SQLAlchemy model objects |

Example:

```python
department_id = Column(
    Integer,
    ForeignKey("departments.id")
)

department = relationship(
    "Department",
    back_populates="students"
)
```

- `department_id` stores the foreign key value.
- `department` provides access to the related Department object.

---

## 9. Lazy Loading

Lazy Loading means related data is loaded when we access the relationship attribute.

Example:

```python
student = db.query(Student).first()

print(student.department.name)
```

Initially, SQLAlchemy loads the student.

When we access:

```python
student.department
```

SQLAlchemy executes another query to fetch the related department, if it is not already loaded.

### Advantages

- Loads related data only when needed.
- Avoids loading unnecessary relationships.

### Disadvantages

- Can generate many database queries.
- May cause the N+1 query problem.

---

## 10. Eager Loading

Eager Loading means related data is loaded as part of the original query or through additional planned queries.

SQLAlchemy provides loading strategies such as:

- `joinedload()`
- `selectinload()`

### A. joinedload()

Uses SQL JOINs to load related records.

```python
from sqlalchemy.orm import joinedload

students = (
    db.query(Student)
    .options(joinedload(Student.department))
    .all()
)
```

SQLAlchemy loads students and their departments together using a JOIN.

### B. selectinload()

Loads related records using a separate query with an IN condition.

```python
from sqlalchemy.orm import selectinload

departments = (
    db.query(Department)
    .options(selectinload(Department.students))
    .all()
)
```

It loads departments first and then fetches their related students in a separate query.

### joinedload vs selectinload

| joinedload | selectinload |
|---|---|
| Uses SQL JOIN | Uses separate SELECT query |
| Good for many-to-one relationships | Often useful for collections |
| Can duplicate parent rows in SQL results | Avoids multiplying parent rows in the main query |
| Loads related data through JOIN | Loads related data using IN |

**Important:** Choose the loading strategy based on the relationship and query requirements.

---

## 11. N+1 Query Problem

The N+1 problem occurs when an application executes one query to fetch parent records and then one additional query for each parent record's related data.

Example:

```python
students = db.query(Student).all()

for student in students:
    print(student.department.name)
```

If there are 100 students, this may execute:

- 1 query to fetch all students.
- Up to 100 additional queries to fetch departments.

Total: Up to 101 queries.

### Solution: Eager Loading

```python
from sqlalchemy.orm import joinedload

students = (
    db.query(Student)
    .options(joinedload(Student.department))
    .all()
)
```

This can significantly reduce unnecessary database queries.

---

## 12. Practical Example — School Management System

Let's understand how relationships work in our School Management SaaS.

Possible database relationships:

| Entity A | Relationship | Entity B |
|---|---|---|
| Department | One-to-Many | Students |
| Department | One-to-Many | Teachers |
| Student | One-to-One | Student Profile |
| Student | Many-to-Many | Courses |
| Teacher | One-to-Many | Courses |
| Class | One-to-Many | Students |

### Example Scenario

A student belongs to a department and enrolls in multiple courses.

A department has multiple students.

A course can have multiple students.

This can be represented using:

- `departments`
- `students`
- `courses`
- `student_courses`

These relationships help us build a normalized and maintainable database structure.

---

## 13. Common Mistakes

1. Forgetting to define Foreign Keys.
2. Using incorrect table names in `ForeignKey()`.
3. Forgetting `back_populates` on the opposite relationship.
4. Using `uselist=False` without enforcing one-to-one uniqueness.
5. Creating many-to-many relationships without an association table.
6. Confusing `ForeignKey()` with `relationship()`.
7. Ignoring the N+1 query problem.
8. Loading too much related data unnecessarily.
9. Creating circular imports between model files.
10. Forgetting to import models before creating tables.

---

## 14. Interview Questions

**Q1. What are relationships in SQLAlchemy?**

Relationships allow us to connect different ORM models and access related records using Python objects.

**Q2. What is a Foreign Key?**

A Foreign Key is a column that references the Primary Key of another table.

**Q3. What are the three main database relationships?**

One-to-One, One-to-Many and Many-to-Many.

**Q4. What is the difference between ForeignKey and relationship()?**

ForeignKey establishes a database-level reference, whereas relationship() establishes an ORM-level relationship between model objects.

**Q5. What is back_populates?**

It connects relationship attributes on both related models.

**Q6. How do you implement a One-to-One relationship?**

Use a Foreign Key with a uniqueness constraint and configure the ORM relationship using `uselist=False`.

**Q7. How do you implement a Many-to-Many relationship?**

Use an association table containing Foreign Keys referencing both related tables.

**Q8. What is Lazy Loading?**

Related data is loaded when the relationship attribute is accessed.

**Q9. What is Eager Loading?**

Related data is loaded proactively as part of a planned query strategy.

**Q10. What is the N+1 query problem?**

It occurs when one query loads parent records and additional queries are executed for each parent's related records.

**Q11. What is joinedload()?**

It is an SQLAlchemy eager-loading strategy that uses SQL JOINs to load related data.

**Q12. What is selectinload()?**

It is an eager-loading strategy that fetches related records using a separate SELECT query with an IN condition.

---

## 15. Practical Assignment

Build the following database relationships for our School Management System.

### Task 1 — One-to-One

Create:

- Student table
- StudentProfile table

Requirements:

- One student should have one profile.
- A profile should belong to one student.
- Use ForeignKey and `uselist=False`.

### Task 2 — One-to-Many

Create:

- Department table
- Teacher table

Requirements:

- One department can have multiple teachers.
- Each teacher belongs to one department.

### Task 3 — Many-to-Many

Create:

- Student table
- Course table
- StudentCourse association table

Requirements:

- A student can enroll in multiple courses.
- A course can have multiple students.

### Task 4 — Query Optimization

- Fetch all students with their departments.
- Use `joinedload()`.
- Fetch all departments with their students.
- Use `selectinload()`.
- Compare the queries and understand the N+1 problem.

---

## 16. Expected Learning Outcome

After completing this lecture, you should understand:

- How database tables are connected.
- How Foreign Keys work.
- How to implement One-to-One relationships.
- How to implement One-to-Many relationships.
- How to implement Many-to-Many relationships.
- How SQLAlchemy `relationship()` works.
- Why we use `back_populates`.
- Lazy Loading vs Eager Loading.
- How to avoid the N+1 query problem.

---

## 17. What's Next?

**Lecture 16 — Alembic Database Migrations**

We will learn:

- What are database migrations?
- Why do we need Alembic?
- Alembic installation and initialization.
- Alembic project structure.
- Connecting Alembic with SQLAlchemy models.
- Understanding `alembic.ini` and `env.py`.
- Creating our first migration.

We will use Alembic to manage database schema changes without manually dropping and recreating tables.
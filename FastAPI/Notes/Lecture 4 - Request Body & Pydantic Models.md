# FastAPI — Lecture 4: Request Body & Pydantic Models

## 1. What Is a Request Body?

A **request body** is data sent by the client to the backend inside an HTTP request.

Example:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

This data is called the request body.

Typical flow:

```text
React / Client
      ↓
POST Request
      ↓
JSON Request Body
      ↓
FastAPI
      ↓
Pydantic Validation
      ↓
Business Logic
```

## 2. When Do We Use a Request Body?

Request bodies are commonly used when we need to:

- Create data
- Update data
- Send structured information to the backend

Example:

```text
POST /students
```

Request body:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

---

## 3. What Is Pydantic?

**Pydantic** is a Python library used for:

- Data validation
- Data parsing
- Data serialization
- Defining data schemas

FastAPI uses Pydantic to validate and process structured request data.

```text
Client Data
     ↓
Pydantic Model
     ↓
Validation
     ↓
FastAPI Endpoint
```

---

## 4. Why Do We Need Pydantic?

Suppose our API expects:

```json
{
    "name": "Nitin",
    "age": 25
}
```

But the client sends:

```json
{
    "name": "Nitin",
    "age": "hello"
}
```

We expect `age` to be an integer, but the client sends an invalid value.

Pydantic validates incoming data against the model and reports validation errors when the data cannot be validated.

This prevents invalid data from reaching the endpoint function.

---

## 5. Creating a Pydantic Model

Import `BaseModel`:

```python
from pydantic import BaseModel
```

Create a model:

```python
class Student(BaseModel):
    name: str
    age: int
    class_name: str
```

This defines the expected structure of a student.

```text
Student
│
├── name       → str
├── age        → int
└── class_name → str
```

Fields without default values are required.

---

## 6. Using Pydantic with FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    class_name: str


@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "class_name": student.class_name
    }
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

Response:

```json
{
    "name": "Nitin",
    "age": 25,
    "class_name": "10"
}
```

Because `Student` is a Pydantic model, FastAPI understands that `student` should come from the request body.

---

## 7. Accessing Model Fields

Consider:

```python
class Student(BaseModel):
    name: str
    age: int
```

Inside the endpoint, access the fields using dot notation:

```python
@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age
    }
```

Here:

```python
student.name
student.age
```

access the values of the Pydantic model instance.

---

## 8. Required Fields

Fields without default values are required.

```python
class Student(BaseModel):
    name: str
    age: int
```

Valid request:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Invalid request because `age` is missing:

```json
{
    "name": "Nitin"
}
```

FastAPI returns a request validation error before executing the endpoint function.

---

## 9. Optional Fields and Default Values

A field can accept `None` and have a default value.

```python
class Student(BaseModel):
    name: str
    age: int
    phone: str | None = None
```

Both requests are valid:

```json
{
    "name": "Nitin",
    "age": 25
}
```

```json
{
    "name": "Nitin",
    "age": 25,
    "phone": "9876543210"
}
```

The declaration:

```python
phone: str | None = None
```

means:

- The field can contain a string or `None`.
- The field is not required because it has a default value.

### Important Difference

```python
phone: str | None
```

The field is required, but its value may be `None`.

```python
phone: str | None = None
```

The field is optional because it has a default value.

---

## 10. What Is `Field()` in Pydantic?

`Field()` allows us to configure a model field.

We can use it to define:

- Default values
- Minimum and maximum values
- Minimum and maximum string lengths
- Numeric constraints
- Descriptions
- Examples
- Aliases
- Other field-related metadata

Import it:

```python
from pydantic import BaseModel, Field
```

### Basic Example

```python
class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, le=100)
```

Here:

```python
name: str = Field(min_length=3, max_length=50)
```

means the name must contain between 3 and 50 characters.

```python
age: int = Field(gt=0, le=100)
```

means:

- `gt=0` → Greater than 0.
- `le=100` → Less than or equal to 100.

Invalid values cause validation errors.

---

## 11. Common `Field()` Constraints

| Constraint | Meaning |
|---|---|
| `gt` | Greater than |
| `ge` | Greater than or equal to |
| `lt` | Less than |
| `le` | Less than or equal to |
| `min_length` | Minimum string or collection length |
| `max_length` | Maximum string or collection length |
| `default` | Default value |
| `description` | Describes the field |
| `examples` | Provides example values |
| `alias` | Defines an alternative field name for validation/serialization |

Example:

```python
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100,
        description="Name of the product"
    )

    price: float = Field(
        gt=0,
        description="Product price must be positive"
    )

    quantity: int = Field(
        ge=0,
        description="Available quantity"
    )
```

This model validates the product fields according to the specified constraints.

---

## 12. `Field()` with Default Values

We can provide a default value through `Field()`.

```python
class Student(BaseModel):
    name: str
    age: int
    active: bool = Field(default=True)
```

If the client sends:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Pydantic uses:

```text
active = True
```

You can also write:

```python
active: bool = True
```

For a simple default value, both approaches are valid.

Use `Field()` when you also need constraints or additional field metadata.

---

## 13. `Field()` with Lists

`Field()` can also validate the length of a list.

```python
class Student(BaseModel):
    name: str
    subjects: list[str] = Field(min_length=1, max_length=5)
```

Valid request:

```json
{
    "name": "Nitin",
    "subjects": ["Python", "FastAPI"]
}
```

Invalid request:

```json
{
    "name": "Nitin",
    "subjects": []
}
```

The list must contain at least one and at most five items.

---

## 14. What Is `model_config`?

In Pydantic v2, `model_config` is used to configure the behavior of a model.

It is defined inside the model class.

Example:

```python
from pydantic import BaseModel, ConfigDict


class Student(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    name: str
    age: int
```

Here:

```python
str_strip_whitespace=True
```

tells Pydantic to remove leading and trailing whitespace from string values.

For example:

```json
{
    "name": "  Nitin  ",
    "age": 25
}
```

The validated name becomes:

```text
"Nitin"
```

`ConfigDict` is the recommended way to configure models in Pydantic v2.

---

## 15. Common `model_config` Options

### A. `str_strip_whitespace`

Removes leading and trailing whitespace from strings.

```python
model_config = ConfigDict(
    str_strip_whitespace=True
)
```

Example:

```text
"  Nitin  " → "Nitin"
```

### B. `extra`

Controls how extra fields are handled.

Suppose the model is:

```python
class Student(BaseModel):
    name: str
    age: int
```

But the client sends:

```json
{
    "name": "Nitin",
    "age": 25,
    "city": "Bhopal"
}
```

The `city` field is not defined in the model.

By default, Pydantic v2 generally ignores extra fields.

You can change this behavior.

#### `extra="ignore"`

```python
class Student(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    age: int
```

The extra `city` field is ignored.

#### `extra="forbid"`

```python
class Student(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    age: int
```

Now the request fails validation because `city` is not allowed.

#### `extra="allow"`

```python
class Student(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    age: int
```

Extra fields are allowed and retained on the model instance.

**Practical recommendation:** Use `extra="forbid"` for request schemas when unexpected fields should be rejected. Keep the default behavior when that strictness is not required.

### C. `str_min_length`

Sets a minimum length for string fields.

```python
class Student(BaseModel):
    model_config = ConfigDict(str_min_length=2)

    name: str
```

Strings shorter than two characters fail validation.

You can still use `Field()` when you need a different constraint for an individual field.

### D. `validate_assignment`

Validates values when an existing model instance is modified.

```python
class Student(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    name: str
    age: int
```

Example:

```python
student = Student(name="Nitin", age=25)

student.age = "invalid"
```

With assignment validation enabled, the assignment raises a validation error.

Without this setting, ordinary assignment to an existing Pydantic model is not automatically validated by default.

### E. `str_to_lower`

Converts string values to lowercase.

```python
class Student(BaseModel):
    model_config = ConfigDict(str_to_lower=True)

    name: str
```

Example:

```text
"NITIN" → "nitin"
```

Use this only when lowercase conversion is appropriate for your data.

---

## 16. `Field()` vs `model_config`

This is an important distinction.

### `Field()`

Configures an individual field.

```python
class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0)
```

Here:

- `name` has its own length constraints.
- `age` must be greater than zero.

### `model_config`

Configures the behavior of the entire model.

```python
class Student(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    name: str
    age: int
```

Here:

- Extra fields are rejected.
- Leading and trailing whitespace is removed from strings.

Remember:

```text
Field()
   ↓
Individual field configuration

model_config
   ↓
Model-level configuration
```

---

## 17. Using `Field()` and `model_config` Together

Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()


class Student(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    name: str = Field(
        min_length=3,
        max_length=50,
        description="Student's full name"
    )

    age: int = Field(
        gt=0,
        le=100,
        description="Student's age"
    )

    phone: str | None = Field(
        default=None,
        min_length=10,
        max_length=15
    )


@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "phone": student.phone
    }
```

Valid request:

```json
{
    "name": "Nitin",
    "age": 25,
    "phone": "9876543210"
}
```

Invalid request:

```json
{
    "name": "AB",
    "age": -5,
    "city": "Bhopal"
}
```

The second request fails because:

- The name is shorter than the minimum length.
- The age is not greater than zero.
- The extra `city` field is forbidden.

FastAPI returns a validation error without executing the endpoint function.

---

## 18. What Is `model_dump()`?

`model_dump()` converts a Pydantic model instance into a Python dictionary.

Example:

```python
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int


student = Student(
    name="Nitin",
    age=25
)

print(student.model_dump())
```

Output:

```python
{
    "name": "Nitin",
    "age": 25
}
```

This is useful when you need to work with model data as a dictionary.

### Excluding Unset Fields

```python
student = Student(name="Nitin", age=25)

print(student.model_dump(exclude_unset=True))
```

`exclude_unset=True` excludes fields that were not explicitly provided when the model was created.

This is useful for partial-update logic.

**Important:** `model_dump()` is a Pydantic v2 method. In Pydantic v1, the corresponding method was commonly `.dict()`.

---

## 19. Nested Pydantic Models

A Pydantic model can contain another Pydantic model.

```python
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str


class Student(BaseModel):
    name: str
    age: int
    address: Address
```

Request:

```json
{
    "name": "Nitin",
    "age": 25,
    "address": {
        "city": "Bhopal",
        "state": "Madhya Pradesh"
    }
}
```

Pydantic validates the nested address structure as well.

---

## 20. Create and Update Models

Different operations may need different schemas.

### Create Model

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    class_name: str
```

These fields are required.

### Update Model

```python
class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    class_name: str | None = None
```

These fields can be omitted, allowing partial updates.

For example:

```json
{
    "age": 26
}
```

To identify which fields were provided, use:

```python
student_update.model_dump(exclude_unset=True)
```

Output:

```python
{
    "age": 26
}
```

**Important:** `str | None = None` allows `None` as a value. If your update API must distinguish omitted fields from explicitly supplied `null` values, `exclude_unset=True` helps preserve that distinction.

---

## 21. Request Body vs Query Parameter

### Query Parameter

```text
GET /students?class_id=10
```

Used for filtering, searching, and pagination.

### Request Body

```text
POST /students
```

Request body:

```json
{
    "name": "Nitin",
    "age": 25
}
```

Used to send structured data to the API.

---

## 22. Pydantic Model vs Database Model

A Pydantic model:

```python
class Student(BaseModel):
    name: str
    age: int
```

is mainly used for:

- Validation
- Serialization
- Request and response schemas

It does not automatically create a database table.

Database models are a separate concept, commonly handled using SQLAlchemy.

```text
Pydantic
   ↓
API Data Validation / Serialization

SQLAlchemy
   ↓
Database ORM / Database Operations
```

---

## 23. Automatic API Documentation

FastAPI automatically uses Pydantic models and field metadata to generate API documentation.

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You can inspect:

- Request body fields
- Field types
- Required fields
- Constraints
- Descriptions
- Example values, when provided

---

## 24. Common Mistakes

### Mistake 1 — Confusing Optional and Nullable

```python
phone: str | None
```

The field is required but accepts `None`.

```python
phone: str | None = None
```

The field is optional and accepts `None`.

### Mistake 2 — Using `Field()` for Model-Wide Configuration

Use `Field()` for field-level constraints.

Use `model_config` for model-level behavior.

### Mistake 3 — Using Pydantic v1 Configuration in Pydantic v2

Modern Pydantic v2 uses:

```python
model_config = ConfigDict(extra="forbid")
```

Older Pydantic v1 examples commonly use an inner `Config` class.

For new projects, prefer Pydantic v2 syntax.

### Mistake 4 — Assuming Type Hints Always Mean Strict Types

Pydantic may coerce compatible input values by default.

For example, a numeric string may be converted to an integer when valid.

If strict type validation is required, learn Pydantic's strict types and strict validation options.

### Mistake 5 — Making Every Field Optional

Avoid making every field optional without a reason.

Required fields should remain required when the API needs them.

---

## 25. Interview Questions

### Q1. What is Pydantic?

Pydantic is a Python library used for data validation, parsing, serialization, and defining data schemas.

### Q2. What is `Field()`?

`Field()` configures individual Pydantic model fields, including constraints, defaults, descriptions, and aliases.

### Q3. What is `model_config`?

`model_config` defines model-wide configuration in Pydantic v2.

Example:

```python
model_config = ConfigDict(extra="forbid")
```

### Q4. What is the difference between `Field()` and `model_config`?

`Field()` configures individual fields, while `model_config` configures the model's overall behavior.

### Q5. What does `extra="forbid"` do?

It rejects input containing fields that are not defined in the model.

### Q6. What does `validate_assignment=True` do?

It enables validation when values are assigned to fields on an existing model instance.

### Q7. What is `model_dump()`?

It converts a Pydantic model instance into a Python dictionary.

### Q8. What is the difference between Pydantic v1 and v2 configuration?

Pydantic v2 uses `model_config = ConfigDict(...)` for model configuration. Pydantic v1 commonly used an inner `Config` class.

### Q9. Does a Pydantic model create a database table?

No. A Pydantic model defines and validates data structures; database tables are managed separately.

### Q10. Can Pydantic models be nested?

Yes. One Pydantic model can contain another Pydantic model as a field.

---

## 26. Quick Revision

```text
BaseModel
    ↓
Defines a Pydantic model

Field()
    ↓
Configures an individual field

model_config
    ↓
Configures model-wide behavior

ConfigDict
    ↓
Defines Pydantic v2 configuration

model_dump()
    ↓
Converts a model instance into a dictionary
```

Important examples:

```python
name: str = Field(min_length=3, max_length=50)
```

```python
age: int = Field(gt=0, le=100)
```

```python
model_config = ConfigDict(extra="forbid")
```

```python
model_config = ConfigDict(validate_assignment=True)
```

```python
student.model_dump(exclude_unset=True)
```

---

## 27. Practice

Create a Pydantic model for a teacher.

Requirements:

- `name`: string, minimum 3 characters
- `age`: integer, greater than 18
- `email`: string
- `subject`: string
- `experience`: integer, greater than or equal to 0
- Reject extra fields

Use:

```python
Field()
```

for field-level constraints and:

```python
model_config = ConfigDict(extra="forbid")
```

for model-wide configuration.

Create:

```text
POST /teachers
```

Return the validated teacher data.

### Extra Practice

Create a `StudentUpdate` model with optional fields.

Test:

```python
student_update.model_dump(exclude_unset=True)
```

with different input combinations.

Do not use a database yet.

---

## Next Lecture

### Lecture 5 — Response Models & Status Codes

Topics:

- Response models
- `response_model`
- Response validation and serialization
- Request model vs response model
- Filtering sensitive fields
- HTTP status codes
- `status_code`
- Common API status codes
- Interview questions
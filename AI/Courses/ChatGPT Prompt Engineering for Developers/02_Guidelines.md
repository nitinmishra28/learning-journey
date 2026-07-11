# 02. Guidelines for Prompting

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Write effective prompts.
- Understand the two Prompt Engineering principles.
- Create structured prompts.
- Reduce hallucinations.
- Improve LLM responses.
- Apply Prompt Engineering in Backend AI applications.

---

# Why Prompt Engineering?

Large Language Models are powerful, but they only know what you tell them.

A poorly written prompt usually produces a poor response.

A well-written prompt produces:

- Better accuracy
- Better reasoning
- Less hallucination
- Consistent outputs
- Structured responses

Think of Prompt Engineering as writing clear requirements for another developer.

---

# Two Core Principles

Andrew Ng introduces two principles:

## Principle 1

> Write Clear and Specific Instructions

## Principle 2

> Give the Model Time to Think

Everything else in Prompt Engineering builds on these two ideas.

---

# Principle 1: Write Clear and Specific Instructions

LLMs are not mind readers.

Never assume the model understands what you want.

Instead,

tell it exactly

- what to do
- what not to do
- output format
- constraints

---

# Tactic 1 — Use Delimiters

## What are Delimiters?

Delimiters separate the **instruction** from the **input**.

Without delimiters, the model may confuse the instruction with the text.

Common delimiters:

- Triple Backticks

```
```

- Triple Quotes

```
"""
```

- XML Tags

```xml
<article>
...
</article>
```

- HTML Tags

```html
<text>
...
</text>
```

---

## Example

```python
text = """
Artificial Intelligence is transforming healthcare,
finance, and education.
"""

prompt = f"""
Summarize the following text
delimited by triple backticks.

```{text}```
"""
```

---

## Why does this work?

The model clearly understands

```text
Instruction

↓

Input Text

↓

Task
```

instead of mixing everything together.

---

## Backend Example

Imagine a Resume Analyzer.

```text
User uploads Resume

↓

Backend extracts text

↓

Prompt

Summarize this resume

```Resume Text```

↓

GPT

↓

Summary
```

This is how delimiters are used in production.

---

# Best Practice

Always separate

- Instructions
- Context
- User Data
- Examples

using delimiters.

---

# Tactic 2 — Ask for Structured Output

Instead of asking

```
Tell me about this person.
```

Ask

```
Return JSON containing

name

skills

experience

education
```

---

## Example

```python
prompt = """
Generate three books.

Return JSON.

Fields:

book_id

title

author

genre
"""
```

Expected Response

```json
[
  {
    "book_id":1,
    "title":"AI Basics",
    "author":"Andrew",
    "genre":"Education"
  }
]
```

---

## Why?

Structured output is easier to use.

Backend can directly convert JSON into

- Database records
- API responses
- UI components

without additional parsing.

---

## Production Example

FastAPI

↓

GPT

↓

JSON

↓

React UI

No manual formatting required.

---

# Tactic 3 — Check Whether Conditions Are Satisfied

Instead of assuming something exists,

ask the model to verify.

Example

```text
If the text contains instructions,

rewrite them.

Otherwise reply

"No instructions found."
```

---

## Why?

Reduces hallucinations.

Improves reliability.

---

# Example

Input

```
Today is a beautiful day.
```

Output

```
No instructions found.
```

---

# Tactic 4 — Few-Shot Prompting

Few-shot means

show examples before asking the real question.

---

Example

```
Child:

Teach me patience.

Grandparent:

Great rivers begin from small streams.

Child:

Teach me resilience.
```

The model learns

- tone
- format
- writing style

from previous examples.

---

## When should you use Few-Shot?

- Email generation
- SQL generation
- Code generation
- Customer Support
- Classification

---

# Principle 2

## Give the Model Time to Think

Instead of asking

```
Solve this.
```

Ask

```
Step 1

Understand problem.

Step 2

Solve.

Step 3

Explain.

Step 4

Return answer.
```

Breaking tasks into steps improves reasoning.

---

# Tactic 1 — Specify the Steps

Example

```python
prompt = """
Perform the following tasks.

1. Summarize the article.

2. Translate into French.

3. Extract people's names.

4. Return JSON.
"""
```

The model performs each task sequentially.

---

## Production Example

Customer uploads PDF

↓

Summarize

↓

Extract Skills

↓

Generate Questions

↓

Return JSON

---

# Tactic 2 — Let the Model Solve Before Judging

Instead of asking

```
Is the student's answer correct?
```

Ask

```
First solve the problem.

Then compare.

Then decide.
```

---

## Why?

Models often agree with incorrect answers.

Independent reasoning improves accuracy.

---

# Model Limitation — Hallucinations

LLMs sometimes generate information that sounds correct but is actually false.

Example

```
Tell me about

AeroGlide UltraSlim Smart Toothbrush
```

The product doesn't exist,

but the model might invent features.

---

## Reduce Hallucinations

- Give context.
- Use RAG.
- Ask for evidence.
- Verify outputs.
- Keep prompts specific.

---

# Temperature

Temperature controls randomness.

| Temperature | Output |
|-------------|---------|
| 0 | Predictable |
| 0.2 | Stable |
| 0.5 | Balanced |
| 1 | Creative |

Use

```
temperature=0
```

for

- SQL generation
- Backend APIs
- JSON
- Production systems

Use

```
temperature=1
```

for

- Stories
- Blogs
- Marketing

---

# Backend AI Example

```text
Frontend

↓

FastAPI

↓

Prompt Template

↓

OpenAI API

↓

LLM

↓

JSON

↓

Frontend
```

Prompt Engineering happens inside the backend before calling the LLM.

---

# Best Practices

✅ Be specific.

✅ Use delimiters.

✅ Ask for JSON.

✅ Break tasks into steps.

✅ Provide examples.

✅ Verify AI output.

---

# Common Mistakes

❌ Vague prompts

❌ No output format

❌ Mixing instructions and input

❌ Asking multiple unrelated questions

❌ Blindly trusting AI

---

# Interview Questions

### Why are delimiters important?

They separate instructions from user data, reducing ambiguity.

---

### Why ask for JSON?

Because structured output is easier for backend applications to parse and process.

---

### What is Few-Shot Prompting?

Providing examples so the model learns the expected response pattern.

---

### Why ask the model to think step-by-step?

Breaking tasks into steps improves reasoning accuracy and reduces mistakes.

---

### What is a hallucination?

A hallucination is when an LLM confidently generates incorrect or fabricated information.

---

# Key Takeaways

- Clear prompts produce better responses.
- Delimiters reduce ambiguity.
- Structured outputs simplify backend integration.
- Few-shot prompting teaches patterns.
- Multi-step reasoning improves accuracy.
- Hallucinations should always be verified.
- Prompt Engineering is one of the most important skills for AI application development.

---

# Next Chapter

➡️ **03_Iterative_Prompt_Development.md**

Learn how to iteratively improve prompts until they produce production-quality responses.
# 02. Guidelines for Prompting

## 📖 Overview

In this chapter, Andrew Ng introduces the **two core principles of
Prompt Engineering**. These principles form the foundation for writing
effective prompts for Large Language Models (LLMs).

The goal is not to make prompts shorter---it is to make them **clearer,
more structured, and easier for the model to understand**.

------------------------------------------------------------------------

# Why Prompt Engineering Matters

LLMs are extremely capable, but they rely on the quality of the
instructions they receive.

A vague prompt often produces vague results.

A well-designed prompt produces:

-   Accurate responses
-   Better reasoning
-   Structured output
-   Fewer hallucinations
-   More consistent answers

------------------------------------------------------------------------

# Two Principles of Prompt Engineering

## Principle 1: Write Clear and Specific Instructions

Clear prompts reduce ambiguity and guide the model toward the desired
output.

> **Important:** Clear does **not** mean short. In many cases, longer
> prompts with proper context produce better answers.

------------------------------------------------------------------------

# Tactic 1: Use Delimiters

Delimiters clearly separate different parts of the prompt.

Common delimiters:

-   Triple backticks `...`
-   Triple quotes \"\"\"...\"\"\"
-   XML tags `<text></text>`
-   Angle brackets `< >`

### Example

``` text
Summarize the text inside the triple backticks.

```This is a long article...```
```

### Why use delimiters?

-   Removes ambiguity
-   Separates instructions from input
-   Helps the model identify context

### Industry Use Cases

-   Summarizing documents
-   RAG applications
-   PDF analysis
-   Code explanation

------------------------------------------------------------------------

# Tactic 2: Ask for Structured Output

Instead of asking for free-form text, specify the format.

Examples:

-   JSON
-   HTML
-   Markdown
-   Tables
-   Bullet Lists

### Example

``` text
Generate three books.

Return JSON with:

book_id
title
author
genre
```

### Benefits

-   Easy to parse
-   API friendly
-   Consistent responses

------------------------------------------------------------------------

# Tactic 3: Ask the Model to Check Conditions

Ask the model to verify whether a condition is true before generating
output.

Example:

``` text
If the text contains instructions,
rewrite them as numbered steps.

Otherwise respond:

"No steps provided."
```

### Why?

Prevents incorrect assumptions and reduces hallucinations.

------------------------------------------------------------------------

# Tactic 4: Few-Shot Prompting

Provide examples before asking the model to perform a task.

Example:

``` text
Child: Teach me patience.

Grandparent:
"The deepest river starts from a small stream."

Child: Teach me resilience.
```

The model learns the response style from the examples.

### When to Use

-   Consistent tone
-   Custom writing style
-   Classification
-   Formatting

------------------------------------------------------------------------

# Principle 2: Give the Model Time to Think

Instead of asking for an immediate answer, guide the model through
intermediate reasoning steps.

------------------------------------------------------------------------

# Tactic 1: Specify the Steps

Break complex tasks into smaller steps.

Example:

1.  Summarize
2.  Translate
3.  Extract names
4.  Return JSON

This approach improves accuracy and organization.

------------------------------------------------------------------------

# Tactic 2: Ask the Model to Work Out Its Own Solution First

Instead of asking whether someone else's answer is correct, instruct the
model to solve the problem independently first.

### Example Workflow

``` text
Question

↓

Model solves problem

↓

Compare with student's answer

↓

Mark correct or incorrect
```

This avoids the model blindly agreeing with incorrect solutions.

------------------------------------------------------------------------

# Model Limitation: Hallucinations

LLMs sometimes generate information that sounds convincing but is
incorrect.

Example:

Ask about a fictional product.

The model may confidently invent specifications.

### Reduce Hallucinations By

-   Giving clear instructions
-   Providing context
-   Asking for evidence
-   Using external knowledge (RAG)

------------------------------------------------------------------------

# Temperature

Temperature controls randomness.

  Temperature   Behavior
  ------------- ---------------------------
  0             Deterministic, consistent
  0.3           Slight creativity
  0.7           Balanced
  1.0           Highly creative

For production AI systems, **0--0.3** is commonly used.

------------------------------------------------------------------------

# Best Practices

-   Be specific.
-   Define the output format.
-   Provide context.
-   Use delimiters.
-   Break complex tasks into steps.
-   Use examples when needed.
-   Ask the model to reason before answering.

------------------------------------------------------------------------

# Common Mistakes

-   Writing vague prompts
-   Mixing instructions with input
-   Not specifying output format
-   Asking multiple unrelated questions
-   Trusting every answer without verification

------------------------------------------------------------------------

# Industry Examples

## Customer Support

``` text
You are a customer support agent.

Answer politely.

Return only JSON.
```

------------------------------------------------------------------------

## Code Review

``` text
Review this Python code.

Explain:
- Bugs
- Improvements
- Time Complexity
```

------------------------------------------------------------------------

## Data Extraction

``` text
Extract:

- Name
- Email
- Phone

Return JSON.
```

------------------------------------------------------------------------

# Interview Questions

### What are the two principles of Prompt Engineering?

1.  Write clear and specific instructions.
2.  Give the model time to think.

------------------------------------------------------------------------

### What is Few-Shot Prompting?

Providing one or more examples so the model learns the expected style or
behavior before answering.

------------------------------------------------------------------------

### Why use delimiters?

To clearly separate instructions, context, and user input, reducing
ambiguity.

------------------------------------------------------------------------

### Why ask for structured output?

Structured output is easier to parse, validate, and integrate into
applications.

------------------------------------------------------------------------

### Why ask the model to solve the problem before judging another solution?

It reduces bias and improves reasoning accuracy.

------------------------------------------------------------------------

# Revision Summary

-   ✅ Principle 1: Write clear and specific instructions.
-   ✅ Principle 2: Give the model time to think.
-   ✅ Use delimiters.
-   ✅ Ask for structured output.
-   ✅ Check conditions.
-   ✅ Use few-shot prompting.
-   ✅ Break complex tasks into steps.
-   ✅ Ask the model to reason before answering.
-   ✅ Beware of hallucinations.
-   ✅ Lower temperature gives more consistent responses.

------------------------------------------------------------------------

# What's Next?

In the next chapter, we will learn **Iterative Prompt Development**,
where we improve prompts step by step to achieve better results.

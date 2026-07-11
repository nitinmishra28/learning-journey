# 06. Transforming

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Translate text between multiple languages.
- Detect the language of a given text.
- Correct grammar and spelling mistakes.
- Rewrite text in different styles and tones.
- Convert text into different formats.
- Build AI-powered text transformation APIs.

---

# What is Text Transformation?

Text Transformation means **changing the format, language, style, or structure of existing text without changing its meaning.**

Unlike text generation, transformation starts with existing content.

Examples:

- English → French
- Informal → Professional
- Incorrect grammar → Correct grammar
- Plain text → Markdown
- Markdown → HTML
- Paragraph → Bullet points

---

# Why is Text Transformation Important?

Many AI applications require transforming user input before displaying or storing it.

Examples include:

- Email rewriting
- Document translation
- Grammar correction
- Data cleaning
- Report formatting
- Localization
- Customer support replies

---

# 1. Language Translation

One of the strongest capabilities of LLMs is translation.

## Example

Prompt

```text
Translate the following text into French.

I love learning Artificial Intelligence.
```

Output

```text
J'aime apprendre l'intelligence artificielle.
```

---

## Multiple Language Translation

Prompt

```text
Translate the following sentence into:

- Hindi
- French
- Japanese
- Spanish

Text:

Artificial Intelligence is changing the world.
```

The model can generate all translations in one response.

---

# 2. Language Detection

LLMs can automatically identify the language.

Example

Prompt

```text
Identify the language.

Text:

Bonjour, comment allez-vous ?
```

Output

```text
French
```

Useful for multilingual applications.

---

# 3. Grammar Correction

Example

Prompt

```text
Correct the grammar.

Text:

He don't likes programming.
```

Output

```text
He doesn't like programming.
```

---

## Backend Example

User submits an email.

↓

Backend

↓

Grammar Correction

↓

Send Email

---

# 4. Spell Checking

Prompt

```text
Correct spelling mistakes.

Text:

I hav completd the assingment.
```

Output

```text
I have completed the assignment.
```

Useful for:

- Chat applications
- Email clients
- Editors

---

# 5. Tone Conversion

LLMs can rewrite text for different audiences.

Example

Original

```text
Send me the report ASAP.
```

Professional

```text
Could you please send me the report at your earliest convenience?
```

Friendly

```text
Hey! Could you send me the report when you get a chance?
```

---

# 6. Style Conversion

Prompt

```text
Rewrite this paragraph for a beginner.
```

or

```text
Rewrite this paragraph for software engineers.
```

Different audiences require different writing styles.

---

# 7. Format Conversion

LLMs can convert between formats.

Example

Markdown

↓

HTML

Prompt

```text
Convert the following Markdown into HTML.
```

---

Another example

Paragraph

↓

Bullet Points

Prompt

```text
Convert this paragraph into bullet points.
```

---

# 8. Structured Output

Instead of paragraphs,

return JSON.

Prompt

```text
Extract information.

Return JSON.

Fields:

name

email

skills
```

Useful for backend systems.

---

# Backend AI Workflow

```text
Frontend

↓

FastAPI

↓

Prompt Template

↓

OpenAI API

↓

Transformation

↓

JSON

↓

Frontend
```

---

# Production Example

Imagine building an AI Email Assistant.

User writes

```text
hey send me update fast
```

Backend sends

```text
Rewrite professionally.
```

LLM returns

```text
Dear Team,

Could you please share the latest update at your earliest convenience?

Thank you.
```

---

# Resume Formatting Example

Input

```
Resume
```

↓

Extract

↓

JSON

↓

Generate Markdown Resume

↓

Generate PDF

---

# Localization

Large companies translate applications into multiple languages.

Prompt

```text
Translate this UI text into:

French

German

Japanese

Spanish

Maintain the same meaning.
```

Useful for SaaS applications.

---

# Best Practices

- Clearly specify the target language.
- Specify the desired tone.
- Mention the audience.
- Use structured output when possible.
- Preserve important information.

---

# Common Mistakes

❌ Asking for translation without specifying language.

❌ Forgetting tone.

❌ Ignoring formatting.

❌ Returning paragraphs instead of JSON.

---

# Real-World Applications

- Gmail Smart Compose
- Grammarly
- Google Translate
- Microsoft Copilot
- AI Writing Assistants
- Localization Platforms
- Documentation Tools
- CRM Systems

---

# Interview Questions

### What is text transformation?

Text transformation changes existing text without changing its meaning.

---

### What transformations can LLMs perform?

- Translation
- Grammar correction
- Spell checking
- Tone conversion
- Style conversion
- Format conversion

---

### Why is transformation useful?

It automates repetitive text-processing tasks and improves communication.

---

### Why use JSON output?

Structured output is easier for backend systems to process.

---

### Where is transformation used?

- Email assistants
- Customer support
- Documentation
- Localization
- AI writing tools

---

# Backend AI Tip

Instead of making multiple API calls,

combine transformations.

Example

```text
Rewrite this email.

- Fix grammar
- Improve professionalism
- Translate to French

Return Markdown.
```

One prompt can perform multiple transformations efficiently.

---

# Key Takeaways

- LLMs can transform text in many ways.
- Translation is only one type of transformation.
- Tone and style can be changed for different audiences.
- Structured output simplifies backend integration.
- Multiple transformations can be combined into one prompt.

---

# What's Next?

➡️ **07_Expanding.md**

Learn how LLMs generate rich, detailed content such as emails, customer replies, product descriptions, and personalized messages while maintaining the desired tone and context.
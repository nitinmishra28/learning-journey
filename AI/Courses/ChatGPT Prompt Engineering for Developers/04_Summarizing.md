# 04. Summarizing

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Summarize long text using LLMs.
- Generate summaries for different audiences.
- Extract important information from documents.
- Control summary length and format.
- Build document summarization APIs.

---

# What is Text Summarization?

Text Summarization is the process of reducing large amounts of text into a shorter version while preserving the important information.

Instead of reading a 20-page report, an LLM can produce a concise summary in seconds.

---

# Why is Summarization Important?

In production AI systems, users rarely want to read entire documents.

Examples include:

- PDF summaries
- Research papers
- Emails
- Chat conversations
- Meeting notes
- Legal contracts
- Medical reports

Summarization helps users quickly understand the key points.

---

# Basic Summarization Prompt

Example:

```text
Summarize the following text.

<Text>

...

</Text>
```

Simple prompts work, but better prompts produce better summaries.

---

# Improve the Prompt

Instead of asking:

```text
Summarize this article.
```

Ask:

```text
Summarize the following article.

Requirements:

- Maximum 100 words
- Use bullet points
- Mention only important facts
- Ignore unnecessary details
```

The more specific the prompt, the better the output.

---

# Summarizing for Different Audiences

One of the strengths of LLMs is adapting summaries for different readers.

### Example

Prompt

```text
Summarize this article for a 10-year-old child.
```

Output

Simple language.

---

Prompt

```text
Summarize this article for a software engineer.
```

Output

Technical summary.

---

Prompt

```text
Summarize this article for senior management.
```

Output

Business-focused summary.

---

# Controlling Summary Length

You can control how detailed the summary should be.

Example:

```text
Summarize in one sentence.
```

or

```text
Summarize in three bullet points.
```

or

```text
Summarize in under 100 words.
```

---

# Extract Instead of Summarize

Sometimes you don't need a summary.

You only need specific information.

Example

Instead of

```text
Summarize this resume.
```

Ask

```text
Extract:

- Skills
- Experience
- Education
```

This produces structured information rather than a narrative summary.

---

# Backend Example

Suppose you're building an AI Resume Analyzer.

User uploads:

```
Resume.pdf
```

Workflow

```text
Resume.pdf

↓

Extract Text

↓

Prompt

↓

OpenAI API

↓

JSON Summary

↓

Frontend
```

Example Prompt

```text
Summarize this resume.

Return JSON.

Fields:

- Summary
- Skills
- Experience
- Education
```

---

# Summarizing Customer Reviews

Instead of reading hundreds of reviews, ask the model to identify common themes.

Prompt

```text
Summarize the following customer reviews.

Mention:

- Positive feedback
- Negative feedback
- Overall sentiment
```

Useful for:

- E-commerce
- Product Management
- Customer Support

---

# Summarizing Meeting Notes

Prompt

```text
Summarize the following meeting transcript.

Return:

- Decisions
- Action Items
- Deadlines
- Participants
```

Useful for:

- Slack
- Teams
- Zoom
- Google Meet

---

# Summarizing Emails

Prompt

```text
Summarize this email.

Mention:

- Main topic
- Requested action
- Deadline
```

Useful for:

- Gmail AI
- Outlook AI
- CRM Systems

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

LLM

↓

Summary

↓

Return JSON

↓

Frontend
```

Prompt templates should be reusable and stored separately from your application code.

---

# Best Practices

- Specify the audience.
- Specify the maximum length.
- Define the output format.
- Ask for bullet points when appropriate.
- Extract important information instead of summarizing everything.

---

# Common Mistakes

❌ Asking for vague summaries.

❌ Not specifying the audience.

❌ Forgetting output format.

❌ Ignoring length constraints.

---

# Real-World Applications

- PDF Chatbots
- AI Search
- RAG Applications
- Customer Support
- CRM Software
- Medical Reports
- Legal Documents
- Research Papers
- Resume Screening

---

# Interview Questions

### What is Text Summarization?

Text Summarization is the process of reducing long text into a shorter version while preserving important information.

---

### Why specify the audience?

Different audiences require different levels of detail and terminology.

---

### Why specify the output format?

Structured outputs are easier for backend systems to parse and display.

---

### When should you extract instead of summarize?

When the application requires specific information such as names, dates, or skills rather than a general overview.

---

### Why are summaries useful in RAG systems?

Summaries reduce the amount of information users need to read while preserving important context.

---

# Key Takeaways

- Summarization reduces long text into concise information.
- Prompt specificity improves summary quality.
- Different audiences require different summaries.
- Output format should be clearly defined.
- Summarization is widely used in Backend AI applications.

---

# Backend AI Tip

In production systems, don't hardcode prompts.

Store prompt templates separately.

Example

```text
prompts/

summarize_resume.txt

summarize_email.txt

summarize_meeting.txt

summarize_reviews.txt
```

This makes prompts reusable, easier to maintain, and version-controlled.

---

# What's Next?

➡️ **05_Inferring.md**

Learn how LLMs can classify text, detect sentiment, identify emotions, extract information, and perform intelligent inference from natural language.
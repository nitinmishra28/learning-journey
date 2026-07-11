# 05. Inferring

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Perform sentiment analysis using LLMs.
- Detect emotions in text.
- Identify customer intent.
- Extract information from unstructured text.
- Build AI-powered classification systems.

---

# What is Inferring?

Inferring is the process of understanding information that is **implied** rather than explicitly stated.

Unlike summarization, inference answers questions like:

- What is the sentiment?
- What emotion is expressed?
- What is the user's intent?
- Is this review positive or negative?
- Which department should handle this ticket?

---

# Why is Inferring Important?

Many AI applications need to **understand** text before taking action.

Examples include:

- Customer support
- Chatbots
- Ticket routing
- Email classification
- Resume analysis
- Fraud detection
- AI Agents

Inference allows LLMs to extract meaning from natural language.

---

# Example 1 – Sentiment Analysis

Prompt

```text
Determine the sentiment of the following review.

Review:

"The product quality is amazing, but delivery was slow."

Return:

- Sentiment
- Reason
```

Possible Output

```text
Sentiment: Positive

Reason:
The customer is happy with the product but dissatisfied with delivery time.
```

---

# Example 2 – Emotion Detection

Prompt

```text
Identify the emotions expressed.

Text:

"I waited two weeks for my package. I'm really disappointed."
```

Output

```text
Emotion:

- Disappointment
- Frustration
```

---

# Example 3 – Intent Detection

Intent means **what the user wants to accomplish.**

Prompt

```text
Identify the user's intent.

Message:

"I forgot my password and can't log in."
```

Output

```text
Intent:

Password Reset
```

---

# Common Intent Categories

- Password Reset
- Refund Request
- Product Inquiry
- Complaint
- Technical Support
- Billing
- Order Status

---

# Example 4 – Extract Information

Prompt

```text
Extract the following information.

Text:

John Smith joined ABC Technologies in 2022 as a Backend Developer.

Return JSON.
```

Output

```json
{
    "name": "John Smith",
    "company": "ABC Technologies",
    "year": 2022,
    "designation": "Backend Developer"
}
```

---

# Why Structured Output?

Instead of returning paragraphs,

return JSON.

Backend systems can directly use the output.

Example

```text
LLM

↓

JSON

↓

FastAPI

↓

Database

↓

Frontend
```

---

# Multi-Task Inference

LLMs can perform multiple inference tasks in a single prompt.

Example

```text
Analyze this review.

Return:

- Sentiment
- Emotion
- Product Category
- Urgency
```

Output

```json
{
    "sentiment":"Negative",
    "emotion":"Frustration",
    "category":"Delivery",
    "urgency":"High"
}
```

---

# Backend Example

Suppose you're building an AI Customer Support System.

Workflow

```text
Customer Message

↓

FastAPI

↓

Prompt Template

↓

OpenAI API

↓

JSON

↓

Support Dashboard
```

Prompt

```text
Analyze this customer message.

Return JSON.

Fields:

intent

sentiment

priority

department
```

---

# AI Ticket Routing

Example

Customer

```text
My internet has not been working since yesterday.
```

LLM Output

```json
{
    "department":"Technical Support",
    "priority":"High"
}
```

Backend automatically routes the ticket.

---

# Resume Screening

Prompt

```text
Analyze this resume.

Extract:

- Skills
- Experience
- Education
- Years of Experience
```

Useful for

- HR Systems
- ATS Platforms
- Recruitment AI

---

# Email Classification

Prompt

```text
Classify this email.

Categories

- Sales
- Support
- Finance
- Marketing
```

Output

```text
Support
```

---

# Review Analysis

Prompt

```text
Analyze the review.

Return:

- Sentiment
- Positive Points
- Negative Points
- Suggestions
```

Useful for

- Amazon
- Flipkart
- Swiggy
- Zomato

---

# Backend AI Workflow

```text
User Input

↓

FastAPI

↓

Prompt Template

↓

OpenAI API

↓

Inference

↓

JSON

↓

Business Logic

↓

Frontend
```

Inference happens before your backend decides what to do next.

---

# Best Practices

- Ask for structured output.
- Define labels clearly.
- Use JSON whenever possible.
- Keep prompts specific.
- Test multiple examples.

---

# Common Mistakes

❌ Asking vague questions.

❌ Mixing multiple unrelated tasks.

❌ Returning paragraphs when JSON is needed.

❌ Not validating AI output.

---

# Real-World Applications

- Customer Support
- Resume Screening
- Email Classification
- Fraud Detection
- AI Agents
- CRM Systems
- Review Analysis
- Helpdesk Automation

---

# Interview Questions

### What is inference in Prompt Engineering?

Inference is the process of understanding information implied in text, such as sentiment, intent, emotion, or category.

---

### What is sentiment analysis?

Determining whether text expresses positive, negative, or neutral opinions.

---

### What is intent detection?

Identifying what the user wants to accomplish.

---

### Why return JSON instead of paragraphs?

JSON is structured, easier to parse, validate, and integrate into backend systems.

---

### Where is inference used?

- AI Chatbots
- Ticket Routing
- Customer Support
- Resume Analysis
- Email Classification
- AI Agents

---

# Backend AI Tip

Production AI systems rarely ask only one question.

Instead of making four separate API calls,

combine related tasks.

Example

```text
Analyze this customer message.

Return JSON.

Fields:

intent

sentiment

priority

recommended_action
```

One API call is faster, cheaper, and easier to maintain.

---

# Key Takeaways

- Inference extracts meaning from text.
- LLMs can classify, analyze, and extract information.
- JSON output simplifies backend integration.
- Inference is widely used in AI-powered backend systems.
- Combine multiple inference tasks into one prompt for better efficiency.

---

# What's Next?

➡️ **06_Transforming.md**

Learn how LLMs can transform text by translating languages, correcting grammar, changing writing styles, converting formats, and rewriting content.
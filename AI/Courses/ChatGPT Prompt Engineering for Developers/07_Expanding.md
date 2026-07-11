# 07. Expanding

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Generate high-quality text using LLMs.
- Create personalized customer responses.
- Control the tone and style of generated content.
- Generate emails, messages, and descriptions.
- Build AI-powered content generation systems.

---

# What is Expanding?

Expanding is the process of generating **new content** from a small amount of information.

Unlike summarization (making text shorter), expanding **adds useful details** while maintaining context.

Example

Input

```text
Customer is unhappy because the product arrived late.
```

Output

```text
Dear Customer,

We sincerely apologize for the delay in delivering your order.

We understand how frustrating this must be, and we appreciate your patience.

Our team is working to improve delivery times, and we hope to serve you better in the future.

Thank you for your understanding.
```

---

# Why is Expanding Important?

Many AI applications generate content instead of simply answering questions.

Examples include:

- Customer Support
- Email Generation
- Chatbots
- Marketing
- Blog Writing
- Documentation
- AI Assistants
- Product Descriptions

---

# Example 1 – Generate Customer Support Reply

Prompt

```text
A customer wrote:

"I've waited 10 days for my package.
I'm very disappointed."

Write a professional customer support response.
```

Possible Output

```text
Dear Customer,

We're sorry to hear about the delay in your order.

We completely understand your frustration.

Our team is currently investigating the shipment and will update you as soon as possible.

Thank you for your patience.
```

---

# Controlling Tone

One of the biggest advantages of LLMs is controlling the writing style.

Prompt

```text
Write the reply in a professional tone.
```

or

```text
Write the reply in a friendly tone.
```

or

```text
Write the reply in an empathetic tone.
```

Different prompts produce different styles.

---

# Example 2 – Marketing Content

Prompt

```text
Write a product description.

Product:

Wireless Noise Cancelling Headphones

Audience:

College Students

Maximum 100 words.
```

Output

A short product description suitable for an online store.

---

# Example 3 – Email Generation

Prompt

```text
Write a professional email.

Purpose:

Request a project status update.

Tone:

Professional

Length:

100 words
```

---

# Example 4 – Personalized Messages

Prompt

```text
Generate a birthday message for a software engineer who loves AI.
```

Output

A personalized greeting.

---

# Backend Example

Imagine you're building an AI Customer Support Platform.

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

Generated Reply

↓

Review

↓

Send to Customer
```

The backend creates the prompt and sends it to the LLM.

---

# Dynamic Prompt Templates

Instead of hardcoding prompts, use variables.

Example

```text
Write a reply for the following complaint.

Complaint:

{customer_message}

Tone:

Professional

Length:

Short
```

The backend replaces the variable before sending the request.

---

# Prompt Variables

Example

```python
customer_name = "John"

issue = "Late Delivery"

prompt = f"""
Write a professional response.

Customer:

{customer_name}

Issue:

{issue}
"""
```

This makes prompts reusable.

---

# Best Practices

- Clearly define the audience.
- Specify the desired tone.
- Mention the maximum length.
- Include context.
- Avoid vague prompts.

---

# Common Mistakes

❌ No context.

❌ No audience.

❌ No tone.

❌ No output format.

❌ Asking for too much in one prompt.

---

# Real-World Applications

- AI Customer Support
- AI Email Assistant
- Marketing Automation
- AI Blog Writer
- AI Chatbots
- Social Media Content
- Notification Generation
- Product Description Generation

---

# Backend AI Workflow

```text
Frontend

↓

FastAPI

↓

Prompt Template

↓

LLM

↓

Generated Content

↓

Validation

↓

Frontend
```

Always validate AI-generated content before sending it to users.

---

# Prompt Template Example

Instead of writing prompts repeatedly,

store them in files.

Example

```text
prompts/

customer_reply.txt

marketing_email.txt

birthday_message.txt

product_description.txt
```

This makes prompts reusable and version-controlled.

---

# Interview Questions

### What is text expansion?

Text expansion is generating new content from a small amount of input while maintaining context and meaning.

---

### Why specify tone?

Tone helps the LLM generate content suitable for the target audience.

---

### Why use prompt templates?

Prompt templates improve maintainability, consistency, and reusability.

---

### What should every content generation prompt include?

- Context
- Audience
- Tone
- Output format
- Constraints

---

### Why validate AI-generated content?

LLMs can generate incorrect or inappropriate information. Validation improves reliability before presenting results to users.

---

# Backend AI Tip

Avoid directly sending user input to the model.

Instead, wrap it inside a prompt template.

Example

```text
You are a professional customer support representative.

Customer Complaint:

{customer_message}

Generate:

- Empathetic response
- Professional tone
- Maximum 150 words
```

This produces more consistent and reliable outputs.

---

# Key Takeaways

- Expanding generates new content from existing information.
- Prompt quality directly affects generated content.
- Tone, audience, and constraints improve results.
- Prompt templates are essential in production AI systems.
- Validate generated content before returning it to users.

---

# What's Next?

➡️ **08_Chatbot.md**

Learn how to build conversational AI applications using message roles, conversation history, system prompts, and multi-turn interactions.
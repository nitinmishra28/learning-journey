# 08. Chatbot

> **Course:** ChatGPT Prompt Engineering for Developers
>
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Understand how chat models work.
- Learn the different message roles.
- Build a multi-turn chatbot.
- Maintain conversation history.
- Design system prompts.
- Build AI-powered chat applications using FastAPI.

---

# What is a Chatbot?

A chatbot is an AI application that can hold a conversation with users.

Unlike previous chapters where each prompt was independent, chatbots remember previous messages and generate context-aware responses.

Examples:

- ChatGPT
- Claude
- Gemini
- Microsoft Copilot
- Customer Support Bots
- AI Assistants

---

# How Chat Models Work

Unlike text completion models, chat models receive a **list of messages**.

Example:

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```

The model generates the next assistant response based on the conversation history.

---

# Message Roles

There are three primary roles.

## 1. System Role

Defines the behavior of the AI.

Example

```text
You are a helpful AI assistant.
```

or

```text
You are an expert Python developer.
```

The system prompt sets the personality, rules, and responsibilities of the assistant.

---

## 2. User Role

Represents the user's message.

Example

```text
Explain Binary Search.
```

---

## 3. Assistant Role

Represents previous AI responses.

Example

```text
Binary Search is an efficient searching algorithm...
```

The assistant messages allow the model to maintain context.

---

# Conversation Flow

```text
System Prompt
       │
       ▼
User Message
       │
       ▼
Assistant Response
       │
       ▼
User Message
       │
       ▼
Assistant Response
```

Each new response is generated using the complete conversation history.

---

# Example Conversation

System

```text
You are a Python Tutor.
```

User

```text
What is a list?
```

Assistant

```text
A list is an ordered collection...
```

User

```text
How is it different from a tuple?
```

Because the previous messages are included, the model understands that "it" refers to a Python list.

---

# Modern OpenAI API Example

```python
from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a Python Tutor."
    },
    {
        "role": "user",
        "content": "Explain dictionaries."
    }
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

print(response.choices[0].message.content)
```

---

# Backend AI Workflow

```text
Frontend

↓

FastAPI

↓

Conversation History

↓

Prompt Builder

↓

OpenAI API

↓

Assistant Response

↓

Save Conversation

↓

Frontend
```

The backend stores and sends the conversation history with each request.

---

# Why Conversation History Matters

Without conversation history:

User

```text
Explain Python.
```

Assistant

```text
Python is a programming language.
```

User

```text
Who created it?
```

The model may not know what "it" refers to.

With conversation history included, the model understands that "it" refers to Python.

---

# Designing Good System Prompts

A strong system prompt defines:

- Role
- Behavior
- Tone
- Restrictions
- Response format

Example

```text
You are a Backend AI Engineer.

Answer in Markdown.

Provide Python examples.

Keep explanations concise.

If unsure, say you don't know instead of guessing.
```

---

# Prompt Template

Instead of writing prompts manually, build them dynamically.

```python
system_prompt = """
You are an AI Coding Assistant.
"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_query
    }
]
```

---

# Backend FastAPI Example

```text
User Question

↓

FastAPI

↓

Load Conversation History

↓

Append New User Message

↓

OpenAI API

↓

Save Assistant Response

↓

Return Response
```

---

# Chat Memory

Chat models do **not** permanently remember users.

Memory exists only if previous messages are sent with the request.

Example

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "..."}
]
```

The backend is responsible for maintaining this message history.

---

# Production Considerations

In real-world applications:

- Store conversation history in a database.
- Trim old messages to stay within token limits.
- Use summaries for long conversations.
- Validate user input.
- Protect against prompt injection.

---

# Backend AI Best Practices

- Keep the system prompt consistent.
- Store prompts separately from code.
- Use structured outputs (JSON) when appropriate.
- Log prompts and responses for debugging.
- Handle API errors gracefully.
- Monitor token usage and cost.

---

# Common Mistakes

❌ Sending only the latest user message.

❌ Changing the system prompt every request.

❌ Ignoring token limits.

❌ Not validating AI responses.

❌ Mixing business logic inside prompts.

---

# Real-World Applications

- Customer Support Bots
- AI Coding Assistants
- HR Chatbots
- Educational Tutors
- Internal Company Assistants
- Healthcare Assistants
- Banking Chatbots
- E-commerce Support

---

# Interview Questions

### What is the purpose of the system role?

The system role defines the assistant's behavior, personality, and rules for the conversation.

---

### Why is conversation history important?

Conversation history provides context, allowing the model to understand follow-up questions and maintain coherent conversations.

---

### Does ChatGPT remember previous conversations automatically?

No. The backend must send previous messages with each request unless persistent memory features are implemented separately.

---

### Where should conversation history be stored?

Typically in a database such as PostgreSQL, MongoDB, or Redis, depending on the application's requirements.

---

### Why should prompts be stored separately from code?

Separating prompts improves maintainability, version control, and reuse across different parts of the application.

---

# Key Takeaways

- Chat models use a list of messages rather than a single prompt.
- System prompts define the assistant's behavior.
- Conversation history enables context-aware responses.
- The backend is responsible for managing memory.
- Production chatbots require prompt management, history storage, and validation.

---

# How This Fits Into Your Backend

```text
React

↓

FastAPI

↓

Authentication

↓

Conversation History (Database)

↓

Prompt Builder

↓

OpenAI API

↓

LLM Response

↓

Business Logic

↓

Frontend
```

As a Backend + AI Engineer, your responsibility is not just calling the LLM—it is designing the complete workflow around it.

---

# What's Next?

🎉 Congratulations!

You have completed the **ChatGPT Prompt Engineering for Developers** course.

Your next learning path should be:

1. LangChain Fundamentals
2. Embeddings
3. Vector Databases
4. Retrieval-Augmented Generation (RAG)
5. AI Agents
6. Model Context Protocol (MCP)
7. FastAPI + AI Integration
8. Production AI Deployment
# 01. Introduction

> **Course:** ChatGPT Prompt Engineering for Developers  
> **Instructor:** Andrew Ng & Isa Fulford (OpenAI)

---

# 📌 Learning Objectives

After completing this chapter, you should be able to:

- Understand what a Large Language Model (LLM) is.
- Differentiate between Base LLMs and Instruction-Tuned LLMs.
- Understand why Prompt Engineering exists.
- Know how ChatGPT generates responses.
- Understand where Prompt Engineering fits into a Backend AI application.

---

# What is a Large Language Model (LLM)?

A **Large Language Model (LLM)** is an AI model trained on massive amounts of text to understand and generate human language.

Instead of memorizing answers, it learns **patterns** in language and predicts the most likely next token.

LLMs can perform tasks such as:

- Answering questions
- Writing code
- Summarizing documents
- Translating languages
- Generating SQL queries
- Explaining code
- Writing emails
- Building chatbots

---

# Popular LLMs

| Company | Model |
|----------|-------|
| OpenAI | GPT-4o, GPT-4.1 |
| Anthropic | Claude |
| Google | Gemini |
| Meta | Llama |
| Mistral AI | Mistral |

---

# Types of LLMs

There are two main types of LLMs:

1. Base LLM
2. Instruction-Tuned LLM

These are the first concepts introduced in this course.

---

# Base LLM

A **Base LLM** is trained to predict the next token based on previous text.

Its goal is **text continuation**, not following instructions.

## Example

Input

```text
The capital of France is
```

Output

```text
Paris
```

Another example

Input

```text
Once upon a time there was a king who
```

Output

```text
lived in a beautiful castle...
```

The model simply continues the sentence.

---

## Characteristics

- Predicts the next token
- Learns language patterns
- Excellent at text completion
- Does not naturally follow instructions
- Not optimized for conversations

---

## Limitation

Suppose we ask

```text
Translate this sentence into French.

Hello
```

A Base LLM might continue the text instead of translating it because it has not been trained to follow instructions.

---

# Instruction-Tuned LLM

An **Instruction-Tuned LLM** starts as a Base LLM and is further trained to follow human instructions.

These models are designed for conversations and practical AI applications.

Examples include:

- ChatGPT
- Claude
- Gemini
- GitHub Copilot

---

## How is an Instruction-Tuned Model Created?

```text
Large Text Dataset
        │
        ▼
Pre-Training
        │
        ▼
Base LLM
        │
Instruction Fine-Tuning
        │
        ▼
Human Feedback (RLHF)
        │
        ▼
Instruction-Tuned LLM
```

---

# What is RLHF?

**RLHF** stands for **Reinforcement Learning from Human Feedback**.

During this stage:

1. Humans review multiple AI responses.
2. Humans rank the best response.
3. The model learns which answers people prefer.

This improves:

- Accuracy
- Safety
- Helpfulness
- Conversation quality

---

# Base LLM vs Instruction-Tuned LLM

| Feature | Base LLM | Instruction-Tuned LLM |
|----------|----------|-----------------------|
| Purpose | Predict next token | Follow instructions |
| Chatbot | ❌ | ✅ |
| Translation | Limited | Excellent |
| Summarization | Limited | Excellent |
| Code Generation | Limited | Excellent |
| Customer Support | ❌ | ✅ |

---

# What is a Token?

LLMs do not read text word-by-word.

They process **tokens**.

Example:

```text
Hello ChatGPT
```

may become

```text
["Hello", " Chat", "GPT"]
```

The exact split depends on the tokenizer used by the model.

---

# Why Tokens Matter

Tokens affect:

- API cost
- Maximum context length
- Response length
- Performance

When using APIs, you pay based on the number of tokens processed.

---

# What is Prompt Engineering?

Prompt Engineering is the practice of writing prompts that help an LLM generate the desired response.

A good prompt provides:

- Clear instructions
- Context
- Constraints
- Expected output format

Example:

❌ Poor Prompt

```text
Write Python.
```

✅ Better Prompt

```text
Write a Python function that checks whether a string is a palindrome.

Explain the logic.

Return only Python code.
```

---

# How ChatGPT Works (Simplified)

```text
User Prompt
      │
      ▼
Tokenizer
      │
      ▼
LLM (GPT)
      │
      ▼
Next Token Prediction
      │
      ▼
Generated Response
```

The model predicts one token at a time until the response is complete.

---

# Where Prompt Engineering Fits in a Backend

As a Backend + AI Engineer, Prompt Engineering is not an isolated skill. It is part of your backend workflow.

```text
React / Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
Prompt Template
        │
        ▼
OpenAI API
        │
        ▼
LLM Response
        │
        ▼
JSON Response
        │
        ▼
Frontend
```

In production systems:

- Users never interact directly with the LLM.
- The backend prepares the prompt.
- The backend validates the response.
- The backend sends clean JSON to the frontend.

---

# Real-World Example

Suppose you're building a Resume Analyzer.

User uploads a resume.

```text
PDF Upload
      │
      ▼
Extract Text
      │
      ▼
Build Prompt
      │
      ▼
OpenAI API
      │
      ▼
Receive Analysis
      │
      ▼
Return JSON
```

Prompt Engineering happens in the **Build Prompt** step.

---

# Best Practices

- Write clear prompts.
- Be specific.
- Provide context.
- Define the expected output format.
- Avoid ambiguous instructions.

---

# Common Mistakes

- Asking vague questions.
- Assuming the model knows your intent.
- Forgetting to specify the output format.
- Trusting AI responses without verification.

---

# Interview Questions

### What is a Base LLM?

A Base LLM predicts the next token based on previous text. It is trained for text completion rather than instruction following.

---

### What is an Instruction-Tuned LLM?

An Instruction-Tuned LLM is a Base LLM that has been further trained using instruction datasets and RLHF so it can follow human instructions.

---

### What is RLHF?

RLHF (Reinforcement Learning from Human Feedback) is a training process where humans rank model outputs, allowing the model to learn preferred responses.

---

### Why is Prompt Engineering important?

Prompt Engineering helps developers communicate effectively with LLMs, improving response quality without retraining the model.

---

### Why are Instruction-Tuned Models better for chat applications?

Because they are optimized to understand and follow user instructions rather than simply predicting the next token.

---

# Key Takeaways

- LLMs generate text by predicting tokens.
- Base LLMs are trained for text continuation.
- Instruction-Tuned LLMs follow human instructions.
- RLHF aligns models with human preferences.
- Prompt Engineering is the skill of communicating effectively with LLMs.
- In production, Prompt Engineering is implemented in the backend before sending requests to the LLM.

---

# Next Chapter

➡️ **02_Guidelines.md**

You'll learn the two fundamental principles of Prompt Engineering:

- Write clear and specific instructions.
- Give the model time to think.
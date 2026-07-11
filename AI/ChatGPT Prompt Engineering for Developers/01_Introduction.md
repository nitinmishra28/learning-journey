# 01. Introduction

## 📖 Overview

This chapter introduces the fundamentals of **Large Language Models
(LLMs)** and explains the difference between **Base LLMs** and
**Instruction-Tuned LLMs**.

Understanding this distinction is essential because modern AI
applications like **ChatGPT, Claude, Gemini, and GitHub Copilot** are
built on **instruction-tuned models**, not raw base models.

------------------------------------------------------------------------

# What is Prompt Engineering?

**Prompt Engineering** is the process of designing clear, effective, and
structured instructions (called *prompts*) that help Large Language
Models (LLMs) generate accurate, useful, and reliable responses.

Instead of changing or retraining the AI model, Prompt Engineering
focuses on improving **how we communicate with the model**.

> **Definition:** Prompt Engineering is the art and science of writing
> prompts that guide an LLM toward the desired output.

------------------------------------------------------------------------

# What is a Large Language Model (LLM)?

A **Large Language Model (LLM)** is an AI model trained on massive
amounts of text data to understand, generate, and manipulate human
language.

LLMs learn statistical patterns in language and predict the next most
likely word (or token) based on the context provided.

## LLMs can perform tasks

-   Answer questions
-   Write code
-   Summarize documents
-   Translate languages
-   Generate content
-   Debug code
-   Analyze data
-   Build chatbots

------------------------------------------------------------------------

# Popular LLMs

-   GPT-4
-   GPT-4o
-   Claude
-   Gemini
-   Llama
-   Mistral

------------------------------------------------------------------------

# Types of LLMs

There are two primary categories:

1.  Base LLM
2.  Instruction-Tuned LLM

------------------------------------------------------------------------

# Base LLM

A **Base LLM** predicts the **next token** based on previous text.

It is trained for **text continuation**, not instruction following.

## Training Objective

    Predict the next token.

Example:

Input

    The capital of France is

Output

    Paris

Another example:

    Once upon a time there was a king who

↓

    lived in a beautiful castle...

## Characteristics

-   Predicts the next token
-   Learns language patterns
-   Trained on massive datasets
-   Excellent at autocomplete
-   Does not naturally follow instructions

## Limitation

Prompt

    Translate "Hello" into French.

A Base LLM may continue the text instead of answering directly.

------------------------------------------------------------------------

# Instruction-Tuned LLM

An **Instruction-Tuned LLM** starts as a Base LLM and is further trained
to understand and follow human instructions.

These are the models used by ChatGPT and other AI assistants.

## Training Pipeline

``` text
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
        RLHF
        │
        ▼
Instruction-Tuned LLM
```

## Characteristics

-   Understands instructions
-   Better reasoning
-   Better conversations
-   Safer responses
-   Optimized for real-world tasks

------------------------------------------------------------------------

# Reinforcement Learning from Human Feedback (RLHF)

RLHF is a training process where humans evaluate AI responses.

The model learns which responses people prefer and improves over time.

Benefits:

-   More helpful
-   More accurate
-   Safer
-   Better aligned with user expectations

------------------------------------------------------------------------

# Base LLM vs Instruction-Tuned LLM

  Feature                Base LLM             Instruction-Tuned LLM
  ---------------------- -------------------- -----------------------
  Purpose                Predict next token   Follow instructions
  Chatbot                ❌                   ✅
  Translation            Limited              Excellent
  Code Generation        Limited              Excellent
  Summarization          Limited              Excellent
  Real-world Assistant   ❌                   ✅

------------------------------------------------------------------------

# Deep Dive: How an LLM Works

``` text
User Prompt
      │
      ▼
Tokenization
      │
      ▼
Transformer Model
      │
      ▼
Next Token Prediction
      │
      ▼
Generated Response
```

------------------------------------------------------------------------

# What is a Token?

A **token** is the smallest unit of text processed by an LLM.

Examples:

    Hello world

may become

    ["Hello", " world"]

Tokens determine:

-   Cost
-   Context window
-   Input size
-   Output size

------------------------------------------------------------------------

# Tokenization

Tokenization converts human-readable text into tokens before the model
processes it.

Example

    Artificial Intelligence is changing the world.

↓

    ["Artificial", " Intelligence", " is", " changing", " the", " world", "."]

------------------------------------------------------------------------

# Pre-Training

Pre-training teaches the model general language understanding using
massive datasets such as:

-   Books
-   Articles
-   Websites
-   Documentation
-   Code

Goal:

> Predict the next token.

------------------------------------------------------------------------

# Fine-Tuning

Fine-tuning teaches the model specific behavior.

Examples:

-   Following instructions
-   Writing code
-   Customer support
-   Medical assistants
-   Legal assistants

Instruction tuning is a type of fine-tuning.

------------------------------------------------------------------------

# Inference

**Inference** is the process of generating responses after training.

Training happens once.

Inference happens every time a user sends a prompt.

------------------------------------------------------------------------

# Context Window

A **Context Window** is the maximum number of tokens an LLM can process
at one time.

It includes:

-   User prompt
-   Conversation history
-   Model response

------------------------------------------------------------------------

# Why Prompt Engineering Matters

Better prompts produce better results.

Poor Prompt

    Write Python.

Better Prompt

    Write a Python function to check whether a string is a palindrome.
    Explain every step.
    Include time complexity.

------------------------------------------------------------------------

# Industry Applications

Instruction-Tuned LLMs are used in:

-   ChatGPT
-   GitHub Copilot
-   AI Chatbots
-   Customer Support
-   Enterprise AI
-   Document Summarization
-   Coding Assistants

------------------------------------------------------------------------

# Limitations of LLMs

## Hallucinations

Models can confidently generate incorrect information.

## Knowledge Cutoff

Some models may not know recent events without external tools.

## No True Understanding

LLMs recognize statistical language patterns rather than human-like
understanding.

## Prompt Sensitive

Poor prompts often produce poor outputs.

------------------------------------------------------------------------

# Best Practices

-   Be clear and specific.
-   Provide context.
-   Define the desired output format.
-   Break complex tasks into smaller prompts.
-   Iterate and refine prompts.

------------------------------------------------------------------------

# Common Mistakes

-   Asking vague questions
-   Missing context
-   Expecting perfect factual accuracy
-   Ignoring token limits

------------------------------------------------------------------------

# Interview Questions

### What is an LLM?

A Large Language Model is an AI model trained on massive text datasets
to generate and understand language by predicting tokens.

### What is the difference between a Base LLM and an Instruction-Tuned LLM?

A Base LLM predicts the next token, whereas an Instruction-Tuned LLM is
optimized to follow human instructions using fine-tuning and RLHF.

### What is RLHF?

Reinforcement Learning from Human Feedback is a process where humans
rank model outputs so the model learns preferred behavior.

### What is the difference between Pre-Training and Fine-Tuning?

Pre-training teaches general language understanding.

Fine-tuning teaches task-specific behavior.

### What is Inference?

Inference is the process of generating predictions using a trained
model.

------------------------------------------------------------------------

# Revision Summary

-   ✅ LLMs predict tokens.
-   ✅ Base LLMs perform text continuation.
-   ✅ Instruction-Tuned LLMs follow instructions.
-   ✅ RLHF aligns models with human preferences.
-   ✅ Prompt Engineering improves output quality.
-   ✅ Tokens determine cost and context length.

------------------------------------------------------------------------

# What's Next?

In the next chapter, we will learn the two core principles of Prompt
Engineering:

-   Write clear and specific instructions.
-   Give the model time to think.

# Backend

My backend engineering notes and learning journey, based primarily on the **Backend from First Principles** playlist.

The main focus of this journey is to understand backend development deeply and then apply those concepts using:

* **Python**
* **FastAPI**
* **PostgreSQL**

The playlist is my primary source, and these notes are my personal reference for understanding, practicing, revising, and building backend projects.

---

## 📚 Course

**Backend from First Principles**

[YouTube Playlist](https://www.youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1)

The course covers backend development from fundamentals to production-level concepts.

### Course Progression

```text
Backend Fundamentals
        ↓
HTTP
        ↓
Routing
        ↓
Serialization / Deserialization
        ↓
Authentication / Authorization
        ↓
Validation / Transformation
        ↓
Controllers / Services / Repositories / Middleware
        ↓
REST API Design
        ↓
PostgreSQL
        ↓
Caching
        ↓
Background Jobs
        ↓
Search
        ↓
Error Handling / Fault Tolerance
        ↓
Configuration
        ↓
Logging / Monitoring / Observability
        ↓
Graceful Shutdown
        ↓
Security
        ↓
Scaling / Performance
        ↓
Concurrency / Parallelism
```

---

# 📁 Structure

Each lecture has its own folder and `README.md`.

```text
backend/
│
├── README.md
│
├── 01-backend-roadmap/
│   └── README.md
│
├── 02-backend-engineer-mindset/
│   └── README.md
│
├── 03-what-is-backend/
│   └── README.md
│
├── 04-first-principles/
│   └── README.md
│
├── 05-http/
│   └── README.md
│
├── 06-routing/
│   └── README.md
│
├── 07-serialization-deserialization/
│   └── README.md
│
├── 08-authentication-authorization/
│   └── README.md
│
├── 09-validation-transformation/
│   └── README.md
│
├── 10-backend-architecture/
│   └── README.md
│
├── 11-rest-api-design/
│   └── README.md
│
├── 12-postgresql/
│   └── README.md
│
├── 13-caching/
│   └── README.md
│
├── 14-task-queues-background-jobs/
│   └── README.md
│
├── 15-elasticsearch/
│   └── README.md
│
├── 16-error-handling-fault-tolerance/
│   └── README.md
│
├── 17-configuration-management/
│   └── README.md
│
├── 18-logging-monitoring-observability/
│   └── README.md
│
├── 19-graceful-shutdown/
│   └── README.md
│
├── 20-backend-security/
│   └── README.md
│
├── 21-scaling-performance/
│   ├── part-1/
│   │   └── README.md
│   └── part-2/
│       └── README.md
│
└── 22-concurrency-parallelism/
    └── README.md
```

> Lecture 21 has two parts, so there are **23 videos in total**, while the lecture numbering goes up to 22.

---

# 📝 Lecture Notes Structure

Each lecture has its own `README.md`.

The general structure is:

```text
Lecture Overview
      ↓
Prerequisites
      ↓
Concepts
      ↓
Simple Explanation
      ↓
Deep Explanation
      ↓
How It Works
      ↓
Examples
      ↓
Backend / Python / FastAPI Connection
      ↓
Internal Working
      ↓
Important Details
      ↓
Common Mistakes / Confusions
      ↓
Practical Usage
      ↓
Important Questions
      ↓
Key Takeaways
      ↓
Quick Revision
      ↓
Connection With Other Lectures
```

Not every lecture needs every section. The structure depends on the topic.

---

# 🐍 Tech Focus

```text
Python
   ↓
FastAPI
   ↓
REST APIs
   ↓
PostgreSQL
   ↓
Backend Systems
```

When a concept is relevant to Python or FastAPI, I connect it to them.

I don't want to learn FastAPI as a collection of commands. I want to understand the backend concept first and then understand how FastAPI implements or helps with it.

---

# 🎯 Notes Approach

My notes should be:

* **Deep**
* **Simple to understand**
* **Practical**
* **Technically accurate**
* **Example-driven**
* **Interview useful**

But:

> **Depth ≠ unnecessary length**

I don't want unrelated concepts or advanced information just for the sake of making the notes bigger.

The notes should contain what is needed to properly understand the topic and apply it in backend development.

---

# 🔄 Learning Flow

My overall workflow for this folder:

```text
Watch Lecture
     ↓
Understand Concept
     ↓
Write / Review Notes
     ↓
Implement in Python / FastAPI
     ↓
Practice
     ↓
Build Projects
     ↓
Revise
```

The notes are meant to be a **long-term backend reference** that I can come back to while building projects and preparing for interviews.

---

# 🧠 Final Knowledge Structure

The overall backend knowledge I want to build through this course:

```text
                    BACKEND ENGINEERING
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
        FUNDAMENTALS                 HTTP / APIs
             │                           │
             └─────────────┬─────────────┘
                           ↓
                    REQUEST HANDLING
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        Validation       Auth         Middleware
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                       REST APIs
                           │
                           ↓
                       Database
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
           Caching      Queues        Search
              │            │            │
              └────────────┼────────────┘
                           ↓
                     PRODUCTION
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Reliability     Observability      Security
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                    PERFORMANCE
                           │
                           ↓
                       SCALING
                           │
                           ↓
                 CONCURRENCY / PARALLELISM     
```

This is the **overall mental map** I want to develop while completing the backend course.

The individual lecture notes will go deeper into each part of this structure.

---

# 📌 Current Focus

**Backend Engineering → Python + FastAPI**

The immediate goal is to complete the playlist lecture-by-lecture and build a strong understanding of backend fundamentals before moving heavily into project development.

---

## 🔗 Related

* **Course:** Backend from First Principles
* **Language:** Python
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **Focus:** Backend Engineering

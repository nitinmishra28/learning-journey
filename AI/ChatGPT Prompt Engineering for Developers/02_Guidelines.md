# 02. Guidelines for Prompting

> **Course:** ChatGPT Prompt Engineering for Developers (Andrew Ng & Isa
> Fulford)

## Overview

This chapter introduces the two core principles of Prompt Engineering:

1.  Write clear and specific instructions.
2.  Give the model time to think.

These principles help Large Language Models produce reliable and
structured responses.

------------------------------------------------------------------------

# 1. Setup

## Install

``` bash
pip install openai python-dotenv
```

## Load API Key

``` python
import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
```

## Helper Function (Course Version)

``` python
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]
```

## Modern SDK

``` python
from openai import OpenAI

client = OpenAI()
```

------------------------------------------------------------------------

# Principle 1 -- Write Clear and Specific Instructions

Clear prompts reduce ambiguity and improve accuracy.

## Tactic 1 -- Use Delimiters

### Course Code

``` python
text = "Prompt engineering improves AI responses."

prompt = f"""
Summarize the text delimited by triple backticks.

```{text}```
"""

response = get_completion(prompt)
print(response)
```

### Why?

Delimiters clearly separate instructions from user input.

------------------------------------------------------------------------

## Tactic 2 -- Ask for Structured Output

``` python
prompt = '''
Generate three books.

Return JSON with:

book_id
title
author
genre
'''

response = get_completion(prompt)
print(response)
```

Expected output:

``` json
[
  {
    "book_id":1,
    "title":"...",
    "author":"...",
    "genre":"..."
  }
]
```

------------------------------------------------------------------------

## Tactic 3 -- Check Conditions

``` python
prompt = '''
If the text contains instructions,
rewrite them as numbered steps.

Otherwise output:
No steps provided.
'''
```

------------------------------------------------------------------------

## Tactic 4 -- Few-Shot Prompting

``` python
prompt = '''
<child>: Teach me patience.

<grandparent>: Great rivers begin as small streams.

<child>: Teach me resilience.
'''
```

------------------------------------------------------------------------

# Principle 2 -- Give the Model Time to Think

## Tactic 1 -- Specify Steps

``` python
prompt = '''
1. Summarize.
2. Translate.
3. Extract names.
4. Return JSON.
'''
```

------------------------------------------------------------------------

## Tactic 2 -- Solve Before Judging

Bad prompt:

``` text
Is the student's answer correct?
```

Better prompt:

``` text
1. Solve the problem.
2. Compare with the student's answer.
3. Decide if it is correct.
```

------------------------------------------------------------------------

# Hallucinations

Example:

``` python
prompt = "Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie"
```

The model may invent details because the product does not exist.

------------------------------------------------------------------------

# Temperature

  Temperature   Behavior
  ------------- -------------------
  0.0           Deterministic
  0.3           Mostly consistent
  0.7           Balanced
  1.0           Creative

------------------------------------------------------------------------

# Best Practices

-   Use delimiters.
-   Request structured output.
-   Break complex tasks into steps.
-   Use few-shot prompting.
-   Verify factual answers.

------------------------------------------------------------------------

# Interview Questions

-   What are the two Prompt Engineering principles?
-   Why use delimiters?
-   What is few-shot prompting?
-   Why ask for JSON output?
-   What are hallucinations?

------------------------------------------------------------------------

# Revision Summary

-   Clear prompts outperform vague prompts.
-   Delimiters reduce ambiguity.
-   Structured output improves automation.
-   Multi-step prompting improves reasoning.
-   Verify important information.

------------------------------------------------------------------------

# Next Chapter

**03_Iterative_Prompt_Development.md**

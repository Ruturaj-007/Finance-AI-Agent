import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"


def analyze(data: dict):
    prompt = f"""
You are a senior financial analyst.

You MUST only use the provided data.
If data is limited, explicitly say so.

Data:
{data}

Instructions:
- Do NOT assume unseen financials
- Do NOT generalize beyond data
- Be precise and grounded

Output format:

## Summary
(What is happening based on price & change)

## Insight
(What can realistically be inferred from THIS data only)

## Limitations
(What is missing to make a strong decision)

## Verdict
(Weak / Moderate / Strong signal + reason)
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": prompt
          }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
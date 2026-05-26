import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def design_system(intent):
    print("Stage 2: Designing system architecture...")

    system_prompt = """You are a software architect.
Given a structured app intent, design the system architecture.
Respond ONLY with valid JSON, no explanation, no markdown.

Output this exact structure:
{
  "pages": [{"name": "string", "route": "string", "components": ["string"]}],
  "entities": [{"name": "string", "fields": ["string"]}],
  "api_endpoints": [{"method": "string", "route": "string", "description": "string"}],
  "roles": [{"name": "string", "permissions": ["string"]}]
}"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(intent)}
        ],
        temperature=0.1
    )

    raw = response.choices[0].message.content

    try:
        result = json.loads(raw)
        print("Stage 2 complete ✅")
        return result
    except json.JSONDecodeError:
        print("Stage 2: JSON parsing failed...")
        return None
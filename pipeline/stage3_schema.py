import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def generate_schema(intent, design):
    print("Stage 3: Generating full schema...")

    system_prompt = """You are a schema generation engine.
Given app intent and system design, generate a complete app schema.
Respond ONLY with valid JSON, no explanation, no markdown.

Output this exact structure:
{
  "ui_schema": {
    "pages": [{"name": "string", "route": "string", "components": ["string"]}]
  },
  "api_schema": {
    "endpoints": [{"method": "string", "route": "string", "request_body": {}, "response": {}}]
  },
  "db_schema": {
    "tables": [{"name": "string", "columns": [{"name": "string", "type": "string", "required": true}]}]
  },
  "auth_schema": {
    "type": "string",
    "roles": ["string"],
    "protected_routes": ["string"]
  }
}"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Intent: {json.dumps(intent)}\nDesign: {json.dumps(design)}"}
        ],
        temperature=0.1
    )

    raw = response.choices[0].message.content

    # Remove markdown fences if AI added them
    clean = raw.strip()
    if clean.startswith("```"):
        clean = clean.split("```")[1]
        if clean.startswith("json"):
            clean = clean[4:]
    clean = clean.strip()

    try:
        result = json.loads(clean)
        print("Stage 3 complete ✅")
        return result
    except json.JSONDecodeError:
        print("Stage 3: JSON parsing failed...")
        print("Raw output:", raw[:200])
        return None
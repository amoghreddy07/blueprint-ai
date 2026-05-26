import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def extract_intent(user_prompt):
    print("Stage 1: Extracting intent...")
    
    system_prompt = """You are an intent extraction engine.
Given a user's app idea, extract structured intent.
Respond ONLY with valid JSON, no explanation, no markdown.

Output this exact structure:
{
  "app_name": "string",
  "app_type": "string",
  "core_features": ["feature1", "feature2"],
  "user_roles": ["role1", "role2"],
  "has_auth": true or false,
  "has_payments": true or false,
  "has_analytics": true or false
}"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1
    )
    
    raw = response.choices[0].message.content
    
    try:
        result = json.loads(raw)
        print("Stage 1 complete ✅")
        return result
    except json.JSONDecodeError:
        print("Stage 1: JSON parsing failed, retrying...")
        return None
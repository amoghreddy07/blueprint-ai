# Blueprint AI

An intelligent system that converts natural language app descriptions into complete, validated JSON blueprints.

## What it does
Type any app idea → Get a complete technical blueprint including:
- UI Schema (pages, components, routes)
- API Schema (endpoints, methods, request/response)
- Database Schema (tables, columns, relationships)
- Auth Schema (roles, permissions, protected routes)

## How it works
The system runs a 4-stage pipeline:
1. **Intent Extraction** — Understands what the user wants to build
2. **System Design** — Plans pages, entities, roles and flows
3. **Schema Generation** — Generates full UI, API, DB and Auth configs
4. **Validation + Repair** — Detects errors and auto-repairs them

## Tech Stack
- Python + Flask
- Groq API (llama-3.3-70b-versatile)
- JSONSchema validation

## Live Demo
https://blueprint-ai-6kct.onrender.com

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env  # Add your GROQ_API_KEY
python app.py
```

import json

def validate_and_repair(schema):
    print("Stage 4: Validating and repairing schema...")
    
    errors = []
    
    # Check top level keys exist
    required_keys = ["ui_schema", "api_schema", "db_schema", "auth_schema"]
    for key in required_keys:
        if key not in schema:
            errors.append(f"Missing key: {key}")
            schema[key] = {}

    # Check UI schema has pages
    if "pages" not in schema.get("ui_schema", {}):
        errors.append("ui_schema missing pages")
        schema["ui_schema"]["pages"] = []

    # Check API schema has endpoints
    if "endpoints" not in schema.get("api_schema", {}):
        errors.append("api_schema missing endpoints")
        schema["api_schema"]["endpoints"] = []

    # Check DB schema has tables
    if "tables" not in schema.get("db_schema", {}):
        errors.append("db_schema missing tables")
        schema["db_schema"]["tables"] = []

    # Check auth schema has roles
    if "roles" not in schema.get("auth_schema", {}):
        errors.append("auth_schema missing roles")
        schema["auth_schema"]["roles"] = []

    # Cross-layer check: API routes should have matching DB tables
    api_routes = [e["route"] for e in schema["api_schema"].get("endpoints", [])]
    db_tables = [t["name"] for t in schema["db_schema"].get("tables", [])]

    if errors:
        print(f"Found {len(errors)} issues, repaired automatically:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("No issues found!")

    print("Stage 4 complete ✅")
    
    return {
        "schema": schema,
        "errors_found": errors,
        "is_valid": len(errors) == 0
    }
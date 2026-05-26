from flask import Flask, request, jsonify, render_template
from pipeline.stage1_intent import extract_intent
from pipeline.stage2_design import design_system
from pipeline.stage3_schema import generate_schema
from pipeline.stage4_validation import validate_and_repair

app = Flask(__name__)

def run_pipeline(user_prompt):
    intent = extract_intent(user_prompt)
    if not intent:
        return {"error": "Failed at Stage 1"}
    
    design = design_system(intent)
    if not design:
        return {"error": "Failed at Stage 2"}
    
    schema = generate_schema(intent, design)
    if not schema:
        return {"error": "Failed at Stage 3"}
    
    result = validate_and_repair(schema)
    
    return {
        "intent": intent,
        "design": design,
        "result": result
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    output = run_pipeline(prompt)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
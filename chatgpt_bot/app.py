from flask import Flask, request, jsonify
from crud import create_prompt, get_response, update_prompt, delete_prompt

app = Flask(__name__)


@app.route("/create_prompt", methods=["POST"])
def add_prompt():

    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    prompt_index = create_prompt(prompt)
    return jsonify({"message": "Prompt stored successfully", "index": prompt_index}), 201


@app.route("/get_response/<int:prompt_index>", methods=["GET"])
def fetch_response(prompt_index):

    response = get_response(prompt_index)
    if response is None:
        return jsonify({"error": "Invalid prompt index"}), 404

    return jsonify({"response": response}), 200


@app.route("/update_prompt/<int:prompt_index>", methods=["PUT"])
def modify_prompt(prompt_index):

    data = request.json
    new_prompt = data.get("prompt")
    if not new_prompt:
        return jsonify({"error": "New prompt is required"}), 400

    success = update_prompt(prompt_index, new_prompt)
    if not success:
        return jsonify({"error": "Invalid prompt index"}), 404

    return jsonify({"message": "Prompt updated successfully"}), 200


@app.route("/delete_prompt/<int:prompt_index>", methods=["DELETE"])
def remove_prompt(prompt_index):

    success = delete_prompt(prompt_index)
    if not success:
        return jsonify({"error": "Invalid prompt index"}), 404

    return jsonify({"message": "Prompt deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)

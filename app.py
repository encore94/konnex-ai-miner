from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/fetch", methods=["POST"])
def fetch_task():
    data = request.get_json(force=True)

    task = data.get("task", "").lower()

    if task == "prepare groceries":
        return jsonify({
            "status": "success",
            "steps": [
                "Check grocery list",
                "Collect required items",
                "Pack groceries into bags"
            ]
        })

    return jsonify({
        "status": "failed",
        "reason": "Unknown task"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

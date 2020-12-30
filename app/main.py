import datetime
from flask import Flask, jsonify, render_template, request, g

app = Flask(__name__)
app.secret_key = "jose"

# API routes
@app.route("/", methods=["GET"])
def home():
    return jsonify(message=True)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8099, debug=True)

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    members = ['Brandon', 'Becky', 'Violet', 'Zoey']
    return jsonify(members)

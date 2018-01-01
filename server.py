from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/members")
def members():
    members = ['Brandon', 'Becky', 'Violet', 'Zoey']
    return jsonify(members)

from flask import Flask, jsonify, request
from flask_cors import CORS
import os

import psycopg2

conn = psycopg2.connect("dbname=family_development user=%s" % os.environ['USER'])
cur = conn.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    members = []

    cur.execute("SELECT id, name FROM members")
    for record in cur:
        members.append({
            "id" : record[0],
            "name" : record[1]
        })

    return jsonify(members)

@app.route("/members", methods=['POST'])
def create_member():
    name = request.json['name']

    cur.execute("INSERT INTO members (name) VALUES (%s);", (name,))
    conn.commit()
    return "OK"

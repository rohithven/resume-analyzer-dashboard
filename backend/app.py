from flask import Flask, request, jsonify
from db import get_conn
from analyzer import analyze_resume

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    name = data['name']
    text = data['text']

    result = analyze_resume(text)

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO resumes (name, skills, score) VALUES (%s, %s, %s)",
        (name, result['skills'], result['score'])
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(result)

@app.route('/resumes', methods=['GET'])
def get_resumes():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM resumes")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
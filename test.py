from flask import jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/test")
def test():
    data = {
        "project": "test CORS",
        "date": "251021",
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
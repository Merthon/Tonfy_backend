from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/api/info")
def api_info():
    data = {
        "project": "helloAPI",
        "version": "1.0",
        "description": "A simple API test."
    }
    return jsonify(data)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
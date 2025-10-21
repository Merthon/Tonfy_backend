from flask import jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
# 完成创建
with app.app_context():
    db.create_all()

@app.route("/api/user/add", methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(username=data['name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"})

@app.route('/api/user/list')
def list_user():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

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
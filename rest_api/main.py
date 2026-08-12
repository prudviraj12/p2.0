from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return "I am Iron Man"

if __name__ == "__main__":
    app.run(debug=True)
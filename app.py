from flask import Flask, jsonify
import json
import datetime
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("news_data.json")


@app.route("/")
def index():
    return "Welcome ENSIA Students from Flask!"


@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello World!",
        "status": "success"
    })


@app.route("/news.all.get")
def get_news_all_articles():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return jsonify(data)


@app.route("/news.categories.get")
def get_news_categories():
    return jsonify({
        "title": "List of Categories",
        "time": datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "categories": [
            {"id": 1, "name": "Sports"},
            {"id": 2, "name": "Politics"},
            {"id": 3, "name": "Education"}
        ]
    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)

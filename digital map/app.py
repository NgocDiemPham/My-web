from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "story.json"

app = Flask(__name__)


def load_story() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        story = json.load(file)

    story.setdefault("project", {})
    story.setdefault("chapters", [])
    story.setdefault("map", {})
    story["map"].setdefault("center", [20, 0])
    story["map"].setdefault("zoom", 2)
    return story


@app.route("/")
def index() -> str:
    story = load_story()
    return render_template("index.html", story=story)


@app.route("/api/story")
def api_story():
    return jsonify(load_story())


if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/env python3
"""simple app setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Configuration of babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Bable(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """render the html file"""
    return render_template("templates/index.html")


if __name__ == '__main__':
    app.run(debug=True)
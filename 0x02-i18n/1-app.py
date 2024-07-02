#!/usr/bin/env python3
"""simple app setup"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Bable(app)

class Config():
    """Configuration of babel"""
    LANGUAGES = ["en", "fr"]

@babel.localeselector
def get_lang():
    conf = new Config()
    return conf.LANGUAGES["en"]

@app.route('/')
def index():
    """render the html file"""
    return render_template("templates/index.html")

if __name__ == '__main__':
    app.run(debug=True)

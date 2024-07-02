#!/usr/bin/env python3
"""simple app setup"""

from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config():
    """Configuration of babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Bable(app)


@babel.localeselector
def get_locale():
    '''get the local language'''
    return request.accept_languages.best_match(ap.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """render the html file"""
    return render_template("templates/index.html")


if __name__ == '__main__':
    app.run(debug=True)

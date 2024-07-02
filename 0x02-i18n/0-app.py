#!/usr/bin/env python3
"""simple app setup"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """render the html file"""
    return render_template("templates/index.html")

if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
"""flask application with babel for i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for the Flask application"""
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFUALT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for the supported language"""
    return request.accept_language.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

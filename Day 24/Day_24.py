# Day 24: Introduction to Flask

"""
Today I started learning Flask — a lightweight web framework for Python. It helps you build web applications quickly and easily.

To install Flask:
    pip install flask

Below is my first-ever Flask app!
"""

from flask import Flask

# Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! This is my first web app."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

"""
- `@app.route("/")` maps the root URL (localhost:5000) to the `home()` function.
- `debug=True` lets you see errors in real-time during development.

This was a basic intro. Can't wait to add more routes and features next!
"""

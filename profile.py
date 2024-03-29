import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    
    return render_template("index.html")


@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    age = request.form['age']
    occupation = request.form['occupation']
    
    return jsonify({'fullname': fullname, 'age': age,
                    'occupation': occupation })

# adding comments for testing in Datadog
# check to confirm events are appearing in Events Explorer



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

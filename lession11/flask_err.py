#!/usr/bin/env python3
from flask import Flask, render_template, abort
app = Flask(__name__)
@app.errorhandler(404)
def no_found(error):
    return render_template('404.html'), 404

@app.route('/user/<username>')
def index(username):
    if username == 'xiao':
        abort(404)
    return render_template('user_index.html'), username


if __name__ == '__main__':
    app.run(debug=True)